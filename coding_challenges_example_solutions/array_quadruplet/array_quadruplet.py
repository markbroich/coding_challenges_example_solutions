
'''
Array Quadruplet

Given an unsorted array of integers arr and a number s, write a function
findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum
up to s. Your function should return an array of these numbers in an
ascending order. If such a quadruplet doesn’t exist, return an empty array.

Note that there may be more than one quadruplet in arr whose sum is s.
You’re asked to return the first one you encounter
(considering the results are sorted).

Example:
arr =  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20

output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
                     # whose sum is 20. Notice that there
                     # are two other quadruplets whose sum is 20:
                     # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
                     # asked to return the just one quadruplet (in an
                     # ascending order)
Constraints:
[time limit] 5000ms
[input] array.integer arr
1 ≤ arr.length ≤ 100
[input] integer s
[output] array.integer
'''


# Ot(n**4)
def find_array_quadruplet_slow(arr, s):
    if len(arr) < 4:
        return []
    res = set()
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            for m in range(0, len(arr)):
                for n in range(0, len(arr)):
                    if i != j and i != m and i != n and j != m and j != n and m != n:
                        if arr[i] + arr[j] + arr[m] + arr[n] == s:
                            res.add(tuple(sorted([arr[i], arr[j], arr[m], arr[n]])))
    smallest = (float('inf'), float('inf'), float('inf'), float('inf'))
    for tup in res:
        if tup < smallest:
            smallest = tup
    if smallest[0] == float('inf'):
        return []
    return list(smallest)


# Ot(n**3) Os(1)
def find_array_quadruplet(arr, s):
    if len(arr) < 4:
        return []
    # Ot(n log n)
    arr.sort()
    if len(arr) == 4:
        if sum(arr) == s:
            return arr
        return []
    
    for i in range(len(arr) - 4):
        for j in range(i + 1, len(arr) - 3):
            r1 = s - (arr[i] + arr[j])
            left = j + 1
            right = len(arr) - 1
            while left < right:
                r2 = arr[left] + arr[right]
                if r1 == r2:
                    res = [arr[i], arr[j], arr[left], arr[right]]
                    # Ot(4 log 4)
                    res.sort()
                    return res
                elif r2 > r1:
                    right -= 1
                else:
                    left += 1
    return []


def tests():
    arr = [2,7,4,0,9,5,1,3]
    s = 20
    exp = [0,4,7,9]
    print(find_array_quadruplet_slow(arr, s) == exp)
    print(find_array_quadruplet(arr, s) == exp)

    arr = []
    s = 12
    exp = []
    print(find_array_quadruplet_slow(arr, s) == exp)
    print(find_array_quadruplet(arr, s) == exp)

    arr = [4,4,4]
    s= 12
    exp = []
    print(find_array_quadruplet_slow(arr, s) == exp)
    print(find_array_quadruplet(arr, s) == exp)

    arr = [4,4,4,2]
    s = 16
    exp = []
    print(find_array_quadruplet_slow(arr, s) == exp)
    print(find_array_quadruplet(arr, s) == exp)

    arr = [4,4,4,4]
    s = 16
    exp = [4,4,4,4]
    print(find_array_quadruplet_slow(arr, s) == exp)
    print(find_array_quadruplet(arr, s) == exp)

    arr = [2,7,4,0,9,5,1,3]
    s = 20
    exp = [0,4,7,9]
    print(find_array_quadruplet_slow(arr, s) == exp)
    print(find_array_quadruplet(arr, s) == exp)

    arr = [2,7,4,0,9,5,1,3]
    s = 120
    exp = []
    print(find_array_quadruplet_slow(arr, s) == exp)
    print(find_array_quadruplet(arr, s) == exp)

    arr = [1,2,3,4,5,9,19,12,12,19]
    s= 40
    exp = [4,5,12,19]
    print(find_array_quadruplet_slow(arr, s) == exp)
    print(find_array_quadruplet(arr, s) == exp)  


tests()