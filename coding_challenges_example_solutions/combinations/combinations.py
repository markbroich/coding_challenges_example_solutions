"""Combinations

Given two integers n and k, return all possible combinations of k numbers
chosen from the range [1, n].
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to
be the same combination.

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

Constraints:
1 <= n <= 20
1 <= k <= n
"""


# O(n**k) n is max branching factor, k is level count
def combinations(n: int, k: int):
    res = []
    def rec(current, i):
        if len(current) == k:
          res.append(current)
          return
        for j in range(i, n + 1):
            rec(current + [j], j + 1)
        return
    rec([], 1)
    return res


n = 3
k = 2
print(combinations(n, k) == [[1, 2], [1, 3], [2, 3]])
n = 4
k = 2
print(combinations(n, k) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
n = 5
k = 3
print(combinations(n, k) == [[1,2,3], [1,2,4], [1,2,5], [1,3,4], [1,3,5], [1,4,5], [2,3,4], [2,3,5], [2,4,5], [3,4,5]]) 


def combinations(n: int, k: int):
    res = []
    stack = [([], 1)]
    while stack:
        current, i = stack.pop()
        for j in range(i, n + 1):
            if len(current) == k - 1:
                res.append(current + [j])
                continue
            stack.append((current + [j], j + 1))
    return res


print()
n = 3
k = 2
print(combinations(n, k) == [[2, 3], [1, 2], [1, 3]])
n = 4
k = 2
print(combinations(n, k) == [[3, 4], [2, 3], [2, 4], [1, 2], [1, 3], [1, 4]])
n = 5
k = 3
print(combinations(n, k) == [[3,4,5], [2,4,5], [2,3,4], [2,3,5], [1,4,5], [1,3,4], [1,3,5], [1,2,3], [1,2,4], [1,2,5]])


'''Below I add permutations.
In permutations the order matters: so 1,2 != 2,1.
So, the answer for n = 3, k = 2
is [[1, 2], [2, 1], [1, 3], [3, 1], [2, 3], [3, 2]])
'''


# O(n**k)
def permutations(n, k):
    res = []
    def rec(current, seen):
        if len(current) == k:
            res.append(current)
            return
        if not seen:
            seen = set()
        if current:
            seen.add(current[-1])
        for j in range(1, n + 1):
            if j not in seen:
                rec(current + [j], seen)
    rec([], None)
    return res

print()
n = 3
k = 2
print(permutations(n, k) == [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]])


def permutations(n, k):
    res = []
    stack = [[]]
    while stack:
        current = stack.pop()
        if len(current) == k:
            res.append(current)
            continue
        for i in range(1, n + 1):
            if i not in current:
                stack.append(current + [i])
    return res


n = 3
k = 2
print(permutations(n, k) == [[3, 2], [3, 1], [2, 3], [2, 1], [1, 3], [1, 2]])