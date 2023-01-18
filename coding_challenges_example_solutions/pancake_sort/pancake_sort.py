# Pancake Sort

# Given an array of integers arr:

# Write a function flip(arr, k) that reverses the order of the first k elements in the array arr.
# Write a function pancakeSort(arr) that sorts and returns the input array. You are allowed to use only the function flip you wrote in the 
# first step in order to make changes in the array.
# Example:

# input:  arr = [1, 5, 4, 3, 2]

# output: [1, 2, 3, 4, 5] # to clarify, this is pancakeSort's output
# Analyze the time and space complexities of your solution.

# Note: it’s called pancake sort because it resembles sorting pancakes on a plate with a spatula, 
# where you can only use the spatula to flip some of the top pancakes in the plate. 
# To read more about the problem, see the Pancake Sorting Wikipedia page.

# Constraints:

# [input] array.integer arr
# [input] integer k
# 0 ≤ k
# [output] array.integer




# the aim is to sort with the least number of array reversales (flips)
# see graphic: https://cdn-images-1.medium.com/max/1600/1*Le34glwWrk1CIDbVG23LKA.png

# the Steps:
# the index of the larget item is found
# items 0 to indexOfLargest are flipped (reversed) which brings the largest item to the front
# the entire arr is then flipped again, which brings the largest item to the end
# the process is repeated for the subset excluding the last item which is already 
# in the right place.

# So: 
# for i in 0 to len(arr)-1:
# find index of largest in arr[0:len(arr)-i]
# flip arr[0: index of largest]
# flip arr arr[0:len(arr)-i]

# Ot(n^2) (actually n*(n+n+n) so n^2)
# Os(1) aka in place


def pancake_sort(arr):
    for i in range(len(arr)):
        # find_index_largest in length - i 
        index = find_index_largest(arr[0:len(arr)-i])
        # if index is not the last within 0 to length - i
        if index < len(arr)-i - 1:
            # flip 0 to index
            arr[0:index+1] = rev_arr(arr[0:index+1])
            # flip 0 to len(arr)-i
            arr[0:len(arr)-i] = rev_arr(arr[0:len(arr)-i])
    return arr


def find_index_largest(arr):
    index = ''
    largest = -99999
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            index = i
    return index


def rev_arr(arr): # aka flip
    for i in range(int(len(arr)/2)):
        temp = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = arr[i]
        arr[i] = temp
    return arr


arr = [1, 5, 4, 3, 2]
print(arr)
# print(rev_arr(arr))
print(pancake_sort(arr))



# another implementation


# O(n)
def find_largest(arr):
    max = -999
    iMax = 0
    for i in range(0,len(arr)):
        if arr[i] > max:
            max = arr[i]
            iMax = i
    return iMax


# O(n)
def flip(arr):
    mid  = int(len(arr)/2)
    for i in range(0, mid):
        temp = arr[i]
        arr[i] = arr[-1-i]
        arr[-1-i] = temp
    return arr


# loops n times so, Ot(n*(n+n)) so n^2, Os(1)
def pancake_sort(arr):
    if not arr:
        return -1

    indexLargest = len(arr)
    for indexSorted in range(len(arr),1,-1):
        # find largest (above sorted)
        indexLargest = find_largest(arr[:indexSorted])
        # flip 0 to largest
        arr[:indexLargest+1] = flip(arr[:indexLargest+1])
        # flip 0 to above sorted
        arr[:indexSorted] = flip(arr[:indexSorted])
    return arr


arr = [1,5,4,3,2]
output = [1,2,3,4,5] 
print(pancake_sort(arr) == output)
print(pancake_sort(arr))


## another implementation using recursion and in build methods

# O(n) using in builds
def flip(arr, k):
    if k == 0:
        return arr    
    return list(reversed(arr[:k])) + arr[k:]

# using recursion Ot(n^2) Os(n) in stack memory
def pancake_sort(arr):  
    n = len(arr)

    if n == 0:
      return []

    m = max(arr)
    m_index = arr.index(m)
    arr = flip(arr, m_index+1)
    arr = flip(arr, n)  # now maximal element is at the end
    return pancake_sort(arr[:n-1]) + [arr[-1]]
  




############# Redone


# Ot(n*(n+n+n)) so Ot(n*n) Os(n) were n is len of arr
def pancake_sort(arr: list) -> list:
    if len(arr) == 0 or len(arr) == 1:
        return arr
    # loop backwards with end being the index
    for end in range(len(arr), 0, -1):
        # find largest (0: end) and flip.
        # Ot(n) Os(1)
        maxx = max(arr[:end])
        # Ot(n) Os(1)
        index_of_largest = arr.index(maxx)
        # Ot(n) Os(1)
        arr = flip_Os1(arr, 0, index_of_largest)
        # then flip all
        # Ot(n) Os(1)
        arr = flip_Os1_concise(arr, 0, end)
    return arr


# Ot(n) Os(1) where n is 0 to end (proportional to lenght or arr)
def find_index_of_largest_before_end(arr: list, end):
    largest = float('-inf')
    index_of_largest = 0
    for i in range(0, end):
        if arr[i] > largest:
            largest = arr[i]
            index_of_largest = i
    return index_of_largest


# Ot(n) Os(1)
def flip_Os1(arr, left, right):
    left = 0
    while left < right:
        tmp = arr[left]
        arr[left], arr[right] = arr[right], tmp
        left += 1
        right -= 1
    return arr


# # O(n) where n is the difference between i and j
def flip_Os1_concise(arr: list, left: int, right: int) -> list:
    arr[left:right] = arr[left:right][::-1]
    return arr


def tests():
    arr = [1]
    exp = [1]
    print(pancake_sort(arr) == exp)

    arr = [1,2]
    exp = [1,2]
    print(pancake_sort(arr) == exp)

    arr = [1,3,1]
    exp = [1,1,3]
    print(pancake_sort(arr) == exp)

    arr = [3,1,2,4,6,5]
    exp = [1,2,3,4,5,6]
    print(pancake_sort(arr) == exp)

    arr = [10,9,8,7,6,5,4,3,2,1]
    exp = [1,2,3,4,5,6,7,8,9,10]
    print(pancake_sort(arr) == exp)

    arr = [10,9,8,6,7,5,4,3,2,1,9,10,8,7,6,5,4,3,2,1,10,9,8,7,6,5,4,3,2,1]
    exp = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10]
    print(pancake_sort(arr) == exp)


tests()

'''
Example how it is done:
# loop backwards with end being the index
[1, 5, 4, 3, 2]
# find largest (0: end) and flip.
[5, 1, 4, 3, 2]
# then flip all
[2, 3, 4, 1, 5]
# find largest (0: end) and flip.
[4, 3, 2, 1, 5]
# then flip all
[1, 2, 3, 4, 5]
# find largest (0: end) and flip.


[2, 5, 1, 4, 3]
'''
