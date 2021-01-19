# Pair Sums:

# Given a list of n integers arr[0..(n-1)], determine the number of 
# different pairs of elements within it which sum to k.
# If an integer appears in the list multiple times, each copy is 
# considered to be different; that is, two pairs are considered 
# different if one pair includes at least one array index which 
# the other doesn't, even if they include the same values.

# Input
# n is in the range [1, 100,000].
# Each value arr[i] is in the range [1, 1,000,000,000].
# k is in the range [1, 1,000,000,000].
# Output
# Return the number of different pairs of elements which sum to k.
# Example 1
# n = 5
# k = 6
# arr = [1, 2, 3, 4, 3]
# output = 2
# The valid pairs are 2+4 and 3+3.
# Example 2
# n = 5
# k = 6
# arr = [1, 5, 3, 3, 3]
# output = 4
# There's one valid pair 1+5, and three different valid pairs 3+3 
# (the 3rd and 4th elements, 3rd and 5th elements, and 4th and 5th elements).


import random
import math

# tests that verify that a function is working for different 
# test cases
def check(expected, output):
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()

def printInteger(n):
  print('[', n, ']', sep='', end='')

def numberOfWays_brute(arr, k):
    outputCounter = 0
    pairSet = set() 
    # brute forth
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] <= k and arr[j] <=k:
                if i != j and not (j,i) in pairSet:
                    if arr[i] + arr[j] == k:
                        outputCounter += 1
                        pairSet.add((i,j))
    return outputCounter

# optimized solution Ot(n), Os(n)
def numberOfWays_tOpt(arr, k):
    outputCounter = 0

    # populate occurrence count dict
    occCountDict = {}
    for i in range(len(arr)):
        if arr[i] in occCountDict:
            occCountDict[arr[i]] = occCountDict[arr[i]] + 1
        else:
            occCountDict[arr[i]] = 1

    # loop over occurrence count dict
    for i in occCountDict:
        if i > k:
            pass
        else:
            countA = occCountDict[i]
            j = k - i
            if i == j:
                # If k/2 appears w times, then you must add 
                # countA!/ ((countA-2)! * (2)!)valid pairs.
                # countA*(countA-1)/2 is == countA!/ ((countA-2)! * (2)!)
                # but much faster
                outputCounter += int(countA*(countA-1)/2)
            elif j in occCountDict: 
                countB = occCountDict[j]
                # multiply counts of i and j and / 2 to 
                # account for double counting of this approach
                # which occurs when we look at j and i
                # if countA or countB == 1 then the product is
                # == the larger count
                outputCounter += (countA * countB) / 2

    return outputCounter 




if __name__ == "__main__":
  test_case_number = 1
  k = 6
  arr = [1, 2, 3, 4, 3]
  expected = 2
  output = numberOfWays_brute(arr, k)
  check(expected, output)
  
  test_case_number = 2
  k = 6
  arr = [1, 5, 3, 3, 3]
  expected = 4
  output = numberOfWays_brute(arr, k)
  check(expected, output)
  
  test_case_number = 3
  k = 6
  arr = [3, 3, 3, 3]
  # permutation of ways of taking 2 out of n if order does not matters
  # (given that we indexValue1 + indexValue2 = k is the same as 
  # indexValue2 + indexValue1 = k)
  expected = int(math.factorial(len(arr))/ (math.factorial(len(arr)-2) * math.factorial(2)))
  output = numberOfWays_brute(arr, k)
  check(expected, output)
  
  test_case_number = 4
  # Will the function work when all pairs sum to k?
  # Imagine an array with 1000 copies of k/2. What should the answer be?
  n = 1000
  k = 6
  arr = [3]*n
  # permutation of ways of taking 2 out of n if order does not matters
  # (given that we indexValue1 + indexValue2 = k is the same as 
  # indexValue2 + indexValue1 = k)
  expected = int(math.factorial(len(arr))/ (math.factorial(len(arr)-2) * math.factorial(2)))
  output = numberOfWays_brute(arr, k)
  check(expected, output)

  test_case_number = 5
  # Make sure to test with values around the maximum possible input value (one billion).
  # try better algo with tiny sample
  k = 6
  arr = [1, 5, 3, 3, 3]
  expected = 4
  output = numberOfWays_tOpt(arr, k)
  check(expected, output)

  test_case_number = 6
  # try w large sample
  #n = 1.0e+09
  n = 1.0e+03
  k = 6
  arr = [3]*int(n)
  # permutation of ways of taking 2 out of n if order does not matters
  # (given that we indexValue1 + indexValue2 = k is the same as 
  # indexValue2 + indexValue1 = k)
  expected = int(math.factorial(len(arr))/ (math.factorial(len(arr)-2) * math.factorial(2)))
  output = numberOfWays_tOpt(arr, k)
  check(expected, output)
  
  test_case_number = 7
  n = 1.0e+09
  # rolling 7 with two dice
  # the chance is 1/6 as 6 of 36 possible outcomes of a role 
  # sum to 7
  k = 7
  arr = [random.randint(1,6) for i in range(int(n))]
  # number of combinations * 1/6 
  expected = math.factorial(len(arr))/ (math.factorial(len(arr)-2) * math.factorial(2)) * 1/6
  output = numberOfWays_tOpt(arr, k)
  check(expected, output)
  print('we do not expect a perfect result of 1/6 of all\
      possible combinations given that n is small so we will only\
      get ~ 1/6: ')
  expectedFrac = output/ int(math.factorial(len(arr))/ (math.factorial(len(arr)-2) * math.factorial(2)))
  print(expectedFrac)
  print('is close to 1/6 =', 1/6)
  print('expected frac - output frac: ', expectedFrac - 1/6)



# a few notes on combinartions and permutations
# equations 
# print()
# n = 100
# print('n = ', n)
# print('combinartions of ways 2 can be taken from n (order does not matters)')
# # print(int(n*(n-1)/2)) # or:
# print(int(math.factorial(n)/ (math.factorial(n-2) * math.factorial(2))))
# print('permutations of ways 2 can be taken from n (order matters)')
# print(int(math.factorial(n)/ (math.factorial(n-2))))
# print('combinartions of ways 2 can be taken from n (order does not matters, repetition allowed)')
# print(int(math.factorial(n+2-1)/ (math.factorial(n-2) * math.factorial(2))))
# print('permutations of ways 2 can be taken from n (order matters, repetition allowed)')
# print(n**2)



