##  Find the shortest way out of the maze
# given a grid representing a maze, we start at the
# top left (maked zero) and need to find the shortest path
# # aka min number of steps to the exit.
# a passage, wall and the exit are maked with
# 1, 2 and 9, respectivley.


def min_path_out_of_maze(grid):
    if len(grid) < 1: 
        return -1
    
    queue = [(0, 0, 0)]
    while queue:
        r, c, d = queue.pop(0)
        grid[r][c] = 0 
        for r_, c_ in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rm, cm = r+r_, c+c_
            if rm >= 0 and rm < len(grid) and cm >= 0 and cm < len(grid[0]):
                if grid[rm][cm] == 1:
                    queue.append((rm, cm, d+1))      
                elif grid[rm][cm] == 2:
                    return d + 1
                      
    return -1


def testing():
    grid = [[0, 1, 0, 1],
            [0, 1, 1, 1],
            [1, 1, 0, 0],
            [2, 0, 0, 0]]
    print(min_path_out_of_maze(grid) == 5)

    grid = [[0, 1, 1, 1],
            [0, 1, 1, 2],
            [1, 1, 0, 1],
            [1, 0, 0, 0]]
    print(min_path_out_of_maze(grid) == 4)

    grid = [[0, 0, 0, 1],
            [1, 1, 1, 1],
            [1, 1, 0, 0],
            [1, 1, 1, 2]]
    print(min_path_out_of_maze(grid) == 6)

    grid = [[0, 1, 0, 1],
            [1, 1, 1, 1],
            [1, 1, 2, 0],
            [1, 0, 0, 0]]
    print(min_path_out_of_maze(grid) == 4)

    grid = [[0, 1, 0, 1],
            [0, 1, 1, 1],
            [0, 1, 0, 0],
            [2, 0, 0, 0]]
    print(min_path_out_of_maze(grid) == -1)

    grid = []
    print(min_path_out_of_maze(grid) == -1)


# testrun
testing()