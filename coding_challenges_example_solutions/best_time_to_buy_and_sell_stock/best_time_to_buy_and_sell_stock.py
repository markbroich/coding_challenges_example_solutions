'''Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
'''


# Ot(n) Os(1)
def max_stock_profit(prices: list):
    max_diff = float('-inf')
    min_val = prices[0]
    for i in range(1, len(prices)):
        if min_val > prices[i]:
            min_val = prices[i]
        else:
            max_diff = max(max_diff, prices[i] - min_val)
    if max_diff > 0:
        return max_diff
    return 0


def tests():
    prices = [7,3,10,1,4,6,4]
    print(max_stock_profit(prices) == 7)

    prices = [7,1,5,3,6,4]
    print(max_stock_profit(prices) == 5)

    prices = [7,6,4,3,1]
    print(max_stock_profit(prices) == 0)


tests()
