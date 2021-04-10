## Array of Array Products

# Given an array of integers arr, you’re asked to calculate for each index i the product of all integers except 
# the integer at that index (i.e. except arr[i]). Implement a function arrayOfArrayProducts that takes an array 
# of integers and returns an array of the products.

# Solve without using division and analyze your solution’s time and space complexities.

# Examples:
# input:  arr = [8, 10, 2]
# output: [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]

# input:  arr = [2, 7, 3, 4]
# output: [84, 24, 56, 42] # by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3


# Ot(n)
# Os(n)

def array_of_array_products(arr):
  if not arr or len(arr) == 1: 
    return []
  n = len(arr)
  # Base case
  if n == 1:
    print(0)
    return
  if n == 2:
    print(0)
    return arr
  i, temp = 1, 1
  # Allocate memory for the product array
  prod = [1 for i in range(n)]
  
  # Initialize the product array as 1
  # In this loop, temp variable contains product of
  # elements on left side excluding arr[i]
  for i in range(n):
    prod[i] = temp
    temp *= arr[i]
    # Initialize temp to 1 for product on right side
  temp = 1
  # In this loop, temp variable contains product of
  # elements on right side excluding arr[i]
  for i in range(n - 1, -1, -1):
    prod[i] *= temp
    temp *= arr[i]
  
  # Print the constructed prod array
  result = []
  for i in range(n):
    result.append(prod[i])
  return result
 
arr = [2,7,3,4] 
expected = [84, 24, 56, 42]
print(array_of_array_products(arr) == expected)

#

# why does this work? 
# manually computing the solution  
#     [2,   3,   4,  5]
# is  [60, 40, 30, 24] by calculating [3*4*5, 2*4*5, 2*3*5, 2*3*4].

# every index i is the product of all the values to the left of index i 
#  with all the values to the right of index i.

# e.g. 
# [2,       3,      4,     5]:
# prods to the left of index
# [1,       1*2,    1*2*3, 1*2*3*4] 
# and their complement prods, the right values, i.e. 
# [3*4*5*1, 4*5*1,  5*1,   1]. 



# It is the product of these two sequences, element by element, that gives 
# us the desired result.
# [60,      40,    30,    24]

# w inspiration from Pramp and geek for geeks. tnx :) 