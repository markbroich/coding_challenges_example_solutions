
'''
K-means clustering is an algorithm that aims to group n observations into k clusters.

There are 3 steps:
* Initialization - K initial "means" (centroids) are generated at random
* Assignment - K clusters are created by associating each observation with the nearest centroid
* Update - The centroid of the clusters becomes the new mean

Assignment and Update steps are repeated iteratively. The user can pass in the number of iterations to run, 
in addition to the data points and the number of clusters (k).

Goal
The goal of this exercise is to get a simplified, working version of K-means for a set of numbers, 
where the input is data and k, and output is the coordinates of the centroids.

You do not need to have any prior knowledge of k-means to do this!

Input
tuples = [(12, 39), (20, 36), (28, 30), (18, 52), (29, 54), (33, 46), (24, 55), (45, 59), (45, 63), (52, 70), (51, 66), (52, 63), (55, 58), (53, 23), (55, 14), (61, 8), (64, 19), (69, 7), (72, 24)]


Expected Output
[[62.33333333, 15.83333333]
 [50,                   63.16666667]
 [23.42857143,  44.57142857]]
'''

import math
import random

random.seed(0)


def k_means(tuples, k, n):
    # Initialization
    min_x, max_x, min_y, max_y = get_min_max_of_x_and_y(tuples)
    cluster_coords = init_cluster_centers(k, min_x, max_x, min_y, max_y)
    #
    for i in range(n):
        # Assignment
        cluster_coord_dict = {}
        for i in range(k):
            cluster_coord_dict[i] = []
        for x, y in tuples:
            idx_cluster = get_nearest(x, y, cluster_coords)
            cluster_coord_dict[idx_cluster].append((x, y))
        # Update
        cluster_coords = get_new_means(cluster_coord_dict)
    return cluster_coords


def get_min_max_of_x_and_y(tuples):
    min_x = min_y = float('inf')
    max_x = max_y = float('-inf')
    for x, y in tuples:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    return min_x, max_x, min_y, max_y


def init_cluster_centers(k, min_x, max_x, min_y, max_y):
    # Limit:
    # if there is little data and k is large,
    # a given center may not have any closest points to it.
    cluster_coords = []
    for i in range(k):
        x = random.randint(min_x, max_x)
        y = random.randint(min_y, max_y)
        cluster_coords.append((x, y))
    return cluster_coords


def get_nearest(x, y, cluster_coords):
    # for large datasets and large number of clusters,
    # an index tree would speed up finding the nearests cluster center
    # to each point.
    idx = None
    min_distance = float('inf')
    for i, v in enumerate(cluster_coords):
        c_x, c_y = v
        # d = √((x2 – x1)^2 + (y2 – y1)^2)
        dist = math.sqrt((x - c_x) ** 2 + (y - c_y) ** 2)
        if dist < min_distance:
            min_distance = dist
            idx = i
    return idx  # index of nearest cluster_coords


def get_new_means(cluster_coord_dict):
    cluster_coords_new = []
    for k, v in cluster_coord_dict.items():
        mean_x, mean_y = calc_mean_coordinate(v)
        cluster_coords_new.append([mean_x, mean_y])
    return cluster_coords_new


def calc_mean_coordinate(arr: list):
    x_sum = 0
    y_sum = 0
    cnt = 0
    for x, y in arr:
        x_sum += x
        y_sum += y
        cnt += 1
    return x_sum / cnt, y_sum / cnt


def test():
    tuples = [(12, 39), (20, 36), (28, 30), (18, 52), (29, 54), (33, 46), (24, 55), (45, 59), (45, 63), (52, 70), (51, 66), (52, 63), (55, 58), (53, 23), (55, 14), (61, 8), (64, 19), (69, 7), (72, 24)]
    expected = [[62.33333333, 15.83333333], [50, 63.16666667], [23.42857143, 44.57142857]]
    print(k_means(tuples, 3, 3))

test()
