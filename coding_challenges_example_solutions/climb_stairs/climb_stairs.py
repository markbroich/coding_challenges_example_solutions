"""
This problem is commonly known as 'climb stairs'

There is a candy of n pieces (like a Toblerone bar).
You can bite off 1, 2, or 3 pieces.
Find the number of ways to eat the entire candy.
"""


'''
-similar to climbing stairs.
-order matters.
-no need to return permutations just the count.
-brute furth is a recuursion (so top down) where each leaf of the tree is a
situation where I finsihed the candy bar. So, the base case is
pieces left == 0 and I return 1.
If < 0 and I return 1, then the attempt failed and I return 0.
-I can arrrive at pieces left == 0 from up to 3 different situations
(where I just ate 1, 2 or 3 pieces) so at most 1 + 1 + 1 ways to take the
last bite.
Each of the starting points (-1, -2, -3 from end) in turn was reached in
up to 3 ways.


n = 1: 1 so 1
n = 2: 1+1, 2 so 2
n = 3: 1+1+1, 2+1, 1+2, 3 so 4
n = 4: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 3+1, 1+3 so 7
n = 5: 1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 2+2+1, 2+1+2, 1+2+2, 1+1+3, 1+3+1, 3+1+1, 2+3, 3+2 so 13
'''


# O(k^n) where k is lengh of bitesize. Space is used for stackmemory.
def ways2eat(n: int, bites: list) -> int:
    if not n or not bites:
        return -1

    def take_bite(leftover: int) -> int:
        if leftover < 0:
            return 0
        if leftover == 0:
            return 1
        return sum([take_bite(leftover - b) for b in bites])
    return take_bite(n)


# Ot(n) given no repeat in tree (e.g. leftover 3 = 3 is only calculated once).
# Os(k) k is proportional to permutartions which are stored in memo.
def ways2eat_memo(n: int, bites: list) -> int:
    if not n or not bites:
        return -1
    memo = {}

    def take_bite(leftover: int) -> int:
        if leftover not in memo:
            if leftover < 0:
                res = 0
            elif leftover == 0:
                res = 1
            else:
                res = sum(take_bite(leftover - b) for b in bites)
            memo[leftover] = res
        return memo[leftover]
    return take_bite(n)


'''
To reduce the memory footprint, I can drop from the memo once
parts are no longer needed. 
In the 'sum(take_bite(leftover - b) for b in bites)' part, the furthest
I look back is leftover - largest_bite + 1.
So, leftover - largest_bite is no longer needed.
So, the number of results in memo only need to be =
number of bites at a time since I can only arrive at a given place 3 ways
(-3, -2 and -1, if bites = [3,2,1]).
'''


# Ot(n) given no repeat in tree (e.g. leftover 3 = 3 is only calculated once).
# Os(s) s is xyz.
def ways2eat_recent_memo(n: int, bites: list) -> int:
    if not n or not bites:
        return -1
    # if there is nothing left, return 1
    memo = {0: 1}
    max_bite = max(bites)

    def take_bite(leftover: int) -> int:
        if leftover not in memo:
            if leftover < 0:
                res = 0
            else:
                res = sum(take_bite(leftover - b) for b in bites)
            memo[leftover] = res
            if leftover - max_bite in memo:
                del memo[leftover - max_bite] 
        return memo[leftover]
    return take_bite(n)


'''Bottom up: rather than working backwards from finishing the candy bar,
I can also build up the subsolutions from the beginning and track them in a table. 
How many ways are there to get to the:
1st piece: 1
2nd piece: 2
3rd piece: 4
I add them to the dp table.
When computing the 4th piece, I add up what exisits in the table:
dp[4-3] = 1
dp[4-2] = 2
dp[4-1] = 4
sums to 7
'''


# Ot(n * len(bites)) where bites is constant so Ot(n) Os(n)
def ways2eat_dp(n: int, bites: list) -> int:
    if not n or not bites:
      return -1
    # init dp for bites
    # Note: bites are fixed
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, n + 1):
        res = 0
        for b in bites:
            if i - b > 0:
              res += dp[i - b]
        dp[i] = res
    return dp[-1]


'''
dp using constant space
'''


# Ot(n) Os(1) Os is constant as I track 3 variables
def ways2eat_dp_contant_space(n: int, bites: list) -> int:
    if not n or not bites:
      return -1
    # init dp for bites
    # Note: bites are fixed
    dp = [0] * 4
    # 
    dp[-3] = 1
    dp[-2] = 2
    dp[-1] = 4
    for i in range(4, n + 1):
        res = 0
        for b in bites:
            if i - b > 0:
              res += dp[-b]
        for j in range(len(bites), 1, -1):
            dp[-j] = dp[-j + 1]
        dp[-1] = res
    return dp[-1]


def tests():
    bites = [1, 2, 3]
    n = 5
    exp = 13
    print(ways2eat(n, bites) == exp)
    print(ways2eat_memo(n, bites) == exp)
    print(ways2eat_recent_memo(n, bites) == exp)
    print(ways2eat_dp(n, bites) == exp)
    print(ways2eat_dp_contant_space(n, bites) == exp)


tests()


''' see also: https://leetcode.com/problems/climbing-stairs/solutions/1792723/python-in-depth-walkthrough-explanation-dp-top-down-bottom-up/'''
