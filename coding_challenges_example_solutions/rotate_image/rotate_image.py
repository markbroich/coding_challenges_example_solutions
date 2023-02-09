'''You are given an n x n 2D matrix representing an image,
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you
have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
1 2 3					7 4 1
4 5 6					8 5 2
7 8 9					9 6 3

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
  5 1 9 11
  2 4 8 10
 13

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
'''


from typing import List


# Ot(n) Os(1) where n is number of cells in the matrix
def rotate(matrix):

    def get_new_coords(old_row, old_col):
        '''rules to find new_row and new_col
        based on old_row_old_col'''
        new_row = old_col
        new_col = len(matrix) - 1 - old_row
        return new_row, new_col

    def mover(v_to_place: int, new_row: int, new_col: int) -> int:
        v_next_to_place = matrix[new_row][new_col]
        matrix[new_row][new_col] = v_to_place
        return v_next_to_place, new_row, new_col

    start_row = start_col = 0
    old_row = start_row
    old_col = start_col
    rim = int(len(matrix) / 2)
    # starting from the other rim going inwards
    for i in range(rim):
        steps = len(matrix) - 1 - 2 * i
        # moving len of rim - 1 steps
        for j in range(steps):
            # pull out value
            v_to_place = matrix[old_row][old_col]
            for _ in range(4):
                # find new location
                new_row, new_col = get_new_coords(old_row, old_col)
                # place value in new location and return its prior content
                v_to_place, old_row, old_col =\
                    mover(v_to_place, new_row, new_col)
            old_row = start_row
            old_col = start_col + 1 + j
        start_row += 1
        start_col += 1
        old_row = start_row
        old_col = start_col
    return matrix


# the elegant solution.
# Ot(n) Os(1) where n is number of cells in the matrix
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)
        return matrix

    def transpose(self, matrix: List[List[int]]) -> None:
        for r in range(len(matrix)):
            for c in range(r + 1, len(matrix)):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    def reflect(self, matrix: List[List[int]]) -> None:
        for r in range(len(matrix)):
            for c in range(len(matrix) // 2):
                matrix[r][c], matrix[r][len(matrix) - 1 - c] =\
                    matrix[r][len(matrix) - 1 - c], matrix[r][c]


def tests():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    expected = [[7,4,1],[8,5,2],[9,6,3]]
    print(rotate(matrix) == expected)
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    S1 = Solution()
    S1.rotate(matrix)

    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    expected = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    print(rotate(matrix) == expected)
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    print(S1.rotate(matrix) == expected)
    '''
    [5,1,9,11]
    [2,4,8,10]
    [13,3,6,7]
    [15,14,12,16]

    [15,13,2,5]
    [14,3,4,1]
    [12,6,8,9]
    [16,7,10,11]
    '''

    matrix = [
        [1,  2, 3, 4,5],
        [6,  7, 8, 9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]]
    expected = [
        [21,16,11,6,1],
        [22,17,12,7,2],
        [23,18,13,8,3],
        [24,19,14,9,4],
        [25,20,15,10,5]]

    print(rotate(matrix) == expected)
    matrix = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]]
    print(S1.rotate(matrix) == expected)


tests()
