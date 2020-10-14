## Pascal triangle
# A Pascal triangle is a triangular array of integers constructed with the following characteristics:

# 1. The first row consists of the number 1.
# 2. For each subsequent row, each element is the sum of the numbers directly above it, on either side.

# Here is an example of the first 7 rows:

#         1
#        1 1
#       1 2 1   
#      1 3 3 1
#     1 4 6 4 1
#   1 5 10 10 5 1 
#  1 6 15 20 15 6 1

# Task:
# Given an input N, return the Nth row of Pascal's triangle in a list.
# Example for N = 5

# >>> pascal(N) 
#  [1, 4, 6, 4, 1]



# big O time:
# n*(n+1)/2, which is in O(n^2)

# simple nested loop algo:
def pascal_simple_nested_loop(n):
    pasc_tria = [1,[1,1]]
    if n <= 2:
        return pasc_tria[0:n]
    else:
        for i in range(1,n):
            new_row = [1]
            for j in range(0, len(pasc_tria[i])-1):
                new_row.append(pasc_tria[i][j] + pasc_tria[i][j+1])
            new_row.append(1)
            pasc_tria.append(new_row)
        return pasc_tria

# print(pascal_simple_nested_loop(2))
# print()
# print(pascal_simple_nested_loop(3))
# print()
print('pascal_simple_nested_loop(6)')
print(pascal_simple_nested_loop(6))
print('')

## Another option is the following algo: 
# create a copy of a row and add a leading zero
# create a copy of a row and add a trailing zero
# add the two copies pairwise.

# E.g row #4:    1 3 3 1
#
# leading zero:  0 1 3 3 1
# trailing zero: 1 3 3 1 0
# pairwise sum:  1 4 6 4 1 
# gives us row #5

# here is the function: 
def PascalTriangle_zip(n):
    pasc_tria = []
    prior_row = [1]
    a_zero = [0]
    for x in range(n):
        pasc_tria.append(prior_row)
        # zip(prior_row+a_zero, a_zero+prior_row) 
        # zips together prior_row once with a leading 0 and once with a trailing zero
        prior_row=[left+right for left,right in zip(prior_row+a_zero, a_zero+prior_row)]
    return pasc_tria

print('PascalTriangle_zip(7)')
print(PascalTriangle_zip(7))
print('')

# same as above but with print statements to show the inner working
def PascalTriangle_zip_show(n):
    prior_row = [1]
    a_zero = [0]
    for x in range(n):
        # added 2 print statements to show what is happening:
        print('prior_row ', prior_row)
        for i in (zip(prior_row+a_zero, a_zero+prior_row)):
            print(i, 'sum: ',sum(i))
        prior_row=[left+right for left,right in zip(prior_row+a_zero, a_zero+prior_row)]    
    return ""

print('PascalTriangle_zip_show(4)')
print(PascalTriangle_zip_show(4))
print('')


## Another way to look at the pascal triangle is as a representation 
# of a number of combinations of n choose k at a time 
#
#         1
#        1 1
#       1 2 1   
#      1 3 3 1
#     1 4 6 4 1
#   1 5 10 10 5 1 
#  1 6 15 20 15 6 1

# considering the equation for number of combinations, of n choose k at a time: 
# combination_count(n,k) = factorial(n) / factorial(k) * factorial(n - k)

# and taken e.g. 
# row 4 with 4 items (so n = 4)
# and stepping through the following 5 numbers:
# 0 1 2 3 4 as k

# so:               n,k
# combination_count(4,0) = 1
# combination_count(4,1) = 4
# combination_count(4,2) = 6
# combination_count(4,3) = 4
# combination_count(4,4) = 1

# which is the result for row number 5. 

# as an algo
# calc number of combinations, of n choose k at a time
import math
def combinations(n, k):
    return int((math.factorial(n)) / ((math.factorial(k)) * math.factorial(n - k)))

# factorial w/o an external library 
def fact(n):
    res = 1
    for c in range(1,n + 1):
        res = res * c
    return res

def PascalTriangle_fact(rows):
    pasc_tria = []
    for n in range(rows): 
        row = [] 
        for k in range(n + 1): 
            # putting this in a list doesn't do anything.
            # [pascals_tri_formula.append(combination(count, element))]
            row.append(combinations(n, k))
        pasc_tria.append(row)
    return pasc_tria

print('PascalTriangle_fact(7)')
print(PascalTriangle_fact(7))
print('')

