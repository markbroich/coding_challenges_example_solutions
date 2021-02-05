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
    if index < len(arr)-i -1:
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

