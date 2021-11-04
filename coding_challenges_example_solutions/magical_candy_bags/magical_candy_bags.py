'''
Magical Candy Bags

You have N bags of candy. The ith bag contains arr[i] pieces of candy, and each
of the bags is magical!
It takes you 1 minute to eat all of the pieces of candy in a bag (irrespective
of how many pieces of candy are inside), and as soon as you finish, the bag
mysteriously refills. If there were x pieces of candy in the bag at the
beginning of the minute, then after you've finished you'll
find that floor(x/2) pieces are now inside.
You have k minutes to eat as much candy as possible. How many pieces of candy
can you eat?

Signature
int maxCandies(int[] arr, int K)

Input
1 ≤ N ≤ 10,000
1 ≤ k ≤ 10,000
1 ≤ arr[i] ≤ 1,000,000,000

Output
A single integer, the maximum number of candies you can eat in k minutes.

Example 1
N = 5
k = 3
arr = [2, 1, 7, 4, 2]
output = 14
In the first minute you can eat 7 pieces of candy. That bag will refill with
floor(7/2) = 3 pieces.
In the second minute you can eat 4 pieces of candy from another bag. That bag
will refill with floor(4/2) = 2 pieces.
In the third minute you can eat the 3 pieces of candy that have appeared in
the first bag that you ate.
In total you can eat 7 + 4 + 3 = 14 pieces of candy.
'''

import heapq

# brute forth would be to scan the array to find the min after each iteration
# so Ot(n * k) or n^2 so at max 100,000,000

# Ot(n + n + k * log(n))
# at max 10000 + 10000 + 92103 [the k * log(n)] so ~110,000
# Os(n)
def maxCandies(arr, k):
    # Ot(n)
    for i in range(0, len(arr)):
        # needs to be negative so that max element is on top of heap
        arr[i] = -arr[i]
    # Ot(n), Os(n) gussign that this is not in place
    heapq.heapify(arr)

    # # Ot(n)
    # # Os(n) as arr is overwritten
    # myHeap = []
    # heapq.heapify(myHeap)
    # # Ot(n log(n)) 
    # [heapq.heappush(myHeap, -i) for i in arr]

    candyCnt = 0
    while k:
        # Ot(log(n))
        x = heapq.heappop(arr)
        # x is negative so -= -10 is candyCnt +10
        candyCnt -= x
        # Ot(log(n))
        heapq.heappush(arr, int(x / 2))
        k -= 1
    return candyCnt


k = 3
arr = [2, 1, 7, 4, 2]
expected = 14
print(expected == maxCandies(arr, k))

k = 3
arr = [2, 1, 7, 4, 2]
expected = 14
print(expected == maxCandies(arr, k))

k = 3
arr = [19, 78, 76, 72, 48, 8, 24, 74, 29]
expected = 228
print(expected == maxCandies(arr, k))


# simulation
import random

# 1 ≤ N ≤ 10,000
# 1 ≤ k ≤ 10,000
# 1 ≤ arr[i] ≤ 1,000,000,000

k = random.randint(1, 10000)
n = random.randint(1, 10000)
arr = [''] * n
for i in range(0, n):
    arr[i] = random.randint(1, 1000000000)

print(maxCandies(arr, k))