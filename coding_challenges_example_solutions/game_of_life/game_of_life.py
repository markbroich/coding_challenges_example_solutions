## Game of Life

# According to Wikipedia's article: "The Game of Life, also known
# simply as Life, is a cellular automaton devised by the British
# mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell
# has an initial state: live (represented by a 1) or dead
# (represented by a 0). Each cell interacts with its eight neighbors
# (horizontal, vertical, diagonal) using the following four rules
# (taken from the above Wikipedia article):

# -Any live cell with fewer than two live neighbors dies
#   as if caused by under-population.
# -Any live cell with two or three live neighbors lives on
#   to the next generation.
# -Any live cell with more than three live neighbors dies,
#   as if by over-population.
# -Any dead cell with exactly three live neighbors becomes
#   a live cell, as if by reproduction.

# The next state is created by applying the above rules simultaneously
# to every cell in the current state, where births and deaths occur
# simultaneously.

# Given the current state of the m x n grid board, return the next state.

# example:
grid = [[0,1,0],
        [0,0,1],
        [1,1,1],
        [0,0,0]]

nextStare = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

# Ot(r*c)
# Os(r*c)
def game_of_life(grid):
    # copy the grid
    gridCp = [[grid[r][c] for c in range(0, len(grid[0]))] 
              for r in range(0, len(grid))]
    # loop over grid
    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            cnt = cnt_neighbors(gridCp, r, c)
            grid = apply_rules(grid, r, c, gridCp, cnt)
    return grid


def cnt_neighbors(grid, r, c):
    cnt = 0
    neigh = [(-1, -1), (-1, 0), (-1, 1),
             (0,-1), (0,1),
             (1, -1), (1, 0), (1, 1)]
    for rm, cm in neigh:
        r_, c_ = r+rm, c+cm
        if (r_ >= 0 and r_ < len(grid) and
            c_ >= 0 and c_ < len(grid[0])):
            if grid[r_][c_] == 1:
                cnt += 1
    return cnt


def apply_rules(grid, r, c, gridCp, cnt):
    # cell w < 2 live neighbors or > 3 live neighbors dies
    # dead cell w 3 live neighbors becomes a live cell
    if gridCp[r][c] == 1 and (cnt < 2 or cnt > 3):
        grid[r][c] = 0
    elif gridCp[r][c] == 0 and cnt == 3:
        grid[r][c] = 1
    return grid


# Ot(r*c)
# Os(1) in place
def game_of_life_inplace(grid):
    # loop over grid
    for r in range(0,len(grid)):
        for c in range(0,len(grid[0])):
            cnt = cnt_neighbors_inplace(grid, r, c)
            grid = apply_rules_inplace(grid, r, c, cnt)
    # loop over grid
    for r in range(0,len(grid)):
        for c in range(0,len(grid[0])):
            grid = exchange_placeholdes(grid, r, c)
    return grid


def cnt_neighbors_inplace(grid, r, c):
    cnt = 0
    neigh = [(-1, -1), (-1, 0), (-1, 1),
             (0,-1), (0,1),
             (1, -1), (1, 0), (1, 1)]
    for rm, cm in neigh:
        r_, c_ = r+rm, c+cm
        if (r_ >= 0 and r_ < len(grid) and
            c_ >= 0 and c_ < len(grid[0])):
            if abs(grid[r_][c_]) == 1:
                cnt += 1
    return cnt


def apply_rules_inplace(grid, r, c, cnt):
    # cell w < 2 live neighbors or > 3 live neighbors dies
    # dead cell w 3 live neighbors becomes a live cell
    if abs(grid[r][c]) == 1 and (cnt < 2 or cnt > 3):
        grid[r][c] = -1  # died
    elif (grid[r][c] == 0 or grid[r][c] == 2) and cnt == 3:
        grid[r][c] = 2  # became alive
    return grid


def exchange_placeholdes(grid, r, c):
    if grid[r][c] > 0:
        grid[r][c] = 1
    else:
        grid[r][c] = 0
    return grid


## run code

# Os(r*c)
grid = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
exp = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
print(game_of_life(grid) == exp)

# Os(1) inplace
grid = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
exp = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
print(game_of_life_inplace(grid) == exp)