'''
Move Zeros To End

Given a static-sized array of integers arr, move all zeroes in the array to the end of the array. You should preserve the relative order of items in the array.
We should implement a solution that is more efficient than a naive brute force.

Examples:
input:  arr = [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]
output: [1, 10, 2, 8, 3, 6, 4, 5, 7, 0, 0, 0, 0, 0]
Constraints:

[time limit] 5000ms
[input] array.integer arr
0 ≤ arr.length ≤ 20
[output] array.integer
'''


# Ot(n) Os(1)
def moveZerosToEnd(arr):
    if not arr:
        return []
    left = 0
    right = 0
    while right < len(arr) - 1:
        while arr[left] != 0:
            left += 1
            if left == len(arr):
                return arr
        right = left + 1
        while arr[right] == 0 and right + 1 < len(arr):
            right += 1
        arr[left], arr[right] = arr[right], arr[left]
        if arr[left] == 0:
            return arr
    return arr


def tests():
    arr = [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]
    expected = [1, 10, 2, 8, 3, 6, 4, 5, 7, 0, 0, 0, 0, 0]
    print(moveZerosToEnd(arr) == expected)
    arr = [1, 10, 0, 1, 0, 0, 0]
    expected = [1, 10, 1, 0, 0, 0, 0]
    print(moveZerosToEnd(arr) == expected)

    arr = [0, 0, 0, 0]
    expected = [0, 0, 0, 0]
    print(moveZerosToEnd(arr) == expected)

    arr = [1, 10, 2, 0, 0, 0, 8]
    expected = [1, 10, 2, 8, 0, 0, 0]
    print(moveZerosToEnd(arr) == expected)

    arr = [1,-1,2,4,6]
    expected = [1,-1,2,4,6]
    print(moveZerosToEnd(arr) == expected)


tests()
