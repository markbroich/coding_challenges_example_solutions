'''
Daily Temperatures

Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have
to wait after the ith day to get a warmer temperature. If there is no future
day for which this is possible, keep answer[i] == 0 instead.


Example 1:
temperatures = [73,74,75,71,69,72,76,73]
exp = [1,1,4,2,1,1,0,0]

Example 2:
temperatures = [30,40,50,60]
exp = [1,1,1,0]

Example 3:
temperatures = [30,60,90]
exp = [1,1,0]


Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''

from typing import List
from heapq import heappush, heappop


# Ot(n*n) Os(n)
def dailyTemperatures_brute_forth(temps: List[int]) -> List[int]:
    res = [0] * len(temps)
    for i in range(len(temps) - 1):
        for j in range(i + 1, len(temps)):
            if temps[j] > temps[i]:
                res[i] = j - i
                break
    return res


# Ot(n) Os(n + n + n)
def dailyTemperatures_stack(temps: List[int]) -> List[int]:
    res = [0] * len(temps)
    stack = [(temps[0], 0)]
    for i in range(1, len(temps)):
        while stack and temps[i] > stack[-1][0]:
            prior_t, j = stack.pop()
            res[j] = i - j
        stack.append((temps[i], i))
    return res


# The heap is not needed as the conentet of the
# stack will be in increasing order
# by the way dailyTemperatures_stack is written

# Ot(n log(n)) Os(n + n)
def dailyTemperatures_heap(temps: List[int]) -> List[int]:
    res = [0] * len(temps)
    heap = []

    for i in range(len(temps)):
        # Ot(log(n)) Os(n)
        heappush(heap, (temps[i], i))
        while temps[i] > heap[0][0]:
            # Ot(log(n)) Os(n)
            t, j = heappop(heap)
            res[j] = (i - j)
    return res


def tests():
    temperatures = [73,74,75,71,69,72,76,73]
    exp = [1,1,4,2,1,1,0,0]
    print(dailyTemperatures_brute_forth(temperatures) == exp)
    print(dailyTemperatures_stack(temperatures) == exp)
    print(dailyTemperatures_heap(temperatures) == exp)

    temperatures = [30,40,50,60]
    exp = [1,1,1,0]
    print(dailyTemperatures_brute_forth(temperatures) == exp)
    print(dailyTemperatures_stack(temperatures) == exp)
    print(dailyTemperatures_heap(temperatures) == exp)

    temperatures = [30,60,90]
    exp = [1,1,0]
    print(dailyTemperatures_brute_forth(temperatures) == exp)
    print(dailyTemperatures_stack(temperatures) == exp)
    print(dailyTemperatures_heap(temperatures) == exp)

    temperatures = [73,74,75,71,69,72,76,73]
    exp = [1,1,4,2,1,1,0,0]
    print(dailyTemperatures_brute_forth(temperatures) == exp)
    print(dailyTemperatures_stack(temperatures) == exp)
    print(dailyTemperatures_heap(temperatures) == exp)

    temperatures = [30,40,50,60]
    exp = [1,1,1,0]
    print(dailyTemperatures_brute_forth(temperatures) == exp)
    print(dailyTemperatures_stack(temperatures) == exp)
    print(dailyTemperatures_heap(temperatures) == exp)

    temperatures = [30,60,90]
    exp = [1,1,0]
    print(dailyTemperatures_brute_forth(temperatures) == exp)
    print(dailyTemperatures_stack(temperatures) == exp)
    print(dailyTemperatures_heap(temperatures) == exp)

    temperatures = [20,19,18,17,16,15,14,13,12,11,10,21]
    exp = [11,10,9,8,7,6,5,4,3,2,1,0]
    print(dailyTemperatures_brute_forth(temperatures) == exp)
    print(dailyTemperatures_stack(temperatures) == exp)
    print(dailyTemperatures_heap(temperatures) == exp)


tests()
