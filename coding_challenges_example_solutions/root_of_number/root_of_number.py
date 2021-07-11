## Root of Number

# Many times, we need to re-implement basic functions 
# without using any standard library functions already 
# implemented. For example, when designing a chip that 
# requires very little memory space.

# In this question we’ll implement a function root that 
# calculates the n’th root of a number. The function takes 
# a nonnegative number x and a positive integer n, and 
# returns the positive n’th root of x within an error of
#  0.001 (i.e. suppose the real root is y, then the error 
# is: |y-root(x,n)| and must satisfy |y-root(x,n)| < 0.001).

# Don’t be intimidated by the question. While there are many 
# algorithms to calculate roots that require prior knowledge 
# in numerical analysis (some of them are mentioned here), 
# there is also an elementary method which doesn’t require 
# more than guessing-and-checking. Try to think more in terms 
# of the latter.

# Make sure your algorithm is efficient, and analyze its time 
# and space complexities.


## Examples:

# input:  x = 7, n = 3
# output: 1.913

# input:  x = 9, n = 2
# output: 3

## Constraints:
# [time limit] 5000ms
# [input] float x
# 0 ≤ x
# [input] integer n
# 0 < n
# [output] float

# x tp the power of n
# rather than x**n 
def power(x ,n):
  res = 1
  for i in range(n):
    res *= x
  return res


import numpy as np

# iterate up.
# a small step may be slow and a 
# large step may never converge
def root(x, n, step=0.001, thr=0.001):
    for i in np.arange(thr,x,step):
        xhat = power(i ,n)
        if abs(xhat - x) < thr:
            break
    return i


# O(log(x))
# O(1)
def root_binarysearch_a(x, n, thr=0.001):
    #
    lo = thr
    hi = x
    #
    apxRoot = lo + ((hi - lo) / 2)
    while abs(power(apxRoot, n)  - x) > thr:
      # or while (apxRoot - lo >= thr):
      if power(apxRoot, n) < x:
        lo = apxRoot
      else:
        hi = apxRoot
      apxRoot = (lo + hi) / 2
    #
    return apxRoot
  
print(root(27, 3))

print(root(3, 2))

# input:  x = 9, n = 2
# output: 3
# 3**2 = 9 or 3**n = x



def root_binarysearch_b(x, n, thr=0.001):
    #
    lo = thr
    hi = x
    #
    while True:
        mid = (lo + hi) / 2
        xhat = power(mid, n) 
        diff = xhat - x
        #
        if abs(diff) < thr:
            break
        elif diff < 0:
            # up
            lo = mid
        else:
            # down      
            hi = mid
    #
    return mid


def testing(thr=0.001):
    x = 7
    n = 3
    expected = 1.913
    print(abs(root_binarysearch_a(x, n) - expected) < thr)
    print(abs(root_binarysearch_b(x, n) - expected) < thr)

    x = 9
    n = 2
    expected = 3
    print(abs(root_binarysearch_a(x, n) - expected) < thr)
    print(abs(root_binarysearch_b(x, n) - expected) < thr)
    
    x = 870
    n = 3
    expected = 9.54640270936004
    print(abs(root_binarysearch_a(x, n) - expected) < thr)
    print(abs(root_binarysearch_b(x, n) - expected) < thr)

    x = 4
    n = 2
    expected = 2
    print(abs(root_binarysearch_a(x, n) - expected) < thr)
    print(abs(root_binarysearch_b(x, n) - expected) < thr)

    x = 27
    n = 3
    expected = 3
    print(abs(root_binarysearch_a(x, n) - expected) < thr)
    print(abs(root_binarysearch_b(x, n) - expected) < thr)

    x = 16
    n = 4
    expected = 2
    print(abs(root_binarysearch_a(x, n) - expected) < thr)
    print(abs(root_binarysearch_b(x, n) - expected) < thr)

    x = 3
    n = 2
    expected = 1.732
    print(abs(root_binarysearch_a(x, n) - expected) < thr)
    print(abs(root_binarysearch_b(x, n) - expected) < thr)

    x = 10
    n = 3
    expected = 2.154
    print(abs(root_binarysearch_a(x, n) - expected) < thr)
    print(abs(root_binarysearch_b(x, n) - expected) < thr)

    x = 160
    n = 3
    expected = 5.429
    print(abs(root_binarysearch_a(x, n) - expected) < thr)
    print(abs(root_binarysearch_b(x, n) - expected) < thr)

testing()



