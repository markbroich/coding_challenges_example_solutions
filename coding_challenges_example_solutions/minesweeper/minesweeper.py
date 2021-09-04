# Minesweeper
# leedcode 529

# 'M' represents an unrevealed mine,
# 'E' represents an unrevealed empty square,
# 'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
# digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
# 'X' represents a revealed mine.

# DFS recursive
# Ot(M*N) given that all cells only need to be visited once
# Os(M*N)
def solve(grid, reveiledSet=set(), click=(0,0)):
    if grid[click[0]][click[1]] == 'B':
        print('bad input (click)')
        return -1
    elif grid[click[0]][click[1]] == 'M':
        print('hit mine : BOOM!')
        grid[click[0]][click[1]] = 'X'
        return grid
    elif grid[click[0]][click[1]] == 'E':
        # unrevealed empty square now revealed
        grid[click[0]][click[1]] = 'B'
        reveiledSet.add((click[0],click[1]))
    #
    adjLst = [(-1, -1), (-1, 0), (-1, 1), 
              (0, -1),           (0, 1), 
              (1, -1),  (1, 0),  (1, 1)]
    for r, c in adjLst:
        r = click[0] + r
        c = click[1] + c
        # returns same grid if all neigbors are reveiledSet
        if not (r, c) in reveiledSet:
            # unreveiled and not mine
            if is_valid(grid, r ,c) and grid[r][c] == 'E':
                mineCnt = cnt_mines(grid, r, c, adjLst, reveiledSet)
                if mineCnt > 0:
                    grid[r][c] = str(mineCnt)        
                else: 
                    # recure
                    grid = solve(grid, reveiledSet, click=(r,c))  
    return grid


def is_valid(grid, r, c):
    if r < 0:
        return False
    elif r >= len(grid):
        return False
    elif c < 0:
        return False
    elif c >= len(grid[0]):
        return False
    return True


def cnt_mines(grid, r, c, adjLst, reveiledSet):
    mineCnt = 0
    # look at neigbors of unreveiled
    for ru, cu in adjLst:
        ru = r + ru
        cu = c + cu
        if not (ru, cu) in reveiledSet:
            if is_valid(grid, ru, cu) and grid[ru][cu] == 'M':
                mineCnt += 1
    return mineCnt


## run code

# example 1
grid = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3,0]
exp = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
print(solve(grid, reveiledSet=set(), click=click) == exp)
print()

# example 2
grid = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
exp = [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
click = [1,2]
print(solve(grid, reveiledSet=set(), click=click) == exp)
print()

# example 3
grid = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
exp = -1
click = [3,0]
print(solve(grid, reveiledSet=set(), click=click) == exp)