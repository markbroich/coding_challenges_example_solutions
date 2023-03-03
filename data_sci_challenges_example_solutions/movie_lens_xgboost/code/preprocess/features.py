''' feature engineering functions'''

import pandas as pd
from tqdm import tqdm


def get_movie_genre(movies):
    # see: https://medium.com/swlh/recommendation-system-for-movies-movielens-grouplens-171d30be334e
    genres_set = set()
    for index, row in movies.iterrows():
        try:
            genres = row.genres.split('|')
            for g in genres:
                genres_set.add(g)
        except:
            genres_set.add(row.genres)

    genres_set.remove('IMAX')
    genres_set.remove('(no genres listed)')
    genres_set.add('None')

    for genre in genres_set:
        movies[genre] = 0

    for index, row in movies.iterrows():
        movieId = row.movieId
        title = row.title
        try:
            # Multiple genres for the movie is separated by '|'
            genres = row.genres.split('|')
        except Exception:
            genres = list(row.genres)

        if 'IMAX' in genres:
            genres.remove('IMAX')
        if '(no genres listed)' in genres:
            genres.remove('(no genres listed)')
            genres.append('None')
        # Changing all columns that are labelled as genres to 1
        # if the movie is in that genre:
        for genre in genres:
            movies.loc[index, genre] = 1

    del movies['title']
    del movies['genres']
    return movies


def get_genre_preference_per_user(ratings):
    genres_occuracne_count = {}
    for i, v in ratings.groupby('userId'):
        cnt = 0
        genres_occuracne_count[i] = {'cnt': 0}
        genres = ['Mystery', 'Sci-Fi', 'Comedy', 'Crime', 'Animation',
                  'Adventure', 'Thriller', 'Action', 'Western',
                  'Documentary', 'Horror', 'War', 'Film-Noir',
                  'Musical', 'Romance', 'Drama', 'None', 'Fantasy', 'Children']
        for g in genres:
            genres_occuracne_count[i][g] = 0
        for index, row in v.iterrows():
            try:
                genres = row.genres.split('|')
                for g in genres:
                    if g in genres_occuracne_count[i]:
                        genres_occuracne_count[i][g] += 1
                    cnt += 1
            except:
                if row.genres in genres_occuracne_count[i]:
                    genres_occuracne_count[i][row.genres] += 1
                cnt += 1
        genres_occuracne_count[i]['cnt'] += cnt

    # genres_occuracne_count
    data = []
    for key, value in genres_occuracne_count.items():
        cnt = 0
        for k, v in value.items():
            if k == 'cnt':
                cnt = v
            else:
                # rounded to nearest percent
                value[k] = int(round(v / cnt * 100, 0))
        del value['cnt']
        value['userId'] = key
        data.append(value)

    return pd.DataFrame(data)


# Copied from bturan19's kaggle nb.
def get_feature_by_user(df):
    res = list()
    for i, v in tqdm(df.groupby('userId')):
        res.append(
            (
                i,
                len(v['movieId']),
                (v['rating'] == 5).sum(),
                (v['rating'] == 4).sum(),
                (v['rating'] == 3).sum(),
                (v['rating'] == 2).sum(),
                (v['rating'] == 1).sum(),
                (v['timestamp'].dt.dayofweek == 0).sum(),
                (v['timestamp'].dt.dayofweek == 1).sum(),
                (v['timestamp'].dt.dayofweek == 2).sum(),
                (v['timestamp'].dt.dayofweek == 3).sum(),
                (v['timestamp'].dt.dayofweek == 4).sum(),
                (v['timestamp'].dt.dayofweek == 5).sum(),
                (v['timestamp'].dt.dayofweek == 6).sum(),
                (v['timestamp'].dt.hour > 17).sum()
            )
        )

    res = pd.DataFrame(
        res,
        columns=[
            'userId', 'revired_products', '5_star_ratings_gave',
            '4_star_ratings_gave', '3_star_ratings_gave',
            '2_star_ratings_gave', '1_star_ratings_gave',
            'monday_review_count_user', 'tuesday_review_count_user',
            'wednesday_review_count_user', 'thursday_review_count_user',
            'friday_review_count_user', 'saturday_review_count_user',
            'sunday_review_count_user','evening_reviews_by_user'
        ])
    return res


def get_feature_by_product(df):
    res = list()
    for i, v in tqdm(df.groupby('movieId')):
        res.append(
            (
                i,
                len(v['userId']),
                (v['rating'] == 5).sum(),
                (v['rating'] == 4).sum(),
                (v['rating'] == 3).sum(),
                (v['rating'] == 2).sum(),
                (v['rating'] == 1).sum(),
                (v['timestamp'].dt.dayofweek == 0).sum(),
                (v['timestamp'].dt.dayofweek == 1).sum(),
                (v['timestamp'].dt.dayofweek == 2).sum(),
                (v['timestamp'].dt.dayofweek == 3).sum(),
                (v['timestamp'].dt.dayofweek == 4).sum(),
                (v['timestamp'].dt.dayofweek == 5).sum(),
                (v['timestamp'].dt.dayofweek == 6).sum(),
                (v['timestamp'].dt.hour > 17).sum(),
            )
        )
    res = pd.DataFrame(
        res,
        columns=[
            'movieId', 'user_count', '1_star_ratings_recieved',
            '2_star_ratings_recieved', '3_star_ratings_recieved',
            '4_star_ratings_recieved', '5_star_ratings_recieved',
            'monday_review_count_item', 'tuesday_review_count_item',
            'wednesday_review_count_item', 'thursday_review_count_item',
            'friday_review_count_item', 'saturday_review_count_item',
            'sunday_review_count_item','evening_reviews_by_movie'
        ])
    return res
