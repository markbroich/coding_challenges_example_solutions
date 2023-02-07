import os
import glob
import json
import requests
import zipfile
from io import BytesIO

import numpy as np
import pandas as pd
import geopandas as gpd
from rtree import index
import great_circle_calculator.great_circle_calculator as gcc
# from fuzzywuzzy import fuzz, process

from shapely.geometry import Point, LineString, mapping
from keplergl import KeplerGl

from dagster import asset, Output


MAX_DISTANCE = 1000  # 1km

MS_HINDS_LOCATION_URL = 'https://drive.google.com/uc?id=1WOmj8wSpe8FDn_7opryh9tsng8ZqhAr1'
MS_HINDS_BUILDINGS_URL = 'https://drive.google.com/uc?id=1qO86txHm82OqWbEEIEsaevF_tRFv4PhK'

PATH_BUILDINGS = '/output/storage/get_buildings_df'
PATH_LOCATIONS = '/output/storage/get_location_df'
PATH_PARCELS = '/output/ms_hindparcels.ndgeojson'
PATH_PARCELS_PREPROCESSED = '/output/ms_hindparcels.json'

UNIQUE_COORDS_BUILDING = 'unique_coordinates_building'
UNIQUE_COORDS_LOCATION = 'unique_coordinates_location'
UNIQUE_COORDS_PARCELS = 'unique_coordinates_parcles'

COLS_TO_KEEP_LOCATIONS = ['f_ziploc', 'f_lat', 'f_lon', 'f_city',
                          'f_addr1', 'f_unit', 'geometry',
                          UNIQUE_COORDS_LOCATION]

COLS_TO_KEEP_BUILDINGS = ['ed_lat', 'ed_lon', 'geometry',
                          UNIQUE_COORDS_BUILDING]

COLS_TO_KEEP_PARCELS = ["address", "original_address",
                        'saleprice', 'owner', 'address',
                        'geometry', UNIQUE_COORDS_PARCELS]

EPSG = 4326

LOCATION_LAT_COL = 'f_lat'
LOCATION_LON_COL = 'f_lon'
BUIDLING_LAT_COL = 'ed_lat'
BUIDLING_LON_COL = 'ed_lon'
MOVES_FILENAME = '/output/moves.geojson'

K_NEIGHBORS = 2  # 10

DISTANCE_COL = 'distance_moved'
IMPROVED_PRECISION_LAT = 'improved_precision_lat'
IMPROVED_PRECISION_LON = 'improved_precision_lon'

OUT_PATH_FILE = '/output/RESULT_IMPROVED_GEO_PRECISION.csv'
PATH_REPORT = '/output/REPORT_IMPORVED_GEOPRECISION.txt'
PATH_KEPLER_MAP = '/output/KEPLER_LOCATIONS_MOVED.html'


# @asset
def get_location_df():
    df = pd.read_csv(MS_HINDS_LOCATION_URL)
    df = df.dropna(subset=[LOCATION_LAT_COL, LOCATION_LON_COL])
    return gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df[LOCATION_LON_COL], df[LOCATION_LAT_COL]))


# @asset
def get_buildings_df():
    r = requests.get(MS_HINDS_BUILDINGS_URL)
    z = zipfile.ZipFile(BytesIO(r.content))
    z.extractall("/output/")
    gdf_buildings = gpd.read_file("/output/ms_hinds_buildings.json")
    return gdf_buildings[['ed_bld_uuid', BUIDLING_LAT_COL, BUIDLING_LON_COL, 'geometry']]


# @asset
def get_parcels_df():
    f = open(PATH_PARCELS, "r+")
    d = f.read()
    f.close()

    d = d.replace('\n', ',\n')
    header = '{"type": "FeatureCollection", "name": "ms_hinds_parcels","crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },"features": ['
    footer = ']}'
    d = header + d[:-2] + footer

    with open(PATH_PARCELS_PREPROCESSED, 'w') as f:
        f.write(d)
    f.close()
    return gpd.read_file(PATH_PARCELS_PREPROCESSED)


def drop_duplicate_locations(gdf, lat, lon, col_name):
    # drop duplicates using hash of geometry
    gdf[col_name] = gdf.geometry.map(hash)
    gdf.drop_duplicates(subset=[col_name], inplace=True)
    if lat:
        gdf = gdf[~gdf[lat].isna()]
    if lon:
        gdf = gdf[~gdf[lon].isna()]
    return gdf


def data_preprocessing():
    gdf_building = get_buildings_df()
    gdf_location = get_location_df()
    gdf_parcel = get_parcels_df()
    gdf_building = drop_duplicate_locations(gdf_building, BUIDLING_LAT_COL,
                                            BUIDLING_LON_COL,
                                            UNIQUE_COORDS_BUILDING)
    gdf_location = drop_duplicate_locations(gdf_location, LOCATION_LAT_COL,
                                            LOCATION_LON_COL,
                                            UNIQUE_COORDS_LOCATION)
    gdf_parcel = drop_duplicate_locations(gdf_parcel, None,
                                          None,
                                          UNIQUE_COORDS_PARCELS)
    # drop unnessesary columns
    gdf_building = gdf_building[COLS_TO_KEEP_BUILDINGS]
    gdf_location = gdf_location[COLS_TO_KEEP_LOCATIONS]
    gdf_parcel = gdf_parcel[COLS_TO_KEEP_PARCELS]
    # set to geogrpahic
    gdf_building = gdf_building.set_crs(epsg=EPSG)
    gdf_location = gdf_location.set_crs(epsg=EPSG)
    gdf_parcel = gdf_parcel.set_crs(epsg=EPSG)
    return gdf_building, gdf_location, gdf_parcel


def split_gdf1_using_bounds_of_gdf2(gdf1, gdf2, lat1: str, lon1: str):
    lon_min, lat_min, lon_max, lat_max = gdf2.total_bounds
    gdf_in = gdf1[(gdf1[lat1] >= lat_min) & (gdf1[lat1] <= lat_max)]
    gdf_in = gdf_in[(gdf_in[lon1] >= lon_min) & (gdf_in[lon1] <= lon_max)]
    gdf_out = gdf1.drop(gdf_in.index)
    return gdf_in, gdf_out


def get_gdf_point_in_and_not_in_gdf_poly(gdf_point, gdf_poly, col: str):
    pointInPoly = gpd.sjoin(gdf_point, gdf_poly, how='inner',
                            predicate='within')
    unique_id = set(pointInPoly[col])
    gdf_point_in_poly = gdf_point[gdf_point[col].isin(unique_id)]
    gdf_point_not_in_poly = gdf_point[~gdf_point[col].isin(unique_id)]
    return gdf_point_in_poly, gdf_point_not_in_poly


def get_gdf_location_in_and_not_in_gdf_parcel(gdf_point, gdf_poly, col: str):
    pointInPoly = gpd.sjoin(gdf_point, gdf_poly, how='inner',
                            predicate='within')
    cols = ['f_ziploc', LOCATION_LAT_COL, LOCATION_LON_COL, 'f_city', 'f_addr1', 'f_unit',
            'geometry', 'unique_coordinates_location',
            'unique_coordinates_parcles']
    gdf_point_in_poly = pointInPoly[cols]
    unique_id = set(pointInPoly[col])
    gdf_point_not_in_poly = gdf_point[~gdf_point[col].isin(unique_id)]
    return gdf_point_in_poly, gdf_point_not_in_poly


def get_gdf_buildings_in_and_not_in_gdf_parcel(gdf_poly1, gdf_poly2, col: str):
    poly1_in_poly2 = gpd.sjoin(gdf_poly1, gdf_poly2, how='inner',
                               predicate='within', lsuffix='left',
                               rsuffix='right')
    unique_id = set(poly1_in_poly2[col])
    poly1_not_in_poly2 = gdf_poly1[~gdf_poly1[col].isin(unique_id)]
    return poly1_in_poly2, poly1_not_in_poly2


def add_nearest_building_lat_lon_within_same_parcel_to_locations(gdf_building_in_parcels, gdf_location_not_in_building_in_parcel):
    #
    def get_closest_point_and_distance(unique_id, loc_lon, loc_lat):
        gdf_sub = gdf_building_in_parcels[[BUIDLING_LAT_COL, BUIDLING_LON_COL]][gdf_building_in_parcels[UNIQUE_COORDS_PARCELS].isin([unique_id])]
        if gdf_sub.empty:
            return ((np.nan, np.nan), np.nan)
        gdf_sub['dist'] = gdf_sub.apply(lambda row: get_distance(row[BUIDLING_LON_COL], row[BUIDLING_LAT_COL], loc_lon, loc_lat), axis=1)
        cols = [BUIDLING_LAT_COL, BUIDLING_LON_COL, 'dist']
        gdf_closest = gdf_sub[cols][gdf_sub['dist'] == gdf_sub['dist'].min()]
        if gdf_closest.values[0][2] > MAX_DISTANCE:
            return ((np.nan, np.nan), np.nan)
        return ((gdf_closest.values[0][0], gdf_closest.values[0][1]), gdf_closest.values[0][2])
    #
    gdf_location_not_in_building_in_parcel['new_point'] = gdf_location_not_in_building_in_parcel.apply(lambda row:
        get_closest_point_and_distance(row[UNIQUE_COORDS_PARCELS], row[LOCATION_LON_COL], row[LOCATION_LAT_COL]), axis=1)
    gdf_location_not_in_building_in_parcel = populate_colums(gdf_location_not_in_building_in_parcel, 'new_point')
    return gdf_location_not_in_building_in_parcel


def get_distance(lon1, lat1, lon2, lat2):
    return gcc.distance_between_points((lon1, lat1), (lon2, lat2), unit='meters', haversine=True)


def populate_colums(df, source_col):
    df[IMPROVED_PRECISION_LAT] = df.apply(lambda row: row[source_col][0][0], axis=1)
    df[IMPROVED_PRECISION_LON] = df.apply(lambda row: row[source_col][0][1], axis=1)
    df[DISTANCE_COL] = df.apply(lambda row: row[source_col][1], axis=1)
    return df


def add_nearest_building_lat_lon_to_locations(gdf_building, gdf_location_not_in_building):
    idx = index.Index()
    gdf_building['index_for_tree'] = np.arange(len(gdf_building))
    gdf_building.apply(lambda row:
                       populate_point_index_tree(idx, row['index_for_tree'],
                                                 row[BUIDLING_LAT_COL],
                                                 row[BUIDLING_LON_COL]),
                                                 axis=1)

    gdf_location_not_in_building['knn'] =\
        gdf_location_not_in_building.apply(lambda row:
                                           get_knn_for_point(idx, row[LOCATION_LAT_COL],
                                                             row[LOCATION_LON_COL]), axis=1)

    def get_closest_point_and_distance(knn, loc_lat, loc_lon):
        gdf_sub = gdf_building[[BUIDLING_LAT_COL, BUIDLING_LON_COL]][gdf_building['index_for_tree'].isin(knn)]
        gdf_sub['dist'] = gdf_sub.apply(lambda row: get_distance(row[BUIDLING_LON_COL], row[BUIDLING_LAT_COL], loc_lon, loc_lat), axis=1)
        cols = [BUIDLING_LAT_COL, BUIDLING_LON_COL, 'dist']
        gdf_closest = gdf_sub[cols][gdf_sub['dist'] == gdf_sub['dist'].min()]
        if gdf_closest.values[0][2] > MAX_DISTANCE:
            return ((np.nan, np.nan), np.nan)
        return ((gdf_closest.values[0][0], gdf_closest.values[0][1]), gdf_closest.values[0][2])

    gdf_location_not_in_building['new_point'] = gdf_location_not_in_building.apply(lambda row:
                            get_closest_point_and_distance(row['knn'], row[LOCATION_LAT_COL], row[LOCATION_LON_COL]), axis=1)
    gdf_location_not_in_building = populate_colums(gdf_location_not_in_building, 'new_point')
    return gdf_location_not_in_building


def populate_point_index_tree(idx, i, lat, lon):
    idx.insert(i, (lon, lat, lon, lat))


def get_knn_for_point(idx, lat, lon):
    return list(idx.nearest((lon, lat, lon, lat), K_NEIGHBORS))


def write_moves_to_line_geojson(gdf, lat1, lon1, lat2, lon2, filename) -> None:
    geojson = make_moved_geojson(gdf, lat1, lon1, lat2, lon2)
    with open(filename, 'w') as f:
        f.write(json.dumps(geojson))
    f.close()


def make_moved_geojson(gdf, lat1, lon1, lat2, lon2):
    features = []
    for index, row in gdf.iterrows():
        if np.isnan(row[lat1]) or np.isnan(row[lon1]) or np.isnan(row[lat2]) or np.isnan(row[lon2]):
            continue
        ls = LineString([Point(row[lon1], row[lat1]),
                        Point(row[lon2], row[lat2])])
        features.append({'type': 'Feature', 'properties': {},
                        'geometry': mapping(ls)})
    geojson = {"type": "FeatureCollection", "features": features}
    return geojson


def merge_three_gdfs(gdf_location, gdf_location_not_in_building_in_parcel, gdf_location_not_in_building_not_in_parcel):
    gdf_location_improved_geo_precision =\
        pd.merge(gdf_location, gdf_location_not_in_building_in_parcel,
                 on=UNIQUE_COORDS_LOCATION, how="left", suffixes=('', '_y'))
    col_keep = [LOCATION_LAT_COL, LOCATION_LON_COL, 'f_addr1', IMPROVED_PRECISION_LAT,
                IMPROVED_PRECISION_LON, UNIQUE_COORDS_LOCATION, DISTANCE_COL]
    gdf_location_improved_geo_precision =\
        gdf_location_improved_geo_precision[col_keep]
    #
    gdf_location_improved_geo_precision =\
        pd.merge(gdf_location_improved_geo_precision, gdf_location_not_in_building_not_in_parcel,
                 on=UNIQUE_COORDS_LOCATION, how="left", suffixes=('', '_y'))
    gdf_location_improved_geo_precision =\
        gdf_location_improved_geo_precision[col_keep]
    return gdf_location_improved_geo_precision


def write_report_long(gdf_location_improved_geo_precision, location_incomming_count, locations_inside_count,
        locations_outside_count, locations_inside_building_count, locations_outside_building_count,
        parcel_w_owner_or_address_count, location_not_in_building_in_parcel_count,
        location_not_in_building_not_in_parcel_count,
        location_moved_to_building_from_not_in_parcel_count, location_not_matched_count,
        filename) -> None:
    def custom_mean(df):
        return df.mean(skipna=True)
    # On average, how far are original geolocation moved
    average_moved = float(gdf_location_improved_geo_precision.agg({DISTANCE_COL:custom_mean}))
    with open(filename, 'w') as f:
        f.write(str('On average, how far are original geolocation moved: ' + str(average_moved)) + '\n')
        f.write(' \n')
        f.write(str('location_incomming_count (deduplicated): ' + str(location_incomming_count)) + '\n')
        f.write(' \n')
        f.write(str('locations_inside_count (inside building gdf bound): ' + str(locations_inside_count)) + '\n')
        f.write(' \n')
        f.write(str('locations_outside_count (outside building gdf bound, can not match): ' + str(locations_outside_count)) + '\n')
        f.write(' \n')
        f.write(str('locations_inside_building_count (already good. No need to do anything): ' + str(locations_inside_building_count)) + '\n')
        f.write(' \n')
        f.write(str('locations_outside_building_count (need fitting): ' + str(locations_outside_building_count)) + '\n')
        f.write(' \n')
        f.write(str('parcel_w_owner_or_address_count (useful parcels.... "not roads"): ' + str(parcel_w_owner_or_address_count)) + '\n')
        f.write(' \n')
        f.write(str('location_not_in_building_in_parcel_count (to be fit to closest building within the parcel): ' + str(location_not_in_building_in_parcel_count)) + '\n')
        f.write(' \n')
        f.write(str('location_not_in_building_not_in_parcel_count (to be fit to closest building): ' + str(location_not_in_building_not_in_parcel_count)) + '\n')
        f.write(' \n')
        f.write(str('location_moved_to_building_from_not_in_parcel_count: ' + str(location_moved_to_building_from_not_in_parcel_count)) + '\n')
        f.write(' \n')
        f.write(str('location_not_matched_count: ' + str(location_not_matched_count)) + '\n')
        f.write(' \n')        
        f.write(' \n')
        f.write(str('all locations to be fit to closest building were fit: ' + str(location_not_in_building_not_in_parcel_count == location_moved_to_building_from_not_in_parcel_count)) + '\n')
        f.write(' \n')
        f.write(str('all needed fitting were fit: ' + str(0 == locations_outside_building_count - location_not_in_building_in_parcel_count - location_not_in_building_not_in_parcel_count)) + '\n')
        f.write(' \n')
        f.write(str('Sanity intact: ' + str(0 == locations_inside_count - locations_inside_building_count - location_not_in_building_in_parcel_count - location_not_in_building_not_in_parcel_count)) + '\n')
        f.write(' \n')
        f.write(str('How many points with too little information to move anywhere: ' + str(locations_outside_count + location_not_matched_count)) + '\n')
    f.close()


def create_kepler_map(gdf_location, gdf_building, gdf_moves, gdf_parcel):
    map_1 = KeplerGl()
    map_1.add_data(data=gdf_building[['geometry']], name='buildings')
    # map_1.add_data(data=gdf_parcel[['geometry']], name='parcels')
    map_1.add_data(data=gdf_location[[LOCATION_LAT_COL, LOCATION_LON_COL]], name='locations_pre')
    map_1.add_data(data=gdf_moves, name='locations_moves')
    # center map
    config = {
        'version': 'v1',
        'config': {
            'mapState': {
                'latitude': 32.3,
                'longitude': -90.3,
                'zoom': 12
            }
        }
    }
    map_1.config = config
    map_1.save_to_html(file_name=PATH_KEPLER_MAP)
###############################################################


@asset
def main():
    gdf_building, gdf_location, gdf_parcel = data_preprocessing()
    location_incomming_count = gdf_location.shape[0]

    # Split locations within and not within bounds of buildings
    gdf_location_in, gdf_location_out =\
        split_gdf1_using_bounds_of_gdf2(gdf_location, gdf_building,
                                        LOCATION_LAT_COL, LOCATION_LON_COL)
    locations_inside_count, locations_outside_count = gdf_location_in.shape[0], gdf_location_out.shape[0]

    # Split locations within and not within building polys.
    # Locations already in buildings are assumed to be ideal already!
    gdf_location_already_in_building, gdf_location_not_in_building =\
        get_gdf_point_in_and_not_in_gdf_poly(gdf_location_in, gdf_building,
                                             UNIQUE_COORDS_LOCATION)
    locations_inside_building_count, locations_outside_building_count = gdf_location_already_in_building.shape[0], gdf_location_not_in_building.shape[0]

    # get parcels that are not roads
    gdf_parcel_w_owner_or_address = gdf_parcel[~(gdf_parcel['saleprice'].isna() & gdf_parcel['owner'].isna())]
    parcel_w_owner_or_address_count = gdf_parcel_w_owner_or_address.shape[0]

    # Split locations not in buidlings into in parcels and not in parcels
    gdf_location_not_in_building_in_parcel, gdf_location_not_in_building_not_in_parcel =\
        get_gdf_location_in_and_not_in_gdf_parcel(gdf_location_not_in_building, gdf_parcel_w_owner_or_address,
                                                UNIQUE_COORDS_LOCATION)
    location_not_in_building_in_parcel_count, location_not_in_building_not_in_parcel_count = gdf_location_not_in_building_in_parcel.shape[0], gdf_location_not_in_building_not_in_parcel.shape[0]
    # Split buildings into in parcels and not in parcels
    gdf_building_in_parcels, gdf_building_not_in_parcels = get_gdf_buildings_in_and_not_in_gdf_parcel(gdf_building, gdf_parcel_w_owner_or_address, UNIQUE_COORDS_BUILDING)

    # The locations in a parcel will be mapped to the closest building in the parcel (using great circle distance).
    gdf_location_not_in_building_in_parcel = add_nearest_building_lat_lon_within_same_parcel_to_locations(gdf_building_in_parcels, gdf_location_not_in_building_in_parcel)
    # check if all were fit
    # assert location_not_in_building_in_parcel_count == gdf_location_not_in_building_in_parcel.shape[0]

    # The locations not in a parcel will be mapped to the closest building (using great circle distance).
    # Approach is to build a rtree for the buildings then find for each location the knn buidlings, then use great circle distance
    # to select the closest.
    gdf_location_not_in_building_not_in_parcel = add_nearest_building_lat_lon_to_locations(gdf_building, gdf_location_not_in_building_not_in_parcel)
    location_moved_to_building_from_not_in_parcel_count = gdf_location_not_in_building_not_in_parcel.shape[0]
    location_not_matched_count = gdf_location_not_in_building_not_in_parcel[DISTANCE_COL].isna().sum()

    # merge the 2 kinds of improved_precision location points with the origional gdf_location and write to a csv. 
    gdf_location_improved_geo_precision = merge_three_gdfs(gdf_location, gdf_location_not_in_building_in_parcel, gdf_location_not_in_building_not_in_parcel)
    gdf_location_improved_geo_precision.to_csv(OUT_PATH_FILE)

    # # write fitted locations to a linstring geojson for visualisation
    write_moves_to_line_geojson(gdf_location_improved_geo_precision, LOCATION_LAT_COL,
                                LOCATION_LON_COL, IMPROVED_PRECISION_LAT,
                                IMPROVED_PRECISION_LON, MOVES_FILENAME)

    # create_kepler_map for result visualsiation
    gdf_moves = gpd.read_file(MOVES_FILENAME)
    create_kepler_map(gdf_location, gdf_building, gdf_moves, gdf_parcel)

    write_report_long(gdf_location_improved_geo_precision, location_incomming_count, locations_inside_count,
            locations_outside_count, locations_inside_building_count, locations_outside_building_count,
            parcel_w_owner_or_address_count, location_not_in_building_in_parcel_count,
            location_not_in_building_not_in_parcel_count, location_moved_to_building_from_not_in_parcel_count, location_not_matched_count,
            PATH_REPORT)

    # clean up
    os.remove('/output/moves.geojson')
    for f in glob.glob('/output/ms_hinds*'):
        os.remove(f)


# could use Cheap ruler for distance measures...
# https://blog.mapbox.com/fast-geodesic-approximations-with-cheap-ruler-106f229ad016
# https://github.com/doublemap/cheap-ruler-python/blob/master/cheapruler.py