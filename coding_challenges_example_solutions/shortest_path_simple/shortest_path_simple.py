# Ot(c*r) where c is cols and r is row count
# Os(v) were v are the vertices.
# For a 3*3 grid, there are 9 vertices.
def shortestCellPath(grid, sr, sc, tr, tc):
    steps = 0
    queue = [(sr, sc, steps)]
    while queue:
        r, c, steps = queue.pop(0)
        grid[r][c] = 0
        if r == tr and c == tc:
            return steps
        for r_add, c_add in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if is_option(grid, r + r_add, c + c_add):
                if grid[r + r_add][c + c_add] == 1:
                    queue.append((r + r_add, c + c_add, steps + 1))
    return -1


def is_option(grid, rx, cx):
    if rx < 0 or rx > len(grid) - 1:
        return False
    elif cx < 0 or cx > len(grid[0]) - 1:
        return False
    return True


def tests():
    grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
    sr = 0
    sc = 0
    tr = 2
    tc = 0
    output = 8
    print(shortestCellPath(grid, sr, sc, tr, tc) == output)

    grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 1]]
    sr = 0
    sc = 0
    tr = 2
    tc = 0
    output = -1
    print(shortestCellPath(grid, sr, sc, tr, tc) == output)


tests()
