## Jump game

# Task: 
# Given an array of non-negative integers, A, you are initially 
# positioned at the first index of the array.
# Each element in the array represents your maximum 
# jump length at that position.
# -Determine if you are able to reach the last index.

# Input Format:
# The first and the only argument of input will be an integer array A.
# 
# Output Format:
# Return an integer, representing the answer as described in the problem statement.
#     => -1 : If you cannot reach the last index.
#     => 1 : If you can reach the last index.
# This is the TRUE FALSE version

# Examples:
# Input 1:
#     A = [2,3,1,1,4]
# Output 1:
#     1
# Explanation 1:
#     Index 0 -> Index 2 -> Index 3 -> Index 4 -> Index 5

# Input 2:
#     A = [3,2,1,0,4]
# Output 2:
#     0
# Explanation 2:
#     There is no possible path to reach the last index.

# The second version of the challenge involves returning the number of jumps 
# required to reach the end or a -1 or -999 value if the end can not be 
# reached
# This is the JUMP COUNT version


# O(2^n)run time of brute forth becomes obvious when 
# considering this example:
# A = [10,1,1,1,1,1,1,1,1,0,1,99]
# for i=0 i+A[i] >= len(A)-1 is false so 
# and we may only take a jump of 10 after having 
# traveled most of the array 9 times. 


# TRUE FALSE 
# sr = simple recurssion 
# O(2^n) given that there are n possible jumps 
# from the first element
def jump_to_end_sr(A, i=0):
    if A[0] == 0:
        return 0  
    if i+A[i] >= len(A)-1:
        return 1
    for j in range(1,A[i]+1):
        if jump_to_end_sr(A, i+j) == 1:
            return 1
    return -1
#
A = [2,3,1,1,4]
print(jump_to_end_sr(A))
A = [3,2,1,0,4]
print(jump_to_end_sr(A))
A = [1,3,6,3,2,3,6,8,9,5]
print(jump_to_end_sr(A))
print()


# JUMP COUNT
# sr = simple recurssion 
# track and return min jumpcount 
# if not reachable, return 999 
# O(2^n)
def jump_to_end_sr_jcount(A, i=0, jump=0):
    if A[0] == 0:
        return 999  
    if i+A[i] >= len(A)-1:
        return jump+1
    minJ=999
    for j in range(1,A[i]+1):
        jump += 1    
        ret = jump_to_end_sr_jcount(A, i+j, jump)
        minJ = min(minJ, ret)
    return minJ
#
#
A = [2,3,1,1,4]
print(jump_to_end_sr_jcount(A))
A = [3,2,1,0,4]
print(jump_to_end_sr_jcount(A))
A = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
print(jump_to_end_sr_jcount(A))
print()


# JUMP COUNT
# sr = simple recurssion 
# dp_td = dynamic programming top down (aka memoization) 
# to trace if I have visited an index before)
# O(n^2) 
# so I will not visit them again
# track and return min jumpcount 
# if not reachable, return 999 
def jump_to_end_sr_jcount_dp_td(A, i=0, jump=0, dp=None):
    if A[0] == 0:
        return 999   
    if dp == None:
        dp = []
    if i+A[i] >= len(A)-1:
        return jump+1
    minJ=999
    for j in range(1,A[i]+1):
        jump += 1  
        if not i+j in dp:
            dp.append(i+j)
            ret = jump_to_end_sr_jcount_dp_td(A, i+j, jump, dp)
            minJ = min(minJ, ret)
    return minJ
#
A = [2,3,1,1,4]
print(jump_to_end_sr_jcount_dp_td(A))
A = [3,2,1,0,4]
print(jump_to_end_sr_jcount_dp_td(A))
A = [1,3,6,3,2,3,6,8,9,5]
print(jump_to_end_sr_jcount_dp_td(A))
print() 


# JUMP COUNT
# when we atttempt the largest jump first (being greedy) 
# by using: range(A[i],0,-1), we get a lower step count 
# ( but only in some cases )
# Still O(n^2) 
def jump_to_end_sr_jcount_dp_td(A, i=0, jump=0, dp=None):
    if A[0] == 0:
        return 999   
    if dp == None:
        dp = []
    if i+A[i] >= len(A)-1:
        return jump+1
    minJ=999
    for j in range(A[i],0,-1):
        jump += 1  
        if not i+j in dp:
            dp.append(i+j)
            ret = jump_to_end_sr_jcount_dp_td(A, i+j, jump, dp)
            minJ = min(minJ, ret)
    return minJ
#
A = [2,3,1,1,4]
print(jump_to_end_sr_jcount_dp_td(A))
A = [3,2,1,0,4]
print(jump_to_end_sr_jcount_dp_td(A))
A = [1,3,6,3,2,3,6,8,9,5]
print(jump_to_end_sr_jcount_dp_td(A))
print() 
# while we get a better result for example 3
# example 1 comes back needing more jumps. 


# TRUE FALSE 
# sr = simple recurssion 
# dp_bu = dynamic programming bottom up (aka tabulation 
# by moving right to left I do not need to recur any more
# O(n^2) 
# so I will not visit them again
# track and return min jumpcount 
# if not reachable, return-1
def jump_to_end_sr_jcount_dp_ba(A): 
    if A[0] == 0:
        return -1       
    if A[0] >= len(A)-1:
        return 1
    jump=0
    dp = ['bad']*len(A)
    dp[len(A)-1] = 'good'
    minJ=999
    for i in range(len(A)-2, -1, -1):
        for j in range(1,A[i]+1):
            if i+j <= len(A)-1:
                if dp[i+j] == 'good':
                    dp[i] = 'good'
            if dp[i] == 'bad':
                return -1
    return 1
#
A = [2,3,1,1,4]
print(jump_to_end_sr_jcount_dp_ba(A))
A = [3,2,1,0,4]
print(jump_to_end_sr_jcount_dp_ba(A))
A = [1,3,6,3,2,3,6,8,9,5]
print(jump_to_end_sr_jcount_dp_ba(A))
print() 

# Note, none of the solution above explores
# the entire decision space and hence may 
# not find the min number of jumps! 
# the dp solutions are faster though than 
# the brute forth. 
# 
# one alternative way would be to create a graph 
# of all states and state transitions and then 
# find the shortest path through the graph. 
# That said, there are faster options as per
# below


# TRUE FALSE 
# O(n) algo return true or false using a loop
# the ideal is that if the index moves beyond 
# maxreach (the max index we can reach) I return 
# false
def jump_to_end_On(A):
    maxreach = 0
    for i in range(0,len(A)): 
        if maxreach >= len(A)-1:
            return 1
        maxreach = max(maxreach,i+A[i])
        if i > maxreach:
            return -1
    return -1
#
A = [2,3,1,1,4]
print(jump_to_end_On(A))
A = [3,2,1,0,4]
print(jump_to_end_On(A))
A = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
print(jump_to_end_On(A))
print()


# JUMP COUNT O(n) using one pass four loop
def jump_to_end_jcount_On(A):
    if A[0] == 0:
        return -1
    new_maxreach = maxreach = A[0]
    # min jumps
    minJ = 1
    #
    for i in range(1,len(A)):
        if i > new_maxreach:
            return -1
        new_maxreach = max(new_maxreach, i + A[i])
        if i >= maxreach:
            minJ += 1
            maxreach = new_maxreach
        if maxreach >= len(A)-1:
            return minJ
    return -1
#
A = [2,3,1,1,4]
print(jump_to_end_jcount_On(A))
A = [3,2,1,0,4]
print(jump_to_end_jcount_On(A))
A = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
print(jump_to_end_jcount_On(A))
print()


# # JUMP COUNT O(n)
# as per https://fizzbuzzed.com/thinking_through_jump_game_2/
# does not have a mechanism to bail if end is not reachable
def jump_to_end_while_jcount_On(A):
    maxreach = 0
    minJ = 0
    # next index
    i = 0 
    while (maxreach < (len(A) - 1)):
        new_maxreach = maxreach
        while (i <= maxreach and maxreach < len(A)):
            new_maxreach = max(new_maxreach, i + A[i])
            i += 1
        minJ += 1
        maxreach = new_maxreach
    return minJ
# 
A = [2,3,1,1,4]
print(jump_to_end_while_jcount_On(A))
A = [3,2,1,0,4]
##print(jump_to_end_while_jcount_On(A))
print('mack mack')
A = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
print(jump_to_end_while_jcount_On(A))
