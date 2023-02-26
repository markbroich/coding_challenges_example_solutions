# to run:
docker build -t dagster .; docker run -v $PWD/output:"/output" dagster

# results will be in output/
# called: RESULT_IMPROVED_GEO_PRECISION.csv, REPORT_IMPORVED_GEOPRECISION.txt and  KEPLER_LOCATIONS_MOVED.html


# ms_hindparcels.ndgeojson needs to be in dagster/output/ 
# it can be downloaded from here: https://drive.google.com/drive/folders/1GP_JJ26DC-D4EAWYLQisbd5eNiiSzkz6

