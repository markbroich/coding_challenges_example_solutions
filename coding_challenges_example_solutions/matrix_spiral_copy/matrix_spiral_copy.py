'''

Matrix Spiral Copy

Given a 2D array (matrix) inputMatrix of integers, create a function 
spiralCopy that copies inputMatrix’s values into a 1D array in a 
spiral order, clockwise. Your function then should return that array. 
Analyze the time and space complexities of your solution.

input:  inputMatrix  = [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]

output: [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 
11, 6, 7, 8, 9, 14, 13, 12]

'''


def spiral_copy(inputMatrix):
    numRows = len(inputMatrix)
    numCols = len(inputMatrix[0])
    topRow = leftCol = 0
    btmRow = numRows
    rightCol = numCols
    result = []

    while (topRow < btmRow and leftCol < rightCol):
        # copy the next top row
        for i in range(leftCol, rightCol):
            result.append(inputMatrix[topRow][i])
        topRow += 1
        # copy the next right hand side column
        for i in range(topRow, btmRow):
            result.append(inputMatrix[i][rightCol-1])
        rightCol -= 1
        # copy the next bottom row
        if topRow < btmRow:
            for i in range(rightCol-1, leftCol-1, -1):
                result.append(inputMatrix[btmRow-1][i])
            btmRow -= 1
        # copy the next left hand side column
        if leftCol < rightCol:
            for i in range(btmRow-1, topRow-1, -1):
                result.append(inputMatrix[i][leftCol])
            leftCol += 1
    return result


inputMatrix =[[1]]
exp = [1]
print(spiral_copy(inputMatrix) == exp)

inputMatrix =[[1],[2]]
exp = [1,2]
print(spiral_copy(inputMatrix) == exp)

inputMatrix =[[1,2]]
exp = [1,2]
print(spiral_copy(inputMatrix) == exp)

inputMatrix =[[1,2],[3,4]]
exp = [1,2,4,3]
print(spiral_copy(inputMatrix) == exp)

inputMatrix =[[1,2,3,4,5],[6,7,8,9,10]]
exp = [1,2,3,4,5,10,9,8,7,6]
print(spiral_copy(inputMatrix) == exp)

inputMatrix =[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
exp = [1,2,3,4,5,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12]
print(spiral_copy(inputMatrix) == exp)

