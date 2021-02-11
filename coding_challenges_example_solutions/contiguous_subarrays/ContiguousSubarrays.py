# Contiguous Subarrays

# You are given an array arr of N integers. For each index i, you are required to determine the 
# 'number' of contiguous subarrays that fulfills the following conditions:

# The value at index i must be the maximum element in the contiguous subarrays, and
# These contiguous subarrays must either start from or end on index i.


# Input
# Array arr is a non-empty list of unique integers that range between 1 to 1,000,000,000
# Size N is between 1 and 1,000,000

# Output
# An array where each index i contains an integer denoting the maximum number of contiguous subarrays of arr[i]
# Example:
# arr = [3, 4, 1, 6, 2]
# output = [1, 3, 1, 5, 1]
# Explanation:
# For index 0 - [3] is the only contiguous subarray that starts (or ends) with 3, and the maximum value in this subarray is 3.
# For index 1 - [4], [3, 4], [4, 1]
# For index 2 - [1]
# For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
# For index 4 - [2]
# So, the answer for the above input is [1, 3, 1, 5, 1]

# brute_forth
# O(n*n*2)
# lots of repeated work

def count_subarrays_brute_forth(arr):
    output = ['']*len(arr)
    for i in range(len(arr)):
        counter = 1
        current = arr[i]
        #go left
        for j in range(i-1,-1,-1):
            #if neighbor is higher: stop
            if arr[j] > current:
                break
            else: 
                counter +=1 
        #go right
        for j in range(i+1, len(arr)):
            #if neighbor is higher: stop
            if arr[j] > current:
                break
            else: 
                counter +=1 
        output[i] = counter 
    return output


# Hints:
#
# Complexity
# Any solution must have time and space complexities of at 
# least O(N) to deal with the array of N integers. 
# A relatively simple solution considering all possible 
# contiguous subarrays, or in fact any solution counting 
# the valid subarrays one-by-one, would require a time 
# complexity of at least O(N^2). 
# However, a number of observations can allow this to be 
# optimized down to the ideal time complexity of O(N). 
# For example, letting L[i] be the number of valid subarrays 
# ending at index i (useful to compute on the way to the final 
# answer), consider how we might efficiently compute L[i] 
# for each i from 1 to N by reusing past information rather 
# than computing it from scratch.
# When analyzing such a solution, note that even if we’re 
# computing N values L[1..N], and computing any single one 
# of those values might take on the order of N steps, the 
# overall time complexity will not necessarily be O(N^2) - 
# we should instead consider how many steps may occur in 
# total across all N of them in the worst case.

# Solution approach
# Letting L[i] be the number of valid subarrays ending at 
# index i and R[i] be the number of valid subarrays beginning 
# at index i, we’ll have output[i] = L[i] + R[i] - 1. 
# Computing R[1..N] is equivalent to computing L[1..N] 
# if a were reversed, allowing us to reduce the problem 
# to computing L[1..N] for an array of N distinct integers.
# We can next observe that the index of the latest element 
# to the left of the ith element which is larger than it 
# determines which subarrays ending at index i are valid 
# - specifically, the ones beginning to the right of that 
# larger element. Letting G[i] be equal to the largest 
# index j such that j < i and a[j] > a[i] (or equal to 0 
# if there’s no such j), then L[i] = i - G[i]. We’ve now 
# reduced the problem to computing these values G[1..N] 
# for an array of N distinct integers.
# Computing G[i] for each i from 1 to N is a promising 
# approach, but we’ll still need to consider how to do 
# so as efficiently as possible. We can observe that 
# it’s not possible to compute G[i] purely based on 
# the values of G[i-1], a[i-1], and a[i]; we may need 
# more information about earlier a values as well, but 
# would like to avoid simply scanning over all of them. 
# Out of earlier indices j (such that j < i), we can 
# consider which indices are worth considering as potential 
# candidates for G[i] - for example, if there exists a 
# pair of indices j and k such that j < k and a[j] < a[k], 
# can index j ever be a candidate for G[i] for any i > k? 
# If we can maintain information about the set of these 
# possible candidate indices as we go through the array, 
# it’s possible to efficiently determine the one that’s 
# actually equal to G[i] for each i.


# O(n) using a stack an 3 subsequent loops over arr

## Stack w tuple of (value, pick up index)
# stack will pick up every value and 'pick up index' as 
# I go over arr. 
# When a higher value is encountered, 
# I will pop from stack and write 
# delta between current index and 'pick up index' to the result
# array at 'pick up index' 

# e.g. L to R pass
# arr  = [3, 4, 1, 6, 2]

# going from right to left (only):
# initial stack: 
# stack[(3,0)]
# for i in range(1, len(arr)):
# at index = 1, write 1 - 0 to res[0]
# res[1,'','','','']
# stack[(4,1)]
# at index = 2, continue
# stack[(4,1), (1,2)]
# at index = 3, write 3 - 2 to res[2] and
# write 3 - 1 to res[1]
# res[1,2,1,'','']
# stack[(6,3)]
# at index = 4, continue
# stack[(6,3), (2,4)]
# unload stack: write 5 - 4 to res[4] and 
# write 5 - 3 to res[3] and 
# res[1,2,1,2,1]

def contiguous_subarrays_stack(arr):
  n = len(arr)
  resL = ['']*n
  resR = ['']*n
  res = ['']*n

  # init stack for R-L pass
  stack = [(arr[0],0)]
  # do R-L pass
  for i in range(1,n):
    while stack and stack[-1][0] < arr[i]:
      toInsert = stack.pop(-1)
      resL[toInsert[1]] = i - toInsert[1]
    stack.append((arr[i],i))
  # empty stack
  while stack:
    toInsert = stack.pop(-1)
    resL[toInsert[1]] = n - toInsert[1]
  
  # init stack for L-R pass
  stack = [(arr[n-1],n-1)]
  # do L-R pass
  for i in range(n-2,-1 ,-1):
    while stack and stack[-1][0] < arr[i]:
      toInsert = stack.pop(-1)
      resR[toInsert[1]] = toInsert[1] - i
    stack.append((arr[i],i))
  # empty stack  
  while stack:
    toInsert = stack.pop(-1)
    resR[toInsert[1]] = toInsert[1] + 1
  # combine passes
  for i in range(0,n):
    res[i] = resL[i] + resR[i] -1 # minus one to account for double counting
  return res


# contiguous_subarrays_stack w inspiration from: https://leetcode.com/discuss/interview-question/579606/count-contiguous-subarrays



#####################
# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  test_1 = [3, 4, 1, 6, 2]
  expected_1 = [1, 3, 1, 5, 1]
  print('count_subarrays_brute_forth')
  output_1 = count_subarrays_brute_forth(test_1)
  check(expected_1, output_1)
  
  print('contiguous_subarrays_stack')
  output_1 = contiguous_subarrays_stack(test_1)
  check(expected_1, output_1)

  test_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [1, 2, 6, 1, 3, 1]
  print('count_subarrays_brute_forth')
  output_2 = count_subarrays_brute_forth(test_2)
  check(expected_2, output_2)
  
  print('contiguous_subarrays_stack')
  output_2 = contiguous_subarrays_stack(test_2)
  check(expected_2, output_2)

  # Add your own test cases here


