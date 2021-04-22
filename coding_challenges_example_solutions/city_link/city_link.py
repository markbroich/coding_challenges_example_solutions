"""
Number of Provinces

There are n cities. Some of them are connected, while some are not. 
If city a is connected directly with city b, and city b is connected 
directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and 
no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 
if the ith city and the jth city are directly connected, and 
isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:
[Image: https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg]
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
[Image: https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg]
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

"""

def city_link(isConnected):
    provinceCount = 0
    visitedSet = set()
    def dfs(i):
        for j, connected in enumerate(isConnected[i]):
            if j not in visitedSet and connected == 1:
                visitedSet.add(j)
                dfs(j)
        #
    for i in range(len(isConnected)):
        if i not in visitedSet and 1 in isConnected[i]:
            provinceCount += 1   
            # dfs from that city
            dfs(i)

    return provinceCount 


def testing():  
    isConnected = [[1,1,0],[1,1,1],[0,1,1]]
    print(city_link(isConnected) == 1)

    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    print(city_link(isConnected) == 2)

    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    print(city_link(isConnected) == 3)

    isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    print(city_link(isConnected) == 1)

    isConnected = [[0,0,0],[0,0,0],[0,0,0]]
    print(city_link(isConnected) == 0)

testing()
