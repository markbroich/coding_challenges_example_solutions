'''get model inputs for fitting and predictions'''

import pandas as pd


def get_model_input(X_u, X_m, y, tgt_users):
    merged = pd.merge(X_u, y, on=['userId'], how='inner')
    merged = pd.merge(X_m, merged, on=['movieId'], how='outer', suffixes=('_p', '_u'))
    merged = merged.query('userId in @tgt_users')
    merged.fillna(0, inplace=True)
    cols_core = ['userId', 'movieId', 'rating', 'timestamp']
    features_cols = list(merged.drop(columns=cols_core).columns)
    query_list = merged['userId'].value_counts()
    merged = merged.set_index(['userId', 'movieId'])
    query_list = query_list.sort_index()
    merged.sort_index(inplace=True)
    df_x = merged[features_cols]
    df_y = merged['rating']
    return df_x, df_y, query_list


def get_model_input_for_prediction(X_u, X_m, y, tgt_users):
    merged = pd.merge(X_u, y, on=['userId'], how='inner')
    merged = pd.merge(X_m, merged, on=['movieId'], how='outer', suffixes=('_p', '_u'))
    merged = merged.query('userId in @tgt_users')
    merged.fillna(0, inplace=True)
    features_cols = list(merged.drop(columns=['userId', 'movieId']).columns)
    merged = merged.set_index(['userId', 'movieId'])
    merged.sort_index(inplace=True)
    df_x = merged[features_cols]
    return df_x


def get_model_input_for_prediction_for_single_user(X_u, X_m, u):
    X_u_user = X_u.loc[u]
    X_u_user = X_u_user.to_frame().T

    X_u_user = X_u_user.loc[X_u_user.index.repeat(X_m.shape[0])]
    X_u_user.reset_index(drop=True, inplace=True)

    X_u_user = X_u_user.rename(columns={'Mystery': 'Mystery_u',
        'Sci-Fi': 'Sci-Fi_u', 'Comedy': 'Comedy_u', 'Crime': 'Crime_u',
        'Animation': 'Animation_u', 'Adventure': 'Adventure_u',
        'Thriller': 'Thriller_u', 'Action': 'Action_u', 'Western': 'Western_u',
        'Documentary': 'Documentary_u', 'Horror': 'Horror_u', 'War': 'War_u',
        'Film-Noir': 'Film-Noir_u', 'Musical': 'Musical_u',
        'Romance': 'Romance_u', 'Drama': 'Drama_u', 'None': 'None_u',
        'Fantasy': 'Fantasy_u', 'Children': 'Children_u'}, errors="raise")
    X_m = X_m.rename(columns={'Mystery': 'Mystery_p', 'Sci-Fi': 'Sci-Fi_p',
        'Comedy': 'Comedy_p', 'Crime': 'Crime_p', 'Animation': 'Animation_p',
        'Adventure': 'Adventure_p', 'Thriller': 'Thriller_p',
        'Action': 'Action_p', 'Western': 'Western_p',
        'Documentary': 'Documentary_p', 'Horror': 'Horror_p',
        'War': 'War_p', 'Film-Noir': 'Film-Noir_p', 'Musical': 'Musical_p',
        'Romance': 'Romance_p', 'Drama': 'Drama_p', 'None': 'None_p',
        'Fantasy': 'Fantasy_p', 'Children': 'Children_p'}, errors="raise")

    merged = pd.concat([X_m, X_u_user], axis=1)

    merged.fillna(0, inplace=True)
    merged = merged.set_index(['movieId'])
    merged.sort_index(inplace=True)
    return merged
