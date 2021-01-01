# Shortest path 
#
# A graph is a set of V of vertices and a set of E of Edges, such 
# that each edge in E connected two of the vertices in V.
# Vertices and edges can be labeled or unlabelled. When they are labeled, 
# the number can be viewed as weight or distance depends on the context.
# It has a wide array of applications from social networking to neural network to engineering field. 


# Given a dictionary of dictionaries that represent a major airline hub and its connecting cities and corresponding distance.

# Please find out the shortest path from city A to city B. You can assume there is always a route between these two cities. Example:
graph = { 
        'a': {'b': 2, 'c': 4, 'e': 1},
          'b': {'a': 2, 'd': 3},
          'c': {'a': 4, 'd': 6},
          'd': {'c': 6, 'b': 3, 'e': 2},
          'e': {'a': 1, 'd': 2},
        }

start = 'a'
end = 'd'


#########################
# My implementation of dijkstras shortest path algo

# the algo find the shortest path from a given start node 
# in a graph to all other nodes. 

# Space complexity is Os(n) where n is the number of nodes
# Time complexity given my implementation is: 
# Ot(n^2) 
# 

# 
# Dijkstras shortest path algo tracks both the shortest path length 
# to any node and the last node on the shortest path. 
# It intis the shortest path length to any note with a very large number 
# while the last visited node stays empty. 
# The algo replaces the shortest path length and the updates the 
# last visited node once a shorter path has been found. 

# beginning from the start node, the algo determines the current path 
# length to any connected node and updated the shortest path length 
# and the last visited node if a shorter path has been found. 
# the algo then determines the next node to visit as the unvisited node 
# with the least cost edge. The algorithm recurs until all nodes have 
# been visited (and all edges have been explored in both directions [if permitted]).  

# the algo uses a priority que (so depth first search) where the priority is determined greedily. 


#########################
# Functions
def find_shortest(graph, start, end, shortest, previous, visited):
    if start not in graph:
        return -1
    
    # get pathlength to current node
    pathlength = shortest[start]
    # at current node to visited
    visited.append(start)
    
    visitNext = None
    visitNextDist = 99999
    for node in graph[start]:
        # update shortest and previous if shorter pathes are found
        shortest, previous = update_shortest_previous(graph, start, node, pathlength, shortest, previous)
        # which one to visit next
        visitNext, visitNextDist = pick_next_node(graph, visited, start, node, visitNext, visitNextDist)

    # if still more nodes to visit:
    if visitNext:
        shortest, previous, visited = find_shortest(graph, visitNext, end, shortest, previous, visited)
    #
    return shortest, previous, visited

# update shortest and previous if shorter pathes are found
def update_shortest_previous(graph, start, node, pathlength, shortest, previous):
    newPathlength = pathlength + graph[start][node]
    curPathlength = shortest[node]
    if newPathlength < curPathlength:
        shortest[node] = newPathlength
        previous[node] = start
    return shortest, previous

# which node to visit next
def pick_next_node(graph, visited, start, node, visitNext, visitNextDist):
    distCurNeighbor = graph[start][node]
    if distCurNeighbor < visitNextDist and node not in visited:
        visitNextDist = distCurNeighbor
        visitNext = node
    return visitNext, visitNextDist

def list_shortest_path_steps(previous, start, end):
    # init list of shortest_path_steps with the end node 
    path = [end]
    # backtrace the previous dict until start has been reached
    # and append nodes to front of list
    while previous[end] != start:
        end = previous[end]
        path.insert(0,end)
    # insert tart node at front of list and return
    path.insert(0,start)
    return(path)

#########################
## Run the code

# init
visited = []
previous = {} # e.g. 'c':'a'
shortest = {} # e.g. 'c':4
for node in graph:
    shortest[node] = 999999 
# set shortest path to start node to 0
shortest[start] = 0 

shortest, previous, visited = find_shortest(graph, start, end, shortest, previous, visited)
print('The shortest from ', start, ' to ', end, ' is: ', shortest[end], ' long.')
print('The path is: ', list_shortest_path_steps(previous, start, end))
print('-------')
print('')




#########################
#### implementation as class
class shortest_path:
    """
    Content: Dijkstras shortest path algorithm
    Inputs: a graph, a start node and an end node 
        the graph is passed as a set that contains dict with 
        each dict having nodes as keys and values beeing dicts 
        of connected nodes: cost 
    Methods; there are two public methods: 
        return_shortest and return_path_steps
    Returns: depending on the method called either the length (cost) 
        of the shortest pass of the nodes visited to get from start to finish
    """
    def __init__(self, graph, start, end):
        self.__graph = graph
        self.__start = start
        self.__end = end
        self.__visited = []
        self.__previous = {} # e.g. 'c':'a'
        self.__shortest = {} # e.g. 'c':4
        self.__pathSteps = []
        for node in self.__graph:
            self.__shortest[node] = 999999
        # set shortest path to start node to 0
        self.__shortest[self.__start] = 0 
    #
    def return_shortest(self):
        self.__find_shortest()
        return self.__shortest[self.__end]
    #
    def return_path_steps(self):
        self.__list_shortest_path_steps()
        return self.__pathSteps
    #
    def __find_shortest(self, __start=None):
        if not __start: 
            __start = self.__start
        if __start not in self.__graph:
            return -1
        # get pathlength to current node
        __pathlength = self.__shortest[__start]
        # at current node to visited
        self.__visited.append(__start)
        #
        self.__visitNext = None
        self.__visitNextDist = 99999
        for __node in self.__graph[__start]:
            # update shortest and previous if shorter pathes are found
            self.__update_shortest_previous(__start, __node, __pathlength)
            # which one to visit next
            self.__pick_next_node(__start, __node)
        # if still more nodes to visit:
        if self.__visitNext:
            self.__find_shortest(self.__visitNext)
    #
    def __update_shortest_previous(self, __start, __node, __pathlength):
        __newPathlength = __pathlength + self.__graph[__start][__node]
        __curPathlength = self.__shortest[__node]
        if __newPathlength < __curPathlength:
            self.__shortest[__node] = __newPathlength
            self.__previous[__node] = __start
    #
    def __pick_next_node(self, __start, __node):
        __distCurNeighbor = self.__graph[__start][__node]
        if __distCurNeighbor < self.__visitNextDist and __node not in self.__visited:
            self.__visitNextDist = __distCurNeighbor
            self.__visitNext = __node
    #
    def __list_shortest_path_steps(self):
        # init list of shortest_path_steps with the end node 
        self.__pathSteps.append(self.__end)
        # backtrace the previous dict until start has been reached
        # and append nodes to front of list
        __currentEnd = self.__end
        while self.__previous[__currentEnd] != self.__start:
            __currentEnd = self.__previous[__currentEnd]
            self.__pathSteps.insert(0,__currentEnd)
        # insert tart node at front of list and return
        self.__pathSteps.insert(0,self.__start)
    #


### init class and run the methods to get the shortest path length and the nodes visited
myShortestPath = shortest_path(graph, start, end)
shortestPathLength = myShortestPath.return_shortest()
shortestPathSteps = myShortestPath.return_path_steps()

print('-as class-')
print('The shortest from ', start, ' to ', end, ' is: ', shortestPathLength, ' long.')
print('The path is: ', shortestPathSteps)



# Known issues: 

# while the dijkstras shortest path algo will find the shortest path using its priority que, 
# it may greedily explore a longer path first e.g. 
# 
# When going from a to d in the examples below it 
# will first expore the b, c path before going:
# directly to d:
# a--2--b--2--c--2--d
#  \               / 
#    ------3------ 
#
# to d via 3:
# a--2--b--2--c--2--d
#  \               / 
#    ---3--e--1--- 
# 


# Big O: While dijkstras shortest path algo is fast, it fails when there are 
# negative cycles, which is can not detect.

# A negative cycles is a cycle where the sum of cost is negative
# In this case we can use the Bellman-Ford algo which is slower at 
# Ot(n*e) where e is the edge count but 
# can detect negative cycles. 
# see: https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/

# max number of edges in a graph: n * (n-1) / 2 
# but since I explore each edge in both directions, 
# the edge count e = n * (n-1) 


# Faster implementations:
# there are faster implementations with Ot(e + n * log n)
# see: https://www.geeksforgeeks.org/dijkstras-algorithm-for-adjacency-list-representation-greedy-algo-8/