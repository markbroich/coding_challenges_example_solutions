'''
Change in a Foreign Currency
You likely know that different currencies have coins and bills of different
denominations. In some currencies, it's actually impossible to receive change
for a given amount of money. For example, Canada has given up the 1-cent penny.
If you're owed 94 cents in Canada, a shopkeeper will graciously supply you with
95 cents instead since there exists a 5-cent coin.
Given a list of the available denominations, determine if it's possible to
receive exact change for an amount of money targetMoney. Both the denominations
and target amount will be given in generic units of that currency.

Signature

boolean canGetExactChange(int targetMoney, int[] denominations)

Input
1 ≤ |denominations| ≤ 100
1 ≤ denominations[i] ≤ 10,000
1 ≤ targetMoney ≤ 1,000,000

Output
Return true if it's possible to receive exactly targetMoney given the available
denominations, and false if not.

Example 1
denominations = [5, 10, 25, 100, 200]
targetMoney = 94
output = false
Every denomination is a multiple of 5, so you can't receive exactly 94 units
of money in this currency.

Example 2
denominations = [4, 17, 29]
targetMoney = 75
output = true
You can make 75 units with the denominations [17, 29, 29].
'''


# brute forth is:
# Ot(S^n) where S is the target amount and n is the numebr of different coins. 
# In worth case, every coin ci could be used at most S/ ci times.
# O​s(n) the max recusion depth.

# using memo (so, top down dynamic programming):
# Ot(S*n) Where S is the amount, n is number of different coins.
# In the worst case the recursive has height of
# S and the algorithm solves only S subproblems because
# it caches precalculated once in a memo.
# Each subproblem is computed with n iterations, one by coin size.
# Os(S) where S is the amount to change stored in memo.
def canGetExactChange(target, denomLst):
    memo = {}

    def rec(remain):
        if remain not in memo:
            if remain == 0:
                return True
            elif remain < 0:
                return False
            ret = False
            for d in denomLst:
                ret = ret or rec(remain - d)
            memo[remain] = ret
        return memo[remain]
    return rec(target)


denomLst = [4, 17, 29]
target = 75
output = True
print(canGetExactChange(target, denomLst) == output)

denomLst = [5, 10, 25, 100, 200]
target = 94
output = False
print(canGetExactChange(target, denomLst) == output)