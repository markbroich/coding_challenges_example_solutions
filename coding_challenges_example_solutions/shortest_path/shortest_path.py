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
print('')


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




#########################
# Bonus: If the edges are unweighted (or if we ignore the weights, the shortest path 
# can be found using a breath first search [BFS]). Since, BFS explores one set of 
# neighbors (or one distance ring of neighbors) at a time, the distance of the 
# shortest path = the number of sets we explored until we found the target node. 

# Ot(n + e) and Os(n)

# The current 'set of neighbors' (distance ring of neighbors) we are in when mapping 
# a node's shortest distance from start is tracked in the 'dist' dictionary

def bfs(graph, start, end, queue, dist, previous):
    if start == end:
        return dist, previous
    #
    start = queue.pop(0)
    for node in graph[start]:
        if node not in dist:      
            queue.append(node)
            dist[node] = dist[start] + 1
            previous[node] = start
    dist, previous = bfs(graph, start, end, queue, dist, previous)
    return dist, previous

## Run the code
queue = [start]
dist = {start: 0}
previous = {start: None}
dist, previous = bfs(graph, start, end, queue, dist, previous)
shortestPathSteps = list_shortest_path_steps(previous, start, end)

print('-as BFS-')
print('The shortest from ', start, ' to ', end, ' is: ', dist[end], ' long.')
print('The path is: ', shortestPathSteps)
print()
# Note: the BFS length of the shortest path differs from dijkstras shortest path
# given that we report a step count ignoring path cost. 
# Futher, the path found in our case is not unique. 





'''
Shortest Cell Path

In a given grid of 0s and 1s, we have some starting row and column
sr, sc and a target row and column tr, tc. Return the length of the
shortest path from sr, sc to tr, tc that walks along 1 values only.

Each location in the path, including the start and the end, must
be a 1. Each subsequent location in the path must be
4-directionally adjacent to the previous location.

It is guaranteed that grid[sr][sc] = grid[tr][tc] = 1, and the
starting and target positions are different.

If the task is impossible, return -1.

Examples:

input:
grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: 8
(The lines below represent this grid:)
1111
0001
1111

grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: -1
(The lines below represent this grid:)
1111
0001
1011
Constraints:

[time limit] 5000ms
[input] array.array.integer grid
1 ≤ arr.length = arr[i].length ≤ 10
[input] integer sr
[input] integer sc
[input] integer tr
[input] integer tc
All sr, sc, tr, tc are valid locations in the grid, grid[sr][sc] = grid[tr][tc] = 1, and (sr, sc) != (tr, tc).
[output] integer
'''


def shortestCellPath(grid, sr, sc, tr, tc):
  seenDict = {(sr, sc):''}
  queue = [((sr, sc), 0)]
  while queue:
    a, depth = queue.pop(0)
    for adj in [(-1,0), (1, 0), (0, -1), (0, 1)]:
      r = adj[0] + a[0]
      c = adj[1] + a[1]
      if r > -1 and r < len(grid) and  c > -1 and c < len(grid[0]) and (r, c) not in seenDict:
        if r == tr and c == tc:
          return depth + 1
        if grid[r][c] == 1:
          seenDict[(r,c)] = ''
          queue.append(((r, c), depth + 1))
  return -1


grid = [[1,1,1,1],[0,0,0,1],[1,1,1,1]]
sr = 0
sc = 0
tr = 2
tc = 0

print(shortestCellPath(grid, sr, sc, tr, tc))


"""
  - Dijkstra
  - run a dijkstra 
  - visited = {(r, c):}
    - maintain a priority q (key will be the distance)
    - insert (sr, sc, 0)
    - at each step 
      - pop the element (i, j, d)
      - if i == tr and j == tc:
          return d
      - increment the dist insert 1' unvisited neighbors in the q (nr, nc, d+1)
    - return -1
    
Time complexity: O(nm)
Space complexity: O(nm)
"""


'''
Dijkstra is use for weighted graphs with none negatvie edges. 
Ot(ELogV)) as there will be at most O(E) vertices in priority queue 
determining the min dist vertice take log(V) and we do that for each of E edges, ???
hence
Ot(E log(V))
Os(V + E) given that V > E: Os(V)
'''

import heapq as pq


def shortestCellPath(grid: list,
                     sr: int, sc: int,
                     tr: int, tc: int
                     ) -> int:
    m, n = len(grid), len(grid[0])
    q = []
    pq.heappush(q, (0, sr, sc))
    visited = {}

    while q:
        d, i, j = pq.heappop(q)
        visited[(i, j)] = d
        if i == tr and j == tc:
            return d
        # Top and bottom node
        for ni in [max(0, i - 1), min(m-1, i+1)]:
            if ni == i:
                continue
            if grid[ni][j] == 1 and (ni, j) not in visited:
                pq.heappush(q, (d+1, ni, j))
        # Left and right node
        for nj in [max(0, j - 1), min(n-1, j+1)]:
            if nj == j:
                continue
            if grid[i][nj] == 1 and (i, nj) not in visited:
                pq.heappush(q, (d+1, i, nj))
    return -1
     

grid = [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
sr = 0
sc = 0
tr = 2
tc = 0
print(shortestCellPath(grid, sr, sc, tr, tc))





# Test Case #1
print(shortestCellPath([[1,1,1,1],[0,0,0,1],[1,1,1,1]], 0, 0, 2, 0) == 8)
# Test Case #2
print(shortestCellPath([[1,1,1,1],[0,0,0,1],[1,0,1,1]], 0, 0, 2, 0) == -1)
# Test Case #3
print(shortestCellPath([[0,1,0],[1,0,0],[1,0,1]], 2, 0, 1, 0) == 1)
# Test Case #4
print(shortestCellPath([[1,1,1],[0,0,0],[0,0,0]], 0, 1, 0, 0) == 1)
# Test Case #5
print(shortestCellPath([[1,0,1,1],[1,0,1,1],[0,0,1,0],[0,0,0,0]], 1, 3, 0, 0) == -1)
# Test Case #6
print(shortestCellPath([[1,0,1,1,1],[1,0,0,0,0],[0,0,0,0,0],[1,1,0,0,1],[1,0,0,1,1]], 0, 3, 3, 1) == -1)
# Test Case #7
print(shortestCellPath([[0,1,0,1,0],[1,0,1,1,0],[0,0,0,0,0],[1,1,1,1,0],[0,0,1,1,1]], 3, 0, 0, 3) == -1)
# Test Case #8
print(shortestCellPath([[1,1,1,1,0,0],[1,0,0,0,0,0],[0,1,1,0,1,1],[1,0,0,0,1,1],[1,0,1,0,1,0],[0,0,0,1,1,0]], 5, 4, 2, 1) == -1)
# Test Case #9
print(shortestCellPath([[1,1,0,0,1,0],[1,0,0,1,1,1],[0,0,0,0,1,1],[1,0,0,0,0,0],[0,1,1,0,0,1],[0,0,1,1,0,0]], 3, 0, 1, 3) == -1)
print()

#### on a weighted graph
import heapq as pq


def shortestPath(G: dict, s: str, t: str) -> int:
    q = []
    pq.heappush(q, (0, s))
    visitedDict = {}
    prevDict = {}

    while q:
        d, n = pq.heappop(q)
        print(d, n)
        visitedDict[n] = d
        if n == t:
            get_path(prevDict, s, t)
            return d
        for m in G[n]:
            if m not in visitedDict:
                prevDict[m] = n
                pq.heappush(q, (d + G[n][m], m))
    return -1

def get_path(prevDict, s, t):
    cur = t
    path = []
    while cur != s:
        path.append(cur)
        cur = prevDict[cur]
    path.append(s)
    print('shortest path from s to t is: ', path[::-1])





# while the dijkstras shortest path algo will find the shortest path
# using its priority que,
# it may greedily explore a longer path first e.g.
# 
# When going from a to d in the examples below it
# will first expore the b, c path before going:
# directly to d:
# a--2--b--2--c--2--d
#  \               /
#    ------3------
#

# Ex 1
G = {
    'a':{'b':2,'d':3}, 
    'b': {'a':2,'c':2}, 
    'c': {'b':2,'d':2}, 
    'd': {'c':2,'a':3}
    }
print(shortestPath(G, s='a', t='d') == 3)


# to d via 3:
# a--2--b--2--c--2--d
#  \               /
#    ---3--e--1---
# 
# Ex 2
G = {
    'a': {'b':2,'e':4}, 
    'b': {'a':2,'c':2}, 
    'c': {'b':2,'d':2}, 
    'd': {'c':2,'e':1}, 
    'e': {'a':4,'d':1}, 
    }
print(shortestPath(G, s='a', t='d') == 5)
