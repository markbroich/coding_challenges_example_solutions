# Depth First Search Sudoku solver
# using a 'stack and loop' approach

# this is my simplified and easy to follow DFS version of https://github.com/tphanco/sample/blob/master/DFS_Sudoku.py
# prioritizes readability and simplicity over speed. 

# for some background on the popular game of Sudoku: https://en.wikipedia.org/wiki/Sudoku


# the code can also be run as breadth first search, with is a simple flick of 'mode' switch in the search function. 
# breadth first search is slower than depth first search when solving Sudoku but the code modification is minimal:
# all the mode switch does it change from stack to queue, hence from dfs to bfs (see lines 29 to 33)

import pickle 
import copy
import time


# depth_first_search stack method (when mode='dfs') or breadth_first_search method (when mode='bfs')
def depth_first_search(puzzle, mode='dfs'):
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
            current_state = state_list.pop(0)
        # if the state == the solution, return the solution (BFS pattern)
        if solution_test(current_state): 
            return current_state
        # else, add viable states for the first empty cell to the state_list 
        state_list.extend(viable_states(current_state)) 
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
def viable_states(current_state):
    all_possible_states = []
    # get first empty cell in puzzle
    #
    row,column = get_cell(current_state) 
    #  
    # could loop over all possible results of get_cell
    # and then select the options with the smallest length
    # get viabale numbers for cell by removing cell's invalid options
    #
    # options = null
    # loop over all possible results of get_cell
    #   newoptions = get_options(current_state, row, column)
    #
    #   if (options == null OR newoptions.size() < options.size()):
    #   options = newoptions
    #       row_ = row 
    #       col_ = column
    #   row = row_
    #   column = col_
    #
    # get viabale numbers for cell by removing cell's invalid options
    options = get_options(current_state, row, column)
    # create all possible states for empty cell using options
    for number in options: 
        possible_state = state_w_current_number(current_state, number, row, column)
        all_possible_states.append(possible_state)
    return (all_possible_states) 

# return first empty cell on grid (marked with 0)
def get_cell(state):
    for row in range(9):
        for column in range(9):
            if state[row][column] == 0:
                return row, column

# get viabale numbers for cell by removing cell's invalid options
def get_options(current_state, row, column):
    # defines valid numbers in puzzle
    options = range(1, 9+1) 
    options = filter_row(options, current_state, row)
    options = filter_col(options, current_state, column)
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


#run the solver (with depth first search 'dfs', which is the default)
start_time = time.time()
a_solution = depth_first_search(puzzle)
elapsed_time = time.time() - start_time
if a_solution:
    print ("A solution using dfs:")
    for row in a_solution:
        print (row)
else:
    print ("No possible solutions")
print ("Elapsed time: " + str(elapsed_time))
print('')

#run the solver (with breadth first search 'bfs')
start_time = time.time()
a_solution = depth_first_search(puzzle, mode='bfs')
elapsed_time = time.time() - start_time
if a_solution:
    print ("A solution using bfs:")
    for row in a_solution:
        print (row)
else:
    print ("No possible solutions")
print ("Elapsed time: " + str(elapsed_time))



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


# many speed upgrades are possible :)