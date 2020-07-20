## Code to get year w/ max people alive
# by Mark Broich inspired by Gayle Laakmann McDowell's utube video on cracking the coding interview: 
# https://www.youtube.com/watch?v=4UWDyJq8jZg 

# Task: write an algo that return the year with the maximum number of people alive. 

# here, I am using a binary search tree class. The values stored in the tree instance are population deltas per event year (changeval method)
# at the end I query the tree instance in order, track the running sum and return the year with the max people alive (runningsum method)


# example input:
#                    [y_b, y_d]
birth_death_list = [[2000, 2010],
                    [1975, 2005],
                    [1975, 2003],
                    [1803, 1809],
                    [1750, 1869],
                    [1840, 1935],
                    [1803, 1921],
                    [1894, 1921]]


# use a large randomized example
# import random
# birth_death_list = []
# for x in range(100000):
#     b = random.randint(1900,2020)
#     d = b + random.randint(0,99)
#     birth_death_list.append([b, d])


# function to polpulate the population delta per event year tree and return the max runningsum 
# w/o any support functions
def get_pop_peak_w_tree(birth_death_list):
    if(birth_death_list == ""): # simple test: if empty entry
        return('errorcode')
    #
    tree_w_deltas = Node(0,0) # init with year zero and zero

    # populate the tree with birth and death events
    # the tree saves the deltas of a given year e.g. 0, -2, +3, +1, -1
    for person in birth_death_list: 
        y_b = person[0]; y_d = person[1]; 
        tree_w_deltas.changeval(y_b,1) # increment year_birth
        tree_w_deltas.changeval(y_d+1,-1) # decrement year_death
        # the nodes calculate and store the population delta for an event year
    #
    # query the tree in order, track the running sum and return the year with the max people alive
    max_running_sum, running_sum, key_max_rs = tree_w_deltas.runningsum()
    #
    return key_max_rs


# binary search tree class that gets populated with [event_year,increment] or [event_year, decrement] and returns a
# binary search tree instance with [event_year,population_delta] nodes
class Node:
    def __init__(self, key = None, value = None):
        self.left = None
        self.right = None
        self.data = [key, value] #root = Node((key,value))
    #
    # method to insert a node
    def insert(self, key, value):
        if not self.data: # if empty, fill
            self.data = [key, value]; 
            return
        else:
            if self.data:
                if key < self.data[0]:
                    if self.left is None:
                        self.left = Node(key, value) 
                    else: 
                        self.left.insert(key, value) # recursion
                elif key > self.data[0]:
                    if self.right is None:
                        self.right = Node(key, value) 
                    else: 
                        self.right.insert(key, value) # recursion
    #
    # method to change the delta value of a node
    def changeval(self, key, value):
        if key == self.data[0]:
           new_val = self.data[1] + value # update existing delta value
           self.data = [key, new_val]
           return
        elif key < self.data[0]:
            if self.left is None:
                self.insert(key, value)
                return 
            return self.left.changeval(key, value) # recursion
        elif key > self.data[0]:
            if self.right is None:
                self.insert(key, value)
                return 
            return self.right.changeval(key, value) # recursion

    #
    # method to transverse the tree in order and track and retrun the running_sum, 
    # max_running_sum and the key_max_rs (key of the node where the max_running_sum was found)
    def runningsum(self, max_running_sum = 0, running_sum = 0, key_max_rs = None):
        if self.left:
            max_running_sum, running_sum, key_max_rs = self.left.runningsum(max_running_sum, running_sum, key_max_rs) # recursion
        running_sum = running_sum + self.data[1]
        if(running_sum > max_running_sum):
            max_running_sum = running_sum
            key_max_rs = self.data[0]
        if self.right:
            max_running_sum, running_sum, key_max_rs = self.right.runningsum(max_running_sum, running_sum, key_max_rs) # recursion
        return(max_running_sum, running_sum, key_max_rs)
    #
    # method to print the tree
    def printtree(self):
        if self.left:
            self.left.printtree() # recursion
        print(self.data)
        if self.right:
            self.right.printtree() # recursion
    #


# Get py libs for timing and sci notification runtime comparison
import time
from decimal import Decimal

# Run and time the tree-based algo
t0 = time.time()
year_max_alive = get_pop_peak_w_tree(birth_death_list)
print(""); print("pop_peak_w_tree no_support_func result: "); print("year max alive: "+str(year_max_alive))
t1 = time.time()
runtime_O_of_P_plus_Y_algo_tree = t1-t0

print('runtime_O_of_P_plus_Y_algo_tree  '+'  %.2E' % Decimal(runtime_O_of_P_plus_Y_algo_tree))


