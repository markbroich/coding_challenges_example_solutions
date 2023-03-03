'''split into train and test by fraction of the time itnerval'''

import numpy as np


def train_test_split(ratings):
    start = min(ratings['timestamp'])
    end = max(ratings['timestamp'])
    interval = end - start

    ratings['rating'] = ratings['rating'].apply(lambda x: int(np.around(x)))

    train = ratings[ratings['timestamp'] <= (end - interval/3)]
    test = ratings[ratings['timestamp'] >= (start + interval/3)]

    train_y = train[train['timestamp'] >= (start + interval/3)]
    train_X = train[train['timestamp'] < (start + interval/3)]
    test_y = test[test['timestamp'] >= (end - interval/3)]
    test_X = test[test['timestamp'] < (end - interval/3)]
    return train_y, train_X, test_y, test_X
