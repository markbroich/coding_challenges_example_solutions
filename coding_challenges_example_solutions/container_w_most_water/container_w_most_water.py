# Container With Most Water

# Given n non-negative integers a1, a2, ..., an,
# where each represents a point at coordinate (i, ai).
# 'n' vertical lines are drawn such that the two endpoints of 
# line i is at (i, ai) and (i, 0).

# Find two lines, which together with x-axis forms a container, 
# such that the container contains the most water.
# The program should return an integer which corresponds to the 
# maximum area of water that can be contained 


# Example:
# Input : [1, 5, 4, 3]
# Output : 6

# Explanation : 5 and 3 are distance 2 apart. So size of the 
# base = 2. Height of container = min(5, 3) = 3. 
# So total area = 3 * 2 = 6


# brute forth w O(n^2)
def max_container_bf(arr):
    area = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            area = max(area, (min(arr[i], arr[j]) * (j-i) )
    return area

arr = [1, 5, 4, 3]
print(max_container_bf(arr))
arr = [1, 5, 4, 3, 1, 3, 4, 3]
print(max_container_bf(arr))



## Pointers:
# The maximum possible base can be N-1                                  
# When considering a1 and aN, then the area is (N-1) * min(a1, aN)     
# This implies that if there was a better solution possible, 
# it will definitely have height greater than min(a1, aN).

# So, I can discard min(a1, aN) from the set               
# and look to solve this problem again from the start. 

# If a1 < aN, then the problem reduces to solving the same thing for a2, aN. 
# Else, it reduces to solving the same thing for a1, aN-1


# O(n) solution
def max_container_n(arr):
    area = 0
    #area = len(arr)-1 * min(arr[0],arr[len(arr)-1])
    i = 0
    j = len(arr)-1
    while j > i:
        area = max(area, (j-i) * min(arr[i],arr[j]) )
        # walk the pointers inward
        if arr[i] > arr[j]:
            j -= 1
        else: 
            i +=1
    return area


arr = [1, 5, 4, 3]
print(max_container_n(arr))
arr = [1, 5, 4, 3, 1, 3, 4, 3]
print(max_container_n(arr))


