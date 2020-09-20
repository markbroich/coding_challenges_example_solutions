## Find the Factor

# Task: Determine the factors of a number (i.e., all positive integer values that evenly divide into a number) and then return the pth element of the list, 
# sorted ascending. If there is no pth element, return -2.

# Example
# n = 20
# p = 3
# The factors of 20 in ascending order are {1, 2, 4, 5, 10, 20}. Using 1-based indexing, if p = 3, then 4 is returned. If p > 6, 0 would be returned.

# pthFactor has the following parameter(s):
#     int n:  the integer whose factors are to be found
#     int p:  the index of the factor to be returned
# Returns:
#     int: the long integer value of the pth integer factor of n or, if there is no factor at that index, then 0 is returned


# this algo is t O(N) w N being the number we are seeking the factors for
def pthFactor(n,p):
    # test for data issues
    if(n == 'NA' or p == 'NA' or n < 0 or p <= 0): 
        return -1
    #
    facts = []
    for i in range(1, n+1):
        if n%i == 0:
            facts.append(i)
    print(facts)
    if p <= len(facts):
        return facts[p-1]
    else:
        return -2

# test cases
n = 250
p = -1
print(pthFactor(n,p))
n = 20
p = 3
print(pthFactor(n,p))
n = 177
p = 2
print(pthFactor(n,p))
n = 250
p = 4
print(pthFactor(n,p))

print("")
n = 250
p = -1
print(pthFactor(n,p))
n = 20
p = 3
print(pthFactor(n,p))
n = 177
p = 2
print(pthFactor(n,p))
n = 250
p = 4
print(pthFactor(n,p))

# more test cases
print("")
n = 10
p = 3
print(pthFactor(n,p))
n = 10
p = 5
print(pthFactor(n,p))
n = 21
p = 2
print(pthFactor(n,p))
n = 21
p = 3
print(pthFactor(n,p))


# faster algo: O(sqrt(N)) w/o sorting (so when only returning all unsorted factors is required)
# else O(sqrt(N) + nlogn) so O(nlogn)
def pthFactor_faster(n,p,ret_p="FALSE"):
    # test for data issues
    if(n == 'NA' or p == 'NA' or n < 0 or p <= 0): 
        return -1
    #
    facts = []
    i = 1
    #  loop from 1 to int(sqrt(x))
    while i*i <= n:
        if n%i == 0:
            facts.append(i)
            if(n/i != i):
                facts.append(int(n/i))
        i += 1
    if not ret_p: 
        return facts
    else:
        # sort and retrun output p 
        facts = sorted(facts) # O(nlogn)
        if p <= len(facts):
            return facts[p-1]
        else:
            return -2

# test cases
n = 250
p = -1
print(pthFactor_faster(n,p, ret_p="TRUE"))
n = 20
p = 3
print(pthFactor_faster(n,p, ret_p="TRUE"))
n = 177
p = 2
print(pthFactor_faster(n,p, ret_p="TRUE"))
n = 250
p = 4
print(pthFactor_faster(n,p, ret_p="TRUE"))

print("")
n = 250
p = -1
print(pthFactor_faster(n,p, ret_p="TRUE"))
n = 20
p = 3
print(pthFactor_faster(n,p, ret_p="TRUE"))
n = 177
p = 2
print(pthFactor_faster(n,p, ret_p="TRUE"))
n = 250
p = 4
print(pthFactor_faster(n,p, ret_p="TRUE"))

# more test cases
print("")
n = 10
p = 3
print(pthFactor_faster(n,p, ret_p="TRUE"))
n = 10
p = 5
print(pthFactor_faster(n,p, ret_p="TRUE"))
n = 21
p = 2
print(pthFactor_faster(n,p, ret_p="TRUE"))
n = 21
p = 3
print(pthFactor_faster(n,p, ret_p="TRUE"))
print("")

# test runtime of brute force vs sqrt algo with large n
import time

n = 1000000000 
p = 4

t0 = time.time()
print(pthFactor_faster(n,p))
t1 = time.time()
total = t1-t0
print(total)


t0 = time.time()
print(pthFactor(n,p))
t1 = time.time()
total = t1-t0
print(total)

# w inspiration from: https://www.rookieslab.com/posts/most-efficient-way-to-find-all-factors-of-a-number-python-cpp







