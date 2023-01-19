'''
0–1 Knapsack Problem

In the 0–1 Knapsack problem, we are given a set of items, each with
a weight and a value, and we need to determine the number of each
item to include in a collection so that the total weight is less
than or equal to a given limit and the total value is as large as possible.

Please note that the items are indivisible; we can either take an
item or not (0-1 property). For example,

Input:
values = [20, 5, 10, 40, 15, 25]
weight = [1, 2, 3, 8, 7, 4]
w = 10
 
Output: Knapsack value is 60
 
value = 20 + 40 = 60
weight = 1 + 8 = 9 < W

Is used in praxis e.g. to decide with combiantions of programs to run first if
compute capacity if limited or which parcels go on the first delivery truck if
high value parcels need to be delivered sooner than low value parcels.
'''


# O(2**n)
def knapsack(values: list, weights: list, max_w: int) -> int:
    if not values and not weights:
        return -1

    def recure(i: int, v: int, w: int) -> int:
        if w > max_w:
            return float('-inf')
        elif i >= len(values):
            return v
        return max(recure(i + 1, v + values[i], w + weights[i]),
                   recure(i + 1, v, w))

    return recure(0, 0, 0)


# O(n * max_w) where n is the length of values
def knapsack_memo(values: list, weights: list, max_w: int) -> int:
    if not values and not weights:
        return -1
    memo = {}

    def recure(i: int, v: int, w: int) -> int:
        if (i, w) not in memo:
            if w > max_w:
                return float('-inf')
            elif i >= len(values):
                return v
            memo[(i, w)] = max(recure(i + 1, v + values[i], w + weights[i]),
                               recure(i + 1, v, w))
        return memo[(i, w)]
    return recure(0, 0, 0)


# O(n * max_w) where n is the length of values
def knapsack_table(values: list, weights: list, max_w: int) -> int:
    table = [[0 for j in range(max_w + 1)] for i in range(len(values) + 1)]
    for i in range(1, len(values) + 1):
        for w in range(max_w + 1):
            # if w < weights[i - 1]:
            #     continue
            if weights[i - 1] > w:
                # if current weight can not fit
                table[i][w] = table[i - 1][w]
            else:
                '''How can we get maximum value if knapsack size w,
                then compute maximum value if knapsack size is w+1
                and so on… to max_w
                '''
                # look up value 'at' capacity minus current weight
                # and add current value.
                table[i][w] =\
                    max(table[i - 1][w],
                        table[i - 1][w - weights[i - 1]] + values[i - 1])
    return table[-1][-1]


def testing():
    values = [20, 5, 10, 40, 15, 25]
    weights = [1, 2, 3, 8, 7, 4]
    max_w = 10
    exp = 60
    print(knapsack(values, weights, max_w) == exp)
    print(knapsack_memo(values, weights, max_w) == exp)
    print(knapsack_table(values, weights, max_w) == exp)

    values = [20, 5, 10, 40, 15, 25]
    weights = [9, 2, 1, 3, 7, 4]
    max_w = 10
    exp = 80
    print(knapsack(values, weights, max_w) == exp)
    print(knapsack_memo(values, weights, max_w) == exp)
    print(knapsack_table(values, weights, max_w) == exp)

    values = [20, 50, 5, 10, 15, 40]
    weights = [9, 0, 0, 0, 1, 1]
    max_w = 10
    exp = 125
    print(knapsack_memo(values, weights, max_w) == exp)
    print(knapsack_table(values, weights, max_w) == exp)


testing()
