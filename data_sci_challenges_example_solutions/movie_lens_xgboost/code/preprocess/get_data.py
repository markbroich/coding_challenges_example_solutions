''' Code to donwload and unzip the data'''

import requests
from zipfile import ZipFile
import pandas as pd

DATA_PATH = '/data/'


def get_data(file_url: str):
    zipfile_name = file_url.split('/')[-1]
    zipfile_folder = zipfile_name.split('.')[0]

    r = requests.get(file_url, stream=True)
    with open(zipfile_name, "wb") as zipfile:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                zipfile.write(chunk)
    zipfile.close()

    with ZipFile(zipfile_name, 'r') as zObject:
        zObject.extractall(
            path=DATA_PATH)

    ratings = pd.read_csv(DATA_PATH + zipfile_folder + "/ratings.csv")
    movies = pd.read_csv(DATA_PATH + zipfile_folder + "/movies.csv")
    return ratings, movies


def main():
    # file_url = "https://files.grouplens.org/datasets/movielens/ml-latest.zip"
    file_url = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
    ratings, movies = get_data(file_url)
