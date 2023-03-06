'''
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1).
The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting
a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination,
where start = [startrow, startcol] and destination = [destinationrow, destinationcol],
return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).


Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)
Output: true


Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)
Output: false

Explanation: There is no way for the ball to stop at the destination.
'''

# https://leetcode.com/problems/the-maze/


def can_score_goal(grid: list, start: list, destination: list) -> bool:
    if not start or not destination or not grid:
        return -1
    row_start, col_start = start
    row_dest, col_dest = destination
    seen = set([(row_start, col_start)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def move_ball(cur_row, cur_col):
        if cur_row == row_dest and cur_col == col_dest:
            return True
        # only makr stop points as seen
        seen.add((cur_row, cur_col))
        for row_mod, col_mod in directions:
            new_row = cur_row + row_mod
            new_col = cur_col + col_mod
            if check_condiction(new_row, new_col, grid, seen):
                while check_condiction(new_row + row_mod, new_col + col_mod, grid, seen):
                    # start rolling
                    new_row += row_mod
                    new_col += col_mod
                if (new_row + row_mod, new_col + col_mod) in seen:
                    # if I stopped b/c I would have rolled into a 'seen'
                    continue
                if move_ball(new_row, new_col):
                    return True
        return False
    return move_ball(row_start, col_start)


def check_condiction(row, col, grid, seen):
    if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])\
            and grid[row][col] == 0 and (row, col) not in seen:
        return True
    return False


grid = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]

start = (0, 4)
destination = (4, 4)
expected = True
print(can_score_goal(grid, start, destination) == expected)


grid = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]

start = (0, 4)
# we can not stop at destination. Only roll through
destination = (3, 2)
expected = False
print(can_score_goal(grid, start, destination) == expected)


grid = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0]]

start = (0, 4)
destination = (0, 2)
expected = True
# 0, 2 can not be marked as seen when we pass through.
print(can_score_goal(grid, start, destination) == expected)
