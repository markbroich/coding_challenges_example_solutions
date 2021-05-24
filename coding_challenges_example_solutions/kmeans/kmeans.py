"""
k-means Implementation

Algorithm:
1) Start with a set of k points as cluster centers (centroids).
2) Assign each x_i to nearest cluster by calculating its distance to each centroid.
3) Update new cluster centers by taking the average of the assigned points.
4) Repeat Step 2 and 3 until none of the cluster assignments change.

# task: complete the methods in kMeansClassifier class so that tests pass

"""

import numpy as np
import copy

# set seed
np.random.seed(1)


TRAIN_DATA = np.array(
    [(8, 3), (9, 2), (5, 0), (2, 9), (3, 7), (0, 5),
     (7, 3), (10, 1), (9, 9), (6, 2), (1, 7), (10, 1),
     (6, 0), (2, 4), (7, 3), (10, 3), (7, 9), (0, 2),
     (1, 3), (8, 7), (8, 9), (6, 1), (1, 7), (10, 10),
     (8, 9)],
     dtype=float)

KNOWN_CENTROIDS = np.array([
    (1.25, 5.5),
    (7.63636364, 1.72727273),
    (8.33333333, 8.83333333)
])
# These are the known centroids
# that a successful k-means training 
# should converge to (with k=3)
# using the above TRAIN_DATA

KNOWN_LABELS = np.array(
    [1, 1, 1, 0, 0, 0, 1, 1, 2, 1,
     0, 1, 1, 0, 1, 1, 2, 0, 0, 2,
     2, 1, 0, 2, 2]
)
# These are the associated cluster labels
# for the above TRAIN_DATA points
# after a successful k-means training
# i.e. using the above KNOWN_CENTROIDS



class kMeansClassifier(object):
    # Incomplete skeleton
    # This class will require `k` to instantiate
    #
    def __init__(self, K):
        self.k = K
        self._centroids = None
    #
    def initialize_points(self, train_data):
        # Takes a numpy array of points
        # and initializes the internal centroids
        # using some algorithm
        self._centroids = train_data[:self.k].copy()
        # ^ This "works", but it is not ideal
        # Why?
    #
    ######################################        
    def distance(self, x, y):
        pass
    #
    def label_single_point(self, pnt):
        pass
    #
    def label_points(self, data):  ##################### start HERE please
        # Given set of input data,
        # returns list of indices for the matching centroids
        pass
    ######################################
    #
    @property
    def centroids(self):
        # Returns the internal centroids
        return self._centroids
    #
    ######################################
    def update_centroids(self, assignments, data):
        pass
    #    
    def train(self, train_data):
        # Implements steps 1-4 as described above
        pass
    ######################################
        

  

class TestClassifier(object):
    def __init__(self):
        self.k = 3
        self.kmodel = kMeansClassifier(self.k)
        # run tests
        self.__test_labeling()
        self.__test_training()
        self.__test_new_predictions()

    #
    def __test_labeling(self):
        # The model is not trained yet,
        # but we want to test labeling with it
        self.kmodel._centroids = KNOWN_CENTROIDS
        #   
        model_labels = self.kmodel.label_points(TRAIN_DATA)      
        #
        print("model_labels={}".format(model_labels))
        print('test_labeling')
        print((np.array_equal(KNOWN_LABELS, model_labels)))
    #
    def __test_training(self):
        #   
        # Train the model
        self.kmodel = kMeansClassifier(self.k)
        self.kmodel.train(train_data=TRAIN_DATA)
        #
        # Test that we got the correct centroids
        model_centroids = self.kmodel.centroids
        model_centroids = sorted(model_centroids, key=lambda x: x[0])
        print('test_training')
        print((np.all(np.isclose(KNOWN_CENTROIDS, model_centroids))))
    #
    def __test_new_predictions(self):
        new_data = np.array([(0, 0),
                             (10, 10),
                             (500, 0),
                             (2, 9),
                             (3, 7),
                             (0, 5)])
        new_labels = self.kmodel.label_points(new_data)
        print('test_new_predictions')
        print(len(set(new_labels)) == 2 and
               len(set(new_labels[3:6])) == 1 and
               len(set(new_labels[1:3])) == 1)



### solution
class kMeansClassifier(object):
    # Incomplete skeleton
    # This class will require `k` to instantiate
    #
    def __init__(self, K):
        self.k = K
        self._centroids = None
    #
    def initialize_points(self, train_data):
        # Takes a numpy array of points
        # and initializes the internal centroids
        # using some algorithm
        np.random.permutation(train_data.shape[0])
        inxCent = np.random.choice(train_data.shape[0], self.k, replace=False)
        self._centroids = train_data[inxCent].copy()
    #  
    def distance(self, x, y):
        euDist = np.sqrt(np.square(y[0]-x[0]) + np.square(y[1]-x[1]))
        return euDist
    #
    def label_single_point(self, pnt):
        distLst = ['']*self.k
        for i, p in enumerate(self._centroids): 
            distLst[i] = (self.distance(p, pnt))
        #   
        return np.argmin(distLst)
    #
    def label_points(self, data): 
        # Given set of input data,
        # returns list of indices for the matching centroids
        clsLst = ['']*data.shape[0]
        for i, p in enumerate(data):
            clsLst[i] = self.label_single_point(p)
        #
        return clsLst
    #
    @property
    def centroids(self):
        # Returns the internal centroids
        return self._centroids
    #
    def update_centroids(self, assignments, data):
        for i in range(0, self.k):
            points = [p for p, a in zip(data, assignments) if a==i]
            if points:
                self._centroids[i] = np.mean(points, axis=0)
    #    
    def train(self, train_data):
        # 1) Start with a set of k points as cluster centers (centroids).
        # 2) Assign each x_i to nearest cluster by calculating its distance to each centroid.
        # 3) Update new cluster centers by taking the average of the assigned points.
        # 4) Repeat Step 2 and 3 until none of the cluster assignments change.
        # Implements steps 1-4 as described above
        self.initialize_points(train_data)   # (1)
        while True:
            cur_cent = copy.deepcopy(self._centroids)
            clsLst = self.label_points(train_data) # (2)
            self.update_centroids(clsLst, train_data) # (3)
            if np.all(cur_cent == self._centroids): # (4)
                break
    #
########################
def main ():
    TESTS = TestClassifier()


if __name__ == '__main__':
    main()



