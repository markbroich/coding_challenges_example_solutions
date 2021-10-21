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
print()


# using while loop rather than recursion and 
# bfs vs dfs switch
def solve(grid, reveiledSet=set(), click=(0,0), bfs=True):
    if grid[click[0]][click[1]] == 'B':
        print('bad input (click)')
        return -1
    elif grid[click[0]][click[1]] == 'M':
        print('hit mine : BOOM!')
        grid[click[0]][click[1]] = 'X'
        return grid
    #
    stackOrQueue = [(click[0], click[1])]
    adjLst = [(-1, -1), (-1, 0), (-1, 1), 
              (0, -1),           (0, 1), 
              (1, -1),  (1, 0),  (1, 1)]
    while stackOrQueue:
        if bfs:
            clr, clc = stackOrQueue.pop(0)
        else:
            # dfs
            clr, clc = stackOrQueue.pop()
        for r, c in adjLst:
            r = clr + r
            c = clc + c
            # returns same grid if all neigbors are reveiledSet
            if not (r, c) in reveiledSet:
                # unreveiled and not mine
                if is_valid(grid, r ,c) and grid[r][c] == 'E':
                    mineCnt = cnt_mines(grid, r, c, adjLst, reveiledSet)
                    if mineCnt > 0:
                        grid[r][c] = str(mineCnt)        
                    else: 
                        # unrevealed empty square now revealed
                        grid[r][c] = 'B'
                        reveiledSet.add((r, c))
                        stackOrQueue.append((r, c))
    return grid




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




# Approach:
#   DFS:
#       add to seen set
#       check if possible neighbor is a mine
#       and cont mines
#       if mines nearby, add number to board and return
#       else: mark as blank and recure all possible neighbors


class Solution:
    def updateBoard(self, board, click):
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        #
        dirLst = [(-1,-1),(-1,0),(-1,1),
                  (0,-1),         (0,1),
                  (1,-1), (1,0),  (1,1)]

        self.rCnt = len(board)
        self.cCnt = len(board[0])
        seen = set()
        def dfs(r, c):
            seen.add((r, c))
            mCnt = 0
            for n in dirLst:
                r_, c_ = r + n[0], c + n[1]
                if not (r_, c_) in seen and self.__inside(r_, c_):
                    if board[r_][c_] == 'M':
                        mCnt += 1
            if mCnt > 0:
                board[r][c] = str(mCnt)
                return
            board[r][c] = 'B'
            for n in dirLst:
                r_, c_ = r + n[0], c + n[1]
                if not (r_, c_) in seen and self.__inside(r_, c_):
                    dfs(r_, c_)

        dfs(click[0], click[1])
        return board

    def __inside(self, r_, c_):
        if r_ < 0 or r_ >= self.rCnt or\
           c_ < 0 or c_ >= self.cCnt:
            return False
        return True

S = Solution()



board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3,0]
exp = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

print(S.updateBoard(board, click) == exp)

board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
click = [1,2]
exp = [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
print(S.updateBoard(board, click) == exp)