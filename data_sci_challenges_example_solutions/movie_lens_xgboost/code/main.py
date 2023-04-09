'''
Code that I build on: https://towardsdatascience.com/learning-to-rank-for-product-recommendations-a113221ad8a7

I added:
1) features for genre (genre per movie and how much a user liked each
specific genre)
2) code to predict movie preference considering all movies for all users in
the test data.

re 2): The author of the original code predicted for 'the movies each user in
the test dataset ended up rating'. This makes sense as there are the only
user-movie combinations in the test interval that we have "truth" for.

However, in production we would want to be able to potentially suggest any
movie in the test interval to each user!
All 81,471 unique users and unique 14,808 movies in the test data
(for ml-latest-small) result in 1,206,422,568 rows
(each user should get each of the 14808 movies ranked).
Creating a df w/ 1,206,422,568 rows for ranking is unlikley to fit in memory.
I hence wrote code to break down the task so it can run on a laptop.
'''

from datetime import datetime
from joblib import dump

import numpy as np
import pandas as pd

from preprocess.get_data import get_data
from preprocess.features import get_movie_genre, get_genre_preference_per_user, get_feature_by_user, get_feature_by_product
from preprocess.get_model_input import get_model_input, get_model_input_for_prediction, get_model_input_for_prediction_for_single_user
from preprocess.train_test_split import train_test_split

from model.define_and_fit_model import define_and_fit_model
from model.predict_and_coverage import predict_at_k, predict_at_k_for_single_user, coverage


FILE_URL = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
# FILE_URL = "https://files.grouplens.org/datasets/movielens/ml-latest.zip"
PATH_MODEL = '/data/model.joblib'

PATH_TRAIN_X_U = '/data/train_X_u.joblib'
PATH_TEST_X_U = '/data/test_X_u.joblib'
PATH_TRAIN_X_P = '/data/train_X_p.joblib'
PATH_TEST_X_P = '/data/test_X_p.joblib'

PATH_X_U = '/data/X_u.joblib'
PATH_X_P = '/data/X_p.joblib'
PATH_TGT_USER = '/data/tgt_user.joblib'

N_ESTIMATORS = 100
LEARNING_RATE = 0.1

K = 5


ratings, movies = get_data(FILE_URL)
ratings['timestamp'] = ratings['timestamp'].map(lambda x: datetime.fromtimestamp(x))
ratings = ratings.merge(movies, how= 'left', on= 'movieId')
genre_preference_per_user = get_genre_preference_per_user(ratings)
movies = get_movie_genre(movies)  # could use refine x_star_ratings_gave by genre
ratings = ratings.drop(['title', 'genres'], axis=1)

train_y, train_X, test_y, test_X = train_test_split(ratings)
train_tgt_user = set(train_X['userId']) & set(train_y['userId'])
test_tgt_user = set(test_X['userId']) & set(test_y['userId'])
print('train_X.shape', train_X.shape, 'test_X.shape', test_X.shape)
#
train_X_u = get_feature_by_user(train_X)
test_X_u = get_feature_by_user(test_X)
#
train_X_u = train_X_u.merge(genre_preference_per_user, how= 'left', on= 'userId')
test_X_u = test_X_u.merge(genre_preference_per_user, how= 'left', on= 'userId')
#
train_X_p = get_feature_by_product(train_X)
test_X_p = get_feature_by_product(test_X)
#
train_X_p = train_X_p.merge(movies, how= 'left', on= 'movieId')
test_X_p = test_X_p.merge(movies, how= 'left', on= 'movieId')
#
dump(train_X_u, PATH_TRAIN_X_U)
dump(test_X_u, PATH_TEST_X_U)
dump(train_X_p, PATH_TRAIN_X_P)
dump(test_X_p, PATH_TEST_X_P)        
#
X_train, y_train, query_list_train = get_model_input(train_X_u, train_X_p, train_y, train_tgt_user)
X_test, y_test, query_list_test = get_model_input(test_X_u, test_X_p, test_y, test_tgt_user)


model = define_and_fit_model(X_train, y_train, query_list_train, X_test, y_test, query_list_test, N_ESTIMATORS, LEARNING_RATE)
dump(model, PATH_MODEL)
# variable importance
df_plt = pd.DataFrame({'feature_name': X_train.columns, 'feature_importance': model.feature_importances_})
df_plt.sort_values(by=['feature_importance'],  ascending=False, inplace=True)
print(df_plt.head(30))


# #Only works for ml-latest-small.zip
# predicted = predict_at_k(X_test, model, K)
# print(len(predicted))


# predict for every user in test set
users = set(pd.unique(test_X_u['userId']))
test_X_u = test_X_u.set_index('userId')
user_top_movies = {}
for u in users:
    X = get_model_input_for_prediction_for_single_user(test_X_u, test_X_p, u)
    pred = predict_at_k_for_single_user(X, model, u, K)
    user_top_movies[u] = tuple(pred['movieId'])


print(len(user_top_movies))
print('dictionary with each userId in the test data as key and the top 5 movieIds as values')
print(user_top_movies)

#####
# prediction trail
# movieId = [1, 1301, 1304, 1307, 1354]
# dict = {'userId':[7] * len(movieId),
#         'movieId': movieId}
# test_y = pd.DataFrame(dict)

# tgt_user = set(ratings['userId'])
# X = get_model_input_for_prediction(test_X_u, test_X_p, test_y, tgt_user)
# predicted = predict_at_k(X, model, K)
# print(predicted)


'''
Other Ranking resources:
https://towardsdatascience.com/learning-to-rank-a-complete-guide-to-ranking-using-machine-learning-4c9688d370d4
https://medium.com/swlh/recommendation-system-for-movies-movielens-grouplens-171d30be334e
https://github.com/dao-v/Movie_Recommendation_System/blob/master/Movie%20Recommendation%20System%20-%20GITHUB%20-%20V1.01.ipynb
https://towardsdatascience.com/how-to-evaluate-learning-to-rank-models-d12cadb99d47
https://towardsdatascience.com/how-to-implement-learning-to-rank-model-using-python-569cd9c49b08
'''


# ######### using spark to predict:

# '''
# Using pyspark:
# https://github.com/jadianes/spark-movie-lens/blob/master/notebooks/building-recommender.ipynb
# '''
# from pyspark.sql import SparkSession
# from pyspark import SparkConf


# '''spark_config.py'''


# from pyspark.sql import SparkSession
# from pyspark import SparkConf

# def create_prod_context() -> SparkSession:
#     spark_conf = SparkConf()
#     # as per: http://spark-configuration.luminousmen.com/
#     spark_conf.setAll(
#         [
#             ("spark.default.parallelism", "140"),
#             ("spark.executor.memory", "9g"),
#             ("spark.executor.instances", "14"),
#             ("spark.driver.cores", "5"),
#             ("spark.executor.cores", "3"),
#             ("spark.driver.memory", "9g"),
#             ("spark.driver.maxResultSize", "9g"),
#             ("spark.driver.memoryOverhead", "921m"),
#             ("spark.executor.memoryOverhead", "921m"),
#             ("spark.dynamicAllocation.enabled", "false"),
#             ("spark.sql.adaptive.enabled", "true"),
#             ("spark.sql.files.maxPartitionBytes", "50000000"),  # 50MB max partition size
#             ("spark.sql.partitions", "8000"),
#             ("spark.sql.sources.partitionOverwriteMode", "dynamic"),
#             ("spark.sql.shuffle.partitions", "8000"),
#             ("spark.sql.inMemoryColumnarStorage.compressed", "true"),
#             ("spark.checkpoint.compress", "true"),
#             ("spark.broadcast.compress", "true"),
#             ("spark.rdd.compress", "true"),
#             ("spark.scheduler.mode", "FAIR"),
#             ("spark.sql.broadcastTimeout", "3600"),
#             ("spark.network.timeout", "1200"),
#             ("spark.shuffle.io.maxRetries", "10"),
#             ("spark.shuffle.io.retryWait", "540"),
#             ("spark.rpc.numRetries", "10"),
#             ("spark.task.maxFailures", "5"),
#             # garbage collection from executors
#             ("spark.cleaner.periodicGC.interval", "1min"),  # default 30mins. this allows faster memory cleanup for executors
#             ("spark.cleaner.referenceTracking", "true"),
#             (
#                 "spark.cleaner.referenceTracking.cleanCheckpoints",
#                 "true",
#             ),  # this removes checkpoint directories in EBS volumes after their reference expires.
#             ("spark.cleaner.referenceTracking.blocking", "false"),
#         ]
#     )
#     return SparkSession.builder.config(conf=spark_conf).getOrCreate()


# def main():
#     create_prod_context()


# from spark.spark_config import create_prod_context


# #######
# from pyspark import SparkContext
# from pyspark.sql.functions import udf
# spark = SparkSession.builder.master("local[*]").getOrCreate()
# sc = spark.sparkContext
# broadcast_model = sc.broadcast(model)


# df = spark.createDataFrame(X)
# print((df.count(), len(df.columns)))

# @udf('float')
# def predict_data(*cols):
#    return float(broadcast_model.value.predict((cols,)))

# list_of_columns = df.columns
# df = df.withColumn("prediction", predict_data(*list_of_columns))
# # df.head(5)
# df.select(df['prediction']).take(K)
# # [Row(prediction=0.26368072628974915), Row(prediction=-0.6309579014778137), Row(prediction=0.26368072628974915), Row(prediction=0.26368072628974915), Row(prediction=-0.5870208144187927)]# 


# partitions = 1 # 4

# df = spark.createDataFrame(X)
# rdd = df.rdd
# print(rdd.getNumPartitions())
# rdd = rdd.repartition(partitions)
# print(rdd.getNumPartitions())

# col_count = len(df.columns)
# def movie_prediction(iterator):
#     res = []
#     for x in iterator:
#         x = np.reshape(x, (-1, col_count))
#         res.append(float(broadcast_model.value.predict((x))))
#     return [res]


# mapped = rdd.mapPartitions(movie_prediction)
# result = mapped.collect()
# result
