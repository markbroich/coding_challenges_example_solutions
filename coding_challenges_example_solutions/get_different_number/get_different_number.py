'''
Getting a Different Number

Given an array arr of unique nonnegative integers, implement a function
getDifferentNumber that finds the smallest nonnegative integer that is NOT in
the array.
Even if your programming language of choice doesn’t have that restriction
(like Python), assume that the maximum value an integer can have is
MAX_INT = 2^31-1. So, for instance, the operation MAX_INT + 1 would be
undefined in our case.
Your algorithm should be efficient, both from a time and a space complexity
perspectives.
Solve first for the case when you’re NOT allowed to modify the input arr.
If successful and still have time, see if you can come up with an algorithm
with an improved space complexity when modifying arr is allowed. Do so without
trading off the time complexity.


input:  arr = [0, 1, 2, 3]
output: 4

Constraints:
[time limit] 5000ms
[input] array.integer arr

1 ≤ arr.length ≤ MAX_INT
0 ≤ arr[i] ≤ MAX_INT for every i, 0 ≤ i < MAX_INT
[output] integer
'''

# Ot(nlogn) Os(1)
def get_different_number_slow(arr):
    if not arr: 
        return -1
    # Ot(nlong) Os(1)
    arr.sort()
    for i in range(0, len(arr)):
        if i == 0 and arr[i] != 0:
            return 0
        if i > 0 and arr[i - 1] + 1 != arr[i]:
            return arr[i - 1] + 1
    return len(arr)

            
# Ot(n) Os(n)
def get_different_number(arr):
  my_set = set(arr)
  for i in range(len(arr)):
    if i not in my_set:
      return i
  return len(arr)


# Ot(n)
def get_different_number_n(arr):
    n = len(arr)
    for i in range(n):
        tmp = arr[i]
        while tmp < n and arr[tmp] != tmp:
            arr[tmp], arr[i] = arr[i], arr[tmp] 
    for i, v in enumerate(arr):
        if i != v:
            return i



def tests():
    arr = [0, 1, 2, 3]
    exp = 4
    print(get_different_number(arr) == exp)
    print(get_different_number_n(arr) == exp)
    arr = [0, 1, 3]
    exp = 2
    print(get_different_number(arr) == exp)
    print(get_different_number_n(arr) == exp)

    arr = [0, 1, 3]
    exp = 2
    print(get_different_number(arr) == exp)
    print(get_different_number_n(arr) == exp)

    arr = [0, 1, 2, 4]
    exp = 3
    print(get_different_number(arr) == exp)
    print(get_different_number_n(arr) == exp)

    arr = [0, 4, 1, 3]
    exp = 2
    print(get_different_number(arr) == exp)
    print(get_different_number_n(arr) == exp)
                      

tests()

