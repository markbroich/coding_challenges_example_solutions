'''
K-Messed Array Sort

Given an array of integers arr where each element is at most k places away
from its sorted position, code an efficient function sortKMessedArray that
sorts arr. For instance, for an input array of size 10 and k = 2, an element
belonging to index 6 in the sorted array will be located at either index
4, 5, 6, 7 or 8 in the input array.

Analyze the time and space complexities of your solution.

Example:

input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2

output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Constraints:

[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ 100
[input] integer k

0 ≤ k ≤ 20
[output] array.integer

'''


#Ot(n * log(k))
#Os(k)

import heapq


def sort_k_messed_array(arr, k):
  li = arr[0:k+1]
  heapq.heapify(li)
  arr[0] = heapq.heappop(li)
  insIdx = 1
  for i in range(k+1, len(arr)):
      heapq.heappush(li,arr[i])
      arr[insIdx] = heapq.heappop(li)
      insIdx += 1

  while len(li) > 0:
    arr[insIdx] = heapq.heappop(li)
    insIdx += 1

  return arr



# Test Case #1
# Input: [1], 0,Expected: [1],Actual: [1]
# Test Case #2
# Input: [1,0], 1,Expected: [0,1],Actual: [0, 1]
# Test Case #3
# Input: [1,0,3,2], 1,Expected: [0,1,2,3],Actual: [0, 1, 2, 3]
# Test Case #4
# Input: [1,0,3,2,4,5,7,6,8], 1,Expected: [0,1,2,3,4,5,6,7,8],Actual: [0, 1, 2, 3, 4, 5, 6, 7, 8]
# Test Case #5
# Input: [1,4,5,2,3,7,8,6,10,9], 2,Expected: [1,2,3,4,5,6,7,8,9,10],Actual: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Test Case #6
# Input: [6,1,4,11,2,0,3,7,10,5,8,9], 6,Expected: [0,1,2,3,4,5,6,7,8,9,10,11],Actual: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]