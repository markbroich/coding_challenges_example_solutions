## Rotting oranges

# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
# If this is impossible, return -1.

# Ot(n*m), which is driven by the initial matrix population
def rot_timer(grid):
    timeToRot = 0

    # Ot(n*m)
    dictF = pop_dict(grid, 1)
    # Ot(n*m)
    dictRrecent = pop_dict(grid, 2)

    # BFS where the stack is dictRrecent
    # the recently rotten oranges

    # Ot(k) where k is the number of fresh
    # I loop over recent rotten, which used to be fresh and
    # if I get to rot all the sum of recent rotten over time will be 
    # number of fresh but in each loop I only deal w a subset of 
    # previously fresh
    while True:
        countF = len(dictF)
        dictRnew = {}
        # loop over recently rot 
        for i,j  in dictRrecent:
            dictF, dictRnew = spread_rot(dictF, dictRnew, i, j)

        # no change, hence break
        if countF == len(dictF):
            break

        dictRrecent = dictRnew
        timeToRot += 1
    
    if dictF:
        return -1

    return timeToRot

def pop_dict(grid, flag=1):
    myDict = {}
    # loop over rows
    for i in range(0,len(grid)):
        # loop over cols
        for j in range(0,len(grid[0])):
            if grid[i][j] == flag:
                myDict[(i,j)] = flag
    return myDict

def spread_rot(dictF, dictRnew, i, j):
    # if adj, add to dictRnew and drop from fresh
    adjLst = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
    for adj in adjLst:
        if adj in dictF:
            dictRnew[adj] = 2
            del dictF[adj]
    #
    return dictF, dictRnew




def testing():
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    expected = 4
    print(rot_timer(grid)==expected)

    grid = [[2,1,1],[0,1,1],[1,0,1]]
    expected = -1
    print(rot_timer(grid)==expected)
    # Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, 
    # because rotting only happens 4-directionally.

    grid = [[0,2]]
    expected = 0
    print(rot_timer(grid)==expected)
    # Explanation: Since there are already no fresh oranges at minute 0, 
    # the answer is just 0.

# run tests
testing()




## will add code version using queue w delineator ... 
