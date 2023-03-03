'''model predict code'''

import numpy as np
import pandas as pd


def predict_at_k(data, model, k):
    user_ids = list()
    product_ids = list()
    ranks = list()
    for userId, df in data.groupby('userId'):
        pred = model.predict(df.loc[userId])
        productId = np.array(df.reset_index()['movieId'])
        topK_index = np.argsort(pred)[::-1][:k]
        product_ids.extend(list(productId[topK_index]))
        user_ids.extend([userId]*len(topK_index))
        ranks.extend(list(range(1, len(topK_index)+1)))
    return pd.DataFrame({'userId': user_ids, 'movieId': product_ids, 'rank': ranks})


def predict_at_k_for_single_user(data, model, userId, k):
    user_ids = list()
    product_ids = list()
    ranks = list()
    pred = model.predict(data)
    productId = np.array(data.reset_index()['movieId'])
    topK_index = np.argsort(pred)[::-1][:k]
    product_ids.extend(list(productId[topK_index]))
    user_ids.extend([userId]*len(topK_index))
    ranks.extend(list(range(1, len(topK_index)+1)))
    return pd.DataFrame({'userId': user_ids, 'movieId': product_ids, 'rank': ranks})


def coverage(preds,train_X_p):
    test_recs = preds['movieId'].nunique()
    train_movies = train_X_p['movieId'].nunique()
    return test_recs/train_movies
