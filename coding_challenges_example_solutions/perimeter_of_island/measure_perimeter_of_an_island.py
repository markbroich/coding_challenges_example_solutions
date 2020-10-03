# Measure the size of an island:

# The challenge is to measure the perimeter of an island in the ocean, based on a 2D map that you have been provided.
# In this map, 0 represents ocean and 1 land.

# Here is an example:
#    1111
#    1000
#    1000
#    1000
#    1111
# resulting perimeter is: 4 + 1 + 3 + 3 + 3 + 1  + 4 + 5 = 24

# You can assume there is only one island on the map.


# O(i * j) algo given that each edge is visited in both directions the number of edges between the i*j nodes is proportional 
# to the i*j grid size and all constants such as the two directions of each edge are dropped simplifying to O(i*j)
def get_peri(grid):
    peri = 0
    for i in range(0,len(grid)):
        for j in range(0,len(grid[1])):
            if grid[i][j] == 1:
                peri = count_edge(grid, i, j, peri)
    return peri

def count_edge(grid, i, j, peri):
    # check if edge above is part of perimeter
    # by checking if outside or insides and == water
    if i-1 < 0 or (i-1 >= 0 and grid[i-1][j] == 0):
        peri += 1  
    # same checks for below, left, right
    if i+1 == len(grid) or (i+1 < len(grid) and grid[i+1][j] == 0):
        peri += 1 
    if j-1 < 0 or (j-1 >= 0 and grid[i][j-1] == 0):
        peri += 1 
    if j+1 == len(grid[1]) or (j+1 < len(grid[1]) and grid[i][j+1] == 0):
        peri += 1 
    return peri


grid = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,1,1,1]]
print(get_peri(grid))


# from: https://codechalleng.es