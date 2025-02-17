# Depth First Search Sudoku solver
# using a 'stack and loop' approach

# this is my simplified and easy to follow DFS version of https://github.com/tphanco/sample/blob/master/DFS_Sudoku.py
# prioritizes readability and simplicity over speed. 

# for some background on the popular game of Sudoku: https://en.wikipedia.org/wiki/Sudoku

# the code can also be run as breadth first search, with is a simple flick of 'mode' switch in the search function. 
# breadth first search is slower than depth first search when solving Sudoku but the code modification is minimal:
# all the mode switch does it change from stack to queue, hence from dfs to bfs (see lines 32 to 36)

# by default the first cell w options (where one ore multiple numbers can be inserted is used). 
# We can increase the efficiency by first filling cells w few options, which prunes the tree
# we can do so by setting fewestOption=True and the runtime comparison shows that filling cells w
# few options first runs in < 1/2 the time.  

import pickle 
import copy
import time

# depth_first_search stack method (when mode='dfs') or breadth_first_search method (when mode='bfs')
def depth_first_search(puzzle, mode='dfs', fewestOption=False):
    start_state = puzzle
    # if the start == the solution, return
    if solution_test(start_state):  
        return start_state
    #
    state_list = []
    state_list.append(start_state) # place initial state onto the state_list = starting position after we checked that it was not the solution
    # while there are states (partially filled puzzles) in the state_list, continue           
    while state_list:                                    
        if(mode=='dfs'):                          
            # take the last state off the stack (DFS pattern)
            current_state = state_list.pop() 
        if(mode=='bfs'):
            # take the last state off the stack (BFS pattern)
            current_state = state_list.pop(0)
        # if the state == the solution, return the solution 
        if solution_test(current_state): 
            return current_state
        # else, add viable states for the first empty cell to the state_list 
        state_list.extend(viable_states(current_state, fewestOption=fewestOption)) 
    return None

# test if a state == the solution; hence, sum of rows, columns and quadrats each == 45 (45 = sum of 1,2,3,4,5,6,7,8,9)
def solution_test(state):
    # expected sum of each row, column or quadrant.
    total = sum(range(1, 9+1))
    # check rows, columns, quadrants and return false if total is invalid
    for row in range(9):
        if (sum(state[row]) != total):
            return False
    for column in range(9):
        if (sum(state[column]) != total):
            return False
    for column in range(0,9,3):
        for row in range(0,9,3):
            block_total = 0
            for block_row in range(0,3):
                for block_column in range(0,3):
                    block_total += state[row + block_row][column + block_column]
            if (block_total != total):
                return False
    return True

# return list of valid states
def viable_states(current_state, fewestOption=False):
    all_possible_states = []
    # get empty cells in puzzle
    cells = get_cells(current_state) 
    #
    if fewestOption: # get row, column and options of cell w fewest options
        row, column, options = fewest_options(cells, current_state)
    else: # use the first cell that has viable options
        row, column = cells[0]
        # get viabale numbers for cell by removing cell's invalid options
        options = get_options(current_state, row, column)
    #
    # create all possible states for empty cell using options
    for number in options: 
        possible_state = state_w_current_number(current_state, number, row, column)
        all_possible_states.append(possible_state)
    return (all_possible_states) 

# return list of empty cells on grid (marked with 0)
def get_cells(state):
    cells=[]
    for row in range(9):
        for column in range(9):
            if state[row][column] == 0:
                cells.append((row, column))
    return cells

# get row, column and options of cell w fewest options
def fewest_options(cells, current_state):
    minOptLen = 99
    minOpt = []
    minRow = minColumn = ''
    for i in range(0,len(cells)):
        row, column = cells[i]
        # get viabale numbers for cell by removing cell's invalid options
        options = get_options(current_state, row, column)
        # find cell w fewer options 
        if len(options) > 0 and len(options) < minOptLen:
            minOptLen = len(options)
            minOpt = options
            minRow, minColumn = cells[i]
            if minOptLen == 1: # if only 1 option, use it
                break
    return minRow, minColumn, minOpt

# get viabale numbers for cell by removing cell's invalid options
def get_options(current_state, row, column):
    # defines valid numbers in puzzle
    options = range(1, 9+1) 
    options = filter_row(options, current_state, row)
    if len(options) == 0:
        return options
    options = filter_col(options, current_state, column)
    if len(options) == 0:
        return options
    options = filter_quad(options, current_state, row, column)
    return options

# filter valid values based on row
def filter_row(options, state, row):
    in_row = [number for number in state[row] if (number != 0)]
    options = filter_values(options, in_row)
    return options

# filter valid values based on column
def filter_col(options, state, column):
    # list of valid values in cell's column
    in_column = [] 
    for column_index in range(9):
        if state[column_index][column] != 0:
            in_column.append(state[column_index][column])
    options = filter_values(options, in_column)
    return options

# filter valid values based on quadrant
def filter_quad(options, state, row, column):
    # list of valid values in cell's quadrant
    in_block = [] 
    row_start = int(row/3)*3
    column_start = int(column/3)*3
    #
    for block_row in range(0, 3):
        for block_column in range(0,3):
            in_block.append(state[row_start + block_row][column_start + block_column])
    options = filter_values(options, in_block)
    return options    

# # how to index the squares in sudoku
# # loop over i (e,g, the row index)
# for i in range(9):
# # get the lower bound of the e.g. square in row direction
# # e.g. subtracting the modolo 'to cut the overhand'
#     # print(int(i/3)*3) # or print(i-i%3)
#     lb = i-i%3
#     # loop over indices in square by addinf 0,1,2 to the lower bound
#     for j in range(0,3):        
#         print('index:', i, 'lower bound:', lb, 'addition:', j, 'location: ', lb + j)

# return set of valid numbers from values that do not appear in used
def filter_values(values, used):
    return [number for number in values if number not in used]

# get state with current number inserted
def state_w_current_number(current_state, number, row, column):
    # to dump an object, and load it later; does the job in 1/3 the time that deepcopy 
    new_state = pickle.loads(pickle.dumps(current_state)) 
    # using deepcopy
    #new_state = copy.deepcopy(current_state) 
    new_state[row][column] = number
    return(new_state)


##### a partially filled puzzle: 
puzzle = [[0,3,9,0,0,0,1,2,0],
        [0,0,0,9,0,7,0,0,0],
        [8,0,0,4,0,1,0,0,6],
        [0,4,2,0,0,0,7,9,0],
        [0,0,0,0,0,0,0,0,0],
        [0,9,1,0,0,0,5,4,0],
        [5,0,0,1,0,9,0,0,3],
        [0,0,0,8,0,5,0,0,0],
        [0,1,4,0,0,0,8,7,0]]

print("A partially filled puzzle: ")
for row in puzzle:
    print (row)
# 


#run the solver (with depth first search 'dfs', which is the default and using the first cell w options)
start_time = time.time()
a_solution = depth_first_search(puzzle, mode='dfs', fewestOption=False)
elapsed_time = time.time() - start_time
if a_solution:
    print ("A solution using dfs and using the first cell w options:")
    for row in a_solution:
        print (row)
else:
    print ("No possible solutions")
print ("Elapsed time: " + str(elapsed_time))
print('')

#run the solver (with depth first search 'dfs', which is the default and using the cell w fewest options)
start_time = time.time()
a_solution = depth_first_search(puzzle, mode='dfs', fewestOption=True)
elapsed_time = time.time() - start_time
if a_solution:
    print ("A solution using dfs and using the cell w fewest options:")
    # for row in a_solution:
    #    print (row)
else:
    print ("No possible solutions")
print ("Elapsed time: " + str(elapsed_time))
print('')

#run the solver (with breadth first search 'bfs' and using the first cell w options)
start_time = time.time()
a_solution = depth_first_search(puzzle, mode='bfs', fewestOption=False)
elapsed_time = time.time() - start_time
if a_solution:
    print ("A solution using bfs and using the first cell w options:")
    # for row in a_solution:
    #    print (row)
else:
    print ("No possible solutions")
print ("Elapsed time: " + str(elapsed_time))
print('')

#run the solver (with breadth first search 'bfs' and using the cell w options)
start_time = time.time()
a_solution = depth_first_search(puzzle, mode='bfs', fewestOption=True)
elapsed_time = time.time() - start_time
if a_solution:
    print ("A solution using bfs and using the cell w fewest options:")
    # for row in a_solution:
    #     print (row)
else:
    print ("No possible solutions")
print ("Elapsed time: " + str(elapsed_time))
print('')

# logic why DFS is preferred over BFS:

# L << B
# where L = length of the shortest path to goal 
# L = all_cells - filled_cells. 
# with all_cells fixed at = 81
# and filled_cells e.g. = 29, 
# so, 
# L = 81 - 29 = 52

# and (average) branching factor B = choices_per_cell * unfilled_cells
# with unfilled_cells = all_cells - filled_cells = L = 52
# and choices_per_cell <= 9
# hence, B  = 9 * 52 (in this example with filled_cells e.g. = 29)

# so: L << B
# BFS will spent a lot of time exploring the diverse branches at a shallow level far from the deeper solution. 
# DFS may go deep down false paths but may also find the solution in as little as L steps 





## the below solution using dfs but first fills the cells 
# where the range of possible values is smallest.
# it also uses recursion thereby eliminating the need for 
# pickel / deepcopy as the board is automatically copies into 
# stack memory as part of the recursion stack


# (code below provided by Pramp.com)

import math

def getCandidates(board, row, col):
    # For some empty cell board[row][col], what possible
    # characters can be placed into this cell
    # that aren't already placed in the same row,
    # column, and sub-board?
    # At the beginning, we don't have any candidates
    candidates = []
    # For each character add it to the candidate list
    # only if there's no collision, i.e. that character 
    # doesn't already exist in the same row, column 
    # and sub-board. Notice the top-left corner of (row, col)'s 
    # sub-board is (row - row%3, col - col%3).
    mylist = ['1','2','3','4','5','6','7','8','9']
    for chr in mylist:
        collision = False
        for i in range(9):
            if board[row][i] == chr: 
              collision = True
              break
            elif  board[i][col] == chr: 
              collision = True
              break
            elif board[(row - row % 3) + int(math.floor(i / 3))][(col - col % 3) + i % 3] == chr:
              collision = True
              break
        if not collision:
          candidates.append(chr)
    return candidates
 
def sudoku_solve(board):
    # For each empty cell, consider 'newCandidates', the
    # set of possible candidate values that can
    # be placed into that cell.
    row = -1 
    col = -1
    candidates = None 
    for r in range(9):
        for c in range(9):
            if (board[r][c] == '.'):
                newCandidates = getCandidates(board, r, c)
                # Then, we want to keep the smallest
                # sized 'newCandidates', plus remember the
                # position where it was found
                if (candidates == None or len(newCandidates) < len(candidates)):
                    candidates = newCandidates
                    row = r 
                    col = c
    # If we have not found any empty cell, then
    # the whole board is filled already
    if (candidates == None):
        return True
    # For each possible value that can be placed
    # in position (row, col), let's
    # place that value and then recursively query
    # whether the board can be solved.  If it can,
    # we are done. 
    for val in candidates:
        board[row][col] = val
        if (sudoku_solve(board)):
            return True
        # The tried value val didn't work so restore  
        # the (row, col) cell back to '.'
        board[row][col] = '.'
    # Otherwise, there is no value that can be placed
    # into position (row, col) to make the
    # board solved
    return False

# same board as puzzle above to compare speed
board = [['.','3','9','.','.','.','1','2','.'],['.','.','.','9','.','7','.','.','.'],['8','.','.','4','.','1','.','.','6'],['.','4','2','.','.','.','7','9','.'],['.','.','.','.','.','.','.','.','.'],['.','9','1','.','.','.','5','4','.'],['5','.','.','1','.','9','.','.','3'],['.','.','.','8','.','5','.','.','.'],['.','1','4','.','.','.','8','7','.']]
start_time = time.time()
print ("A dfs solution first filling cells w fewest possible values and using recursion:")
print(sudoku_solve(board)==True)
elapsed_time = time.time() - start_time
print ("Elapsed time: " + str(elapsed_time))
print('... interestingly this solution does not run faster than dfs using 1st cell w options and a loop w pickle / deepcopy, perhaps due to the recursion overhead.')
print('next step would be to bring the cell prioritization into the loop version of dfs and measure the performance chance (increase). ')

def tests():
    print('a few unit tests:')
    board = [[".",".",".","7",".",".","3",".","1"],["3",".",".","9",".",".",".",".","."],[".","4",".","3","1",".","2",".","."],[".","6",".","4",".",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".","1",".",".","8",".","4","."],[".",".","6",".","2","1",".","5","."],[".",".",".",".",".","9",".",".","8"],["8",".","5",".",".","4",".",".","."]]
    # Expected: True
    print(sudoku_solve(board)== True)
    board = [[".","8","9",".","4",".","6",".","5"],[".","7",".",".",".","8",".","4","1"],["5","6",".","9",".",".",".",".","8"],[".",".",".","7",".","5",".","9","."],[".","9",".","4",".","1",".","5","."],[".","3",".","9",".","6",".","1","."],["8",".",".",".",".",".",".",".","7"],[".","2",".","8",".",".",".","6","."],[".",".","6",".","7",".",".","8","."]]
    # Expected: False
    print(sudoku_solve(board) == False)
    # Test Case #3
    board = [[".","2","3","4","5","6","7","8","9"],["1",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
    # Test Case #4
    print(sudoku_solve(board) == False)
    board =[[".",".","5",".",".","2",".",".","."],[".",".","9",".","4","7",".","2","."],[".",".","8",".","5","6",".",".","1"],[".",".",".",".",".","8","3","4","."],[".",".",".",".",".",".",".",".","6"],[".",".",".",".","3",".","1","8","."],[".","2",".",".",".",".",".",".","."],[".","9",".",".","8",".","6","7","."],["3",".","6","5","7",".",".",".","."]]
    # Test Case #5
    print(sudoku_solve(board) == True)
    board =[[".",".","3","8",".",".","4",".","."],[".",".",".",".","1",".",".","7","."],[".","6",".",".",".","5",".",".","9"],[".",".",".","9",".",".","6",".","."],[".","2",".",".",".",".",".","1","."],[".",".","4",".",".","3",".",".","2"],[".",".","2",".",".",".","8",".","."],[".","1",".",".",".",".",".","5","."],["9",".",".",".",".","7",".",".","3"]]
    # Test Case #6
    print(sudoku_solve(board) == True)
    board = [[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
    print(sudoku_solve(board) == True)

# run tests
tests()


# the brute forth time complexity is O(9^k) where k is the number of unfilled cells. Space complexity is O(n*k) 
# where n is the board size and k is the number of unfilled cells since at max we need to store k matrices of n cells. 
# the time and space complexity of DFS and when first exploring cells w few valid numbers is much smaller. 
# the tree has a depth of k but its width gets such smaller under dfs and w prioritizing cells w few options as many banches 
# get pruned. 


# some code to check the boxes:
# check quadrant and return false if total is invalid
def check_box(col, row, num):
    for block_row in range(0,3):
        for block_column in range(0,3):
            if board[(row - row%3) + block_row][(col - col%3) + block_column] == num:
                return False


## other options for indexing the square:
def sq_indexing():
    # using %
    for row in range(0,9):
        r_sq = row - row % 3
        for col in range(0,8):
            c_sq = col - col % 3
            print()
            for i in range(0,3):
                for j in range(0,3):
                    print(r_sq+i, c_sq+j)

    # sample
    for row in range(0,9):
        r_sq = row - row % 3
        print()
        print('row',row)
        for i in range(0,3):
            print(r_sq+i,)

    # using lookup
    lookup = {
            0:[0,1,2],
            1:[0,1,2],
            2:[0,1,2],
            3:[3,4,5],
            4:[3,4,5],
            5:[3,4,5],
            6:[6,7,8],
            7:[6,7,8],
            8:[6,7,8]
    }

    # sample
    for i in range(0,9):
        for j in lookup[i]:
            print(i,j)
        print()

    for r in range(0,9):
        for c in range(0,9):
            for i in lookup[r]:
                for j in lookup[c]:
                    print(i, j)
                print()

