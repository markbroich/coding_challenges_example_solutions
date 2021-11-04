'''Counting Triangles

Given a list of N triangles with integer side lengths, determine how many
different triangles there are. Two triangles are considered to be the same
if they can both be placed on the plane such that their vertices occupy
exactly the same three points.

Signature
int countDistinctTriangles(ArrayList<Sides> arr)
or
int countDistinctTrianges(int[][] arr)

Input
In some languages, arr is an Nx3 array where arr[i] is a length-3 array that
contains the side lengths of the ith triangle. In other languages, arr is a
list of structs/objects that each represent a single triangle with side
lengths a, b, and c.
It's guaranteed that all triplets of side lengths represent real triangles.
All side lengths are in the range [1, 1,000,000,000]
1 <= N <= 1,000,000

Output
Return the number of distinct triangles in the list.


Example 1
arr = [[2, 2, 3], [3, 2, 2], [2, 5, 6]]
output = 2
The first two triangles are the same, so there are only 2 distinct triangles.

Example 2
arr = [[8, 4, 6], [100, 101, 102], [84, 93, 173]]
output = 3
All of these triangles are distinct.

Example 3
arr = [[5, 8, 9], [5, 9, 8], [9, 5, 8], [9, 8, 5], [8, 9, 5], [8, 5, 9]]
output = 1
All of these triangles are the same.
'''

'''
Apporach:

Loop over tups and sort each tup Ot(t * n log(n)) where t is
tup count and n is sides in triange, so 3. So ~ t * 3

then sort list of tups Ot(t log(t))

then loop over list of tups and count distinct Ot(k)

So, with k = 100000
k * math.log(3) * 3) + int(k * math.log(k) + k * 3 =
1780875


'''


# Ot(k * 3 * log*(3) + k log(k) + k * 3) 
# Ot(k log(k))  dominates. k is number of triangles
# Os(1)
def countDistinctTriangles(arr):
    sort_triangel_sides(arr)
    # sort triangles
    # Ot(t log(t))
    # Os(1)
    arr.sort()
    dCnt = 1
    dCnt = count_distinct(arr, dCnt)
    return dCnt


# Ot(t * n log(n))
# Os(1)
def sort_triangel_sides(arr):
    for i in range(0, len(arr)):
        arr[i] = sorted(arr[i])


# Ot(t * n) so Ot(t)
# where t is tup count and n is sides in triange
# Os(1)
def count_distinct(arr, dCnt):
    for i in range(0, len(arr)-1):
        if arr[i] != arr[i + 1]:
            dCnt += 1
    return dCnt


# OR: 
# Ot(k log(k)). k is number of triangles. faster for sure!
# Os(d) were d ist the number of distinct triangles
def countDistinctTriangles_set(arr):
    mySet = set()
    for i in range(0, len(arr)):
        mySet.add(tuple(sorted(arr[i])))
    return len(mySet)


# example 1
arr = [(7, 6, 5), (5, 7, 6), (8, 2, 9), (2, 3, 4), (2, 4, 3)]
expected = 3
print(expected == countDistinctTriangles(arr))
print(expected == countDistinctTriangles_set(arr))

# example 2
arr = [(3, 4, 5), (8, 8, 9), (7, 7, 7)]
expected = 3
print(expected == countDistinctTriangles(arr))
print(expected == countDistinctTriangles_set(arr))

# example 3
arr = [[2, 2, 3], [3, 2, 2], [2, 5, 6]]
expected = 2
print(expected == countDistinctTriangles(arr))
print(expected == countDistinctTriangles_set(arr))

# example 4
arr = [[8, 4, 6], [100, 101, 102], [84, 93, 173]]
expected = 3
print(expected == countDistinctTriangles(arr))
print(expected == countDistinctTriangles_set(arr))

# example 5
arr = [[5, 8, 9], [5, 9, 8], [9, 5, 8], [9, 8, 5], [8, 9, 5], [8, 5, 9]]
expected = 1
print(expected == countDistinctTriangles(arr))
print(expected == countDistinctTriangles_set(arr))


# simulation
import math
import random

t = 100000
s = 1000000000
arr = [''] * t
for i in range(0, t):
    myLst = [''] * 3
    # random create 2 sides
    for j in range(0, 2):
        myLst[j] = random.randint(1, s)
        # random angle
    a = random.randint(1, 90)
    # calc 3rd side
    myLst[2] =int((myLst[0]**2 + myLst[1]**2 - 2*myLst[0]*myLst[1] * math.cos(math.radians(a)))** 0.5)
    arr[i] = tuple(myLst)

print(countDistinctTriangles(arr))