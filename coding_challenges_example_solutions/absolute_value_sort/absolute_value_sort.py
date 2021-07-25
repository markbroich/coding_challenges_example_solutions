'''
Absolute Value Sort

Given an array of integers arr, write a function absSort(arr), 
that sorts the array according to the absolute values of the 
numbers in arr. If two numbers have the same absolute value, 
sort them according to sign, where the negative numbers come 
before the positive numbers.

Examples:

input:  arr = [2, -7, -2, -2, 0]
output: [0, -2, -2, 2, -7] 
'''


# Ot(nlogn)
# Os(1)
from functools import cmp_to_key


def myFunc(a, b):
  if abs(a) == abs(b):
    if a < b:
      return -1
    else:
      return 1  
  else: 
    if abs(a) < abs(b):
      return -1
    else:
      return 1


def absSort(arr):
    # https://www.geeksforgeeks.org/how-does-the-functools-cmp_to_key-function-works-in-python/
    arr.sort(key=cmp_to_key(myFunc))
    return arr


def testing():
    arr = [2, -7, -2, -2, 0]
    exp = [0, -2, -2, 2, -7]
    print(absSort(arr) == exp)

    arr = [-2,1]
    exp = [1,-2]
    print(absSort(arr) == exp)

    arr = [0,1,2]
    exp = [0,1,2]
    print(absSort(arr) == exp)

    arr = [2,-1,-1,-1]
    exp = [-1,-1,-1,2]
    print(absSort(arr) == exp)

    arr = [-2,3,5,-1,4]
    exp = [-1,-2,3,4,5]
    print(absSort(arr) == exp)

    arr = [4,-1,6,-4,2,-1]
    exp = [-1,-1,2,-4,4,6]
    print(absSort(arr) == exp)

    arr = [6,4,-5,0,-1,7,0]
    exp = [0,0,-1,4,-5,6,7]
    print(absSort(arr) == exp)

    arr = [-7,-2,-2,6,5,-6,-2,-6]
    exp = [-2,-2,-2,5,-6,-6,6,-7]
    print(absSort(arr) == exp)

    arr = [-4,9,-1,1,-1,2,-8,-6,3]
    exp = [-1,-1,1,2,3,-4,-6,-8,9]
    print(absSort(arr) == exp)

# run testing
testing()
