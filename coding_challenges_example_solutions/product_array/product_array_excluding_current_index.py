# Product Array (excluding current index)

# return a result array that is the product of the array 
# excluding the index

# e.g. 
# arr = [1, 2, 3, 4]
# result = [24, 12, 8, 6]

# or: 
# arr = [2, 3, 4, 5]
# result = [60, 40, 30, 24]

# The product of all the values to the left of index i with all the values to the right of index i.

# the left values, i.e. [1, 1*2, 1*2*3, 1*2*3*4] and their complements, the right values, i.e. [3*4*5*1, 4*5*1, 5*1, 1].
# Notice that it is the product of these two sequences, element by element, that gives us the desired result.

# But, how to create these sequences? 

########
import time 
import random

import numpy as np


# brute forth (Ot(n**2), Os(n))
def calcProductArray1(arr):
    n = len(arr) 
    if(n == 0 or n == 1):
        # no values to multiply if n equals to 0 or 1
        return []
    productArr = [1]*n

    for i in range(0, n):
        for j in range(0, n):
            if i != j:
                productArr[i] *= arr[j]
    return productArr

arr = [1, 2, 3, 4]
print(calcProductArray1(arr))
arr = [2, 3, 4, 5]
print(calcProductArray1(arr))


# much faster but more space: (Ot(n+n), Os(n*3))
def calcProductArray2(arr):
    n = len(arr) 
    if(n == 0 or n == 1):
        # no values to multiply if n equals to 0 or 1
        return []

    # Allocate memory for temporary arrays left[] and right[]  
    # and the productArr
    left = [0]*n  
    right = [0]*n  
    productArr = ['']*n
    
    # Left most element of left array is always 1  
    left[0] = 1
    # Rightmost most element of right array is always 1  
    right[n - 1] = 1
  
    # Construct the left array  
    for i in range(1, n):  
        left[i] = arr[i - 1] * left[i - 1]  

    # Construct the right array  
    for j in range(n-2, -1, -1):  
        right[j] = arr[j + 1] * right[j + 1]  
    
    # Construct the product array using  
    # left[] and right[]  
    for i in range(n):  
        productArr[i] = left[i] * right[i]  

    return productArr

arr = [1, 2, 3, 4]
print(calcProductArray2(arr))
arr = [2, 3, 4, 5]
print(calcProductArray2(arr))


# much faster and less space: (Ot(n+n), Os(n))
def calcProductArray3(arr):
    n = len(arr) 
    if(n == 0 or n == 1):
        # no values to multiply if n equals to 0 or 1
        return []
    productArr = ['']*n
    
    # In this loop, temp variable contains product of 
    # elements on left side excluding arr[i]  
    temp = 1
    for i in range(0, n):
        productArr[i] = temp
        temp *= arr[i]
    
    # In this loop, temp variable contains product of 
    # elements on right side excluding arr[i]  
    temp = 1
    for i in range(n-1, -1, -1):
        productArr[i] *= temp
        temp *= arr[i]
    return productArr

arr = [1, 2, 3, 4]
print(calcProductArray3(arr))
arr = [2, 3, 4, 5]
print(calcProductArray3(arr))
print()


# time mean runtime of a function func
# using a random array or length n, and 
# average over nt times
def timer(func, n=100, nt=10):
    random.seed(1)
    arr = [random.randint(1, n) for i in range(n)]
    timeArr = [0]*nt

    start_time = time.time()
    for i in range(nt):
        prodArr = func(arr)
        timeArr[i] = time.time() - start_time
    print(np.mean(timeArr))

n= 100
nt = 10
print('mean runtime of 3 versions of the function')
# brute forth (Ot(n**2), Os(n))
timer(calcProductArray1, n, nt)
# much faster but more space: (Ot(n+n), Os(n*3))
timer(calcProductArray2, n, nt)
# much faster and less space: (Ot(n+n), Os(n))
timer(calcProductArray3, n, nt)







