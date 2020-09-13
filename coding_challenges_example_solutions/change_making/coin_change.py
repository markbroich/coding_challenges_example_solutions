# Coin change challenge

# write an algo to return the min number of coins for a given change amount and coin set
# We assume an infintie supply of coins to make the change


# greedy approach that returns the maximum coin at every step. 
# the greedy solution is fast and locally optimal but it may compromise the global solution
# e.g. it may not find the globally optimal solution (min number of coins) or it may not find any solution
# see examples below  

def greedy_change(change, coins):
    coin_count = 0
    chosen_coins = []

    pointer = len(coins)-1
    while change > 0 and pointer >=0:
        if change - coins[pointer] >=0:
            chosen_coins.append(coins[pointer])
            change = change - coins[pointer]
            coin_count += 1
        else:
            pointer -= 1
    #
    print('coin_count ', coin_count)
    print('chosen_coins ', chosen_coins)
    if(change > 0):
        print('change remaining: ', change, "\n")

# this work nicely with a greedy algo
coins = [1, 2, 5, 10, 25]
change = 32
print("coins: ", coins," change: ", change)
greedy_change(change, coins)
print("")

# a greedy algo will not return all change here (hence not find a solution)
coins = [4, 10, 25]
change = 41
print('can we solve this? ')
print("coins: ", coins," change: ", change)
greedy_change(change, coins)

# a greedy algo will return more coins than a human would ( 3x10 + 2x2 so 5 coins) 
#  greedy algo would return 1x25 7 x1 so 8 coins (hence the locally optimal solution at every step but a globally poor solution)
coins = [1, 10, 25]
change = 32
print("coins: ", coins," change: ", change)
greedy_change(change, coins)
print("=> nmore than necessary coins are given as change\n\n")


# this brute_force algo find the optical solution if there is one 
# it uses 3 nested loops and is currently hard coded to 3 unique coin values
# O(change/coin1_value  * change/coin2_value * change/coin3_value), which can be quite large
def changemaker_brute_force(change, coins):
    change_combos = 0
    combos = []

    max_coins_1 = int(change/coins[0])
    max_coins_2 = int(change/coins[1])
    max_coins_10 = int(change/coins[2])

    # set up for 3 types of coins only
    for i in range(0,max_coins_1+1): 
        for j in range(0,max_coins_2+1): 
            for k in range(0,max_coins_10+1): 
                if(i*coins[0] + j*coins[1] + k*coins[2] == change):
                    change_combos += 1
                    combos.append([ (str(i)+"x"+str(coins[0])),(str(j)+"x"+str(coins[1])),(str(k)+"x"+str(coins[2]))])
    if change_combos > 0:
        print('change_combos: ', change_combos)
        print('combos: ', combos)
    else:
        print('no possible combination')


change = 41
coins = [4, 10, 25]
print('can we solve this? ')
print("coins: ", coins," change: ", change)
changemaker_brute_force(change, coins)
print("")

change = 16
coins = [1, 7, 10]
print("coins: ", coins," change: ", change)
changemaker_brute_force(change, coins)
print("")


# as above but works for any number of different coins using itertools.product
def brute_change(change, coins):
    import itertools

    len_c = len(coins)
    coin_count = 99999
    ranges = []
    max_loop = [0]*len_c

    for i in range(0, len_c):
        max_loop[i] = int(change/coins[i])
        ranges.append(range(0, max_loop[i]+1))

    for xs in itertools.product(*ranges):
        cur_sum = 0
        cur_count = 0
        for i in range(0, len_c):
            cur_sum = cur_sum + xs[i]*coins[i]
            cur_count = cur_count + xs[i]
        if cur_sum == change and coin_count > cur_count:
                coin_count = cur_count

    if coin_count == 99999:
        return 'no solution found'
    return coin_count

print('testing brute change')
change = 41
coins = [4, 10, 25]
print('can we solve this? ')
print("coins: ", coins," change: ", change)
print('returning ',brute_change(change, coins), ' coins')
print("")

change = 16
coins = [1, 7, 10]
print("coins: ", coins," change: ", change)
print('returning ',brute_change(change, coins), ' coins')
print("")

# Dynamic programming algo 'that works for any coin set and change amount':
# O(i x j) time where i is the change (e.g. 32c) and j is the number of different coin sizes
# O(i) space 

# the approach is to solve subproblems, tabulate their solutions (bottom up) and reuse these solutions in larger problems.
# e.g. if we have already determined that the optimal coincount to make change for 9c (based on 1c and 7c coins) is 3 coins (2x1c + 1x7c)
# then when looking for the optimal coincount for 19c change, we can consider a 10c coin (subtract 1x10c coin from 16c) and 'look up' 
# the min number of coins we need to provide 9c of change 19c - 1x10 = 9 so one 10c coin + 3 coins (2x1c + 1x7c) = 4 coins . 

def minimum_coins_to_make_change(change, coins):
    # initialize arrays for 'min coin count to make change amount'
    min_coin_count = [10000]*(change+1)
    # needs to start with zero for 'min_coin_count[i - j] + 1' 
    # to work as for amount 1 - coinvalue 1 = 0 so at index 0 we need to find zero for 0+1 = 1
    min_coin_count[0] = 0

    # after each i (each populated i slot) will have the min coin count. 
    for i in range(1, change + 1): 
        for j in coins:
            if i - j > -1: # if current_amount - coin >= 0 (so if coin <= current_amount)
                # use the small of: prior min_coin_count for change or count at index [change - current_coin] + 1 
                # which is the current coin + the min coin count that made up the remainder
                min_coin_count[i] = min(min_coin_count[i], min_coin_count[i - j] + 1)
    return min_coin_count[change]

print("minimum_coins_to_make_change: ")
coins = [1, 7, 10]
change = 16
print(minimum_coins_to_make_change(change, coins))


def minimum_coins_and_combo_to_make_change(change, coins):
    # initialize arrays for 'min coin count to make change amount and coins_composition'
    min_coin_count = [0]*(change+1)
    coins_composition = [[]]*(change+1) # list in lists

    for i in range(1, change + 1):
        best = 10000
        best_coins_composition = None

        for j in coins:
            if i - j > -1 and min_coin_count[i - j] + 1 < best:
                best = min_coin_count[i - j] + 1
                best_coins_composition = coins_composition[i - j] + [j]

        min_coin_count[i] = best
        coins_composition[i] = best_coins_composition
    return i, best, best_coins_composition


coins = [1, 7, 10]
change = 16
print("minimum_coins_and_combo_to_make_change: ")
print(minimum_coins_and_combo_to_make_change(change, coins))
print ("so 7x2 + 1x2 = 4 coins not 10x1 + 1x6 = 7 coins as w greedy\n")


change = 41
coins = [4, 10, 25]
print("minimum_coins_and_combo_to_make_change: ")
print(minimum_coins_and_combo_to_make_change(change, coins))


# dynamic algo w inspiration from: https://www.koderdojo.com/blog/algorithm-to-make-change-in-python-dynamic-programming


# the time complexity of the dynamic programing algo is: 
# O(changeamout x different_coins) is << determining the combination of coins that forms the minimum coin 
# count for every change amount: 


def loop_count_brute_force_vs_dynamic(change, coins):
    count_combos = 1
    for i in range(0, len(coins)):
        count_combos = count_combos * (int(change/coins[i]) + 1)

    print('count combos to eval calculation: ', count_combos)
    print("loops in dynamic approach: ", change*len(coins))
    print('dynamic algo is ', round(count_combos / change*len(coins)), ' times faster\n')


change = 41
coins = [4, 10, 25]
print("coins: ", coins," change: ", change)
loop_count_brute_force_vs_dynamic(change, coins)

change = 16
coins = [1, 7, 10]
print("coins: ", coins," change: ", change)
loop_count_brute_force_vs_dynamic(change, coins)

change = 150
coins = [1, 7, 10]
print("coins: ", coins," change: ", change)
loop_count_brute_force_vs_dynamic(change, coins)

