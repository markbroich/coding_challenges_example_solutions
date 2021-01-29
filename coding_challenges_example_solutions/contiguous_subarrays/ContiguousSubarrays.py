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


