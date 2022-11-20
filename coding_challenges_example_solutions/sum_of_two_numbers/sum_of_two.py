"""
find two numbers in array that sum to s and return them
else, return (float('-inf'), float('-inf'))
input is sorted

arr = [1, 2, 3, 9]
s = 8
exp = empty_return

arr = [1, 2, 4, 4]
s = 8
exp = (4, 4)
"""

from typing import Tuple


# Ot(log n) Os(1) where n is lengeht or arr
def find_sum(arr: list, s: int) -> Tuple:
    '''do a bianry search'''
    empty_return = (float('-inf'), float('-inf'))
    if not arr or len(arr) < 2 or not s:
        return empty_return
    if len(arr) == 2 and sum(arr) != s:
        return empty_return

    left = 0
    right = len(arr) - 1
    while True:
        if arr[left] + arr[right] == s:
            return arr[left], arr[right]
        if right - left == 1:
            return empty_return
        mid = left + int((right - left) / 2)
        ls = arr[left] + arr[mid]
        rs = arr[mid] + arr[right]
        if ls == s:
            return arr[left], arr[mid]
        if rs == s:
            return arr[mid], arr[right]
        if ls < s:
            if rs < s:
                left = mid
            else:
                left += 1
                right -= 1
        else:
            right = mid


def tests() -> None:
    empty_return = (float('-inf'), float('-inf'))

    arr = [1, 2, 4, 4]
    s = 8
    exp = (4, 4)
    print(find_sum(arr, s) == exp)

    arr = []
    s = 8
    exp = empty_return
    print(find_sum(arr, s) == exp)

    arr = [1, 1]
    s = None
    exp = empty_return
    print(find_sum(arr, s) == exp)

    arr = [1]
    s = 1
    exp = empty_return
    print(find_sum(arr, s) == exp)

    arr = [1, 1]
    s = 2
    exp = (1, 1)
    print(find_sum(arr, s) == exp)

    arr = [1, 2, 3, 9]
    s = 8
    exp = empty_return
    print(find_sum(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 0
    exp = empty_return
    print(find_sum(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 2
    exp = (1, 1)
    print(find_sum(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 3
    exp = empty_return
    print(find_sum(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 4
    exp = (1, 3)
    print(find_sum(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 5
    exp = empty_return
    print(find_sum(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 6
    exp = (1, 5)
    print(find_sum(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 7
    exp = empty_return
    print(find_sum(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 8
    exp = (3, 5)
    print(find_sum(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 9
    exp = (1, 8)
    print(find_sum(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 10
    exp = (1, 9)
    print(find_sum(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 11
    exp = (3, 8)
    print(find_sum(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 12
    exp = (5, 7)
    print(find_sum(arr, s) == exp)

tests()


"""
assume arr is not sorted. Return True if a pair exists, else return False
"""


# Ot(n) Os(n) where n is length of the array
def find_sum_in_unsorted(arr: list, s: int) -> bool:
    if not arr or len(arr) < 2 or not s:
        return False
    if len(arr) == 2 and sum(arr) != s:
        return False

    complementary = set()
    for val in arr:
        # print(s, arr, val, complementary)
        if val in complementary:
            return True
        complementary.add(s - val)
    return False


def tests_unsorted() -> None:
    arr = [8, 1, 3, 5, 7, 1, 8, 9]
    s = 12
    exp = True
    print(find_sum_in_unsorted(arr, s) == exp)

    arr = [1, 2, 4, 4]
    s = 8
    exp = True
    print(find_sum_in_unsorted(arr, s) == exp)

    arr = []
    s = 8
    exp = False
    print(find_sum_in_unsorted(arr, s) == exp)

    arr = [1,1]
    s = None
    exp = False
    print(find_sum_in_unsorted(arr, s) == exp)

    arr = [1]
    s = 1
    exp = False
    print(find_sum_in_unsorted(arr, s) == exp)

    arr = [1, 1]
    s = 2
    exp = True
    print(find_sum_in_unsorted(arr, s) == exp)

    arr = [1, 2, 3, 9]
    s = 8
    exp = False
    print(find_sum_in_unsorted(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 0
    exp = False
    print(find_sum_in_unsorted(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 2
    exp = True
    print(find_sum_in_unsorted(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 3
    exp = False
    print(find_sum_in_unsorted(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 4
    exp = True
    print(find_sum_in_unsorted(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 5
    exp = False
    print(find_sum_in_unsorted(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 6
    exp = True
    print(find_sum_in_unsorted(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 7
    exp = False
    print(find_sum_in_unsorted(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 8
    exp = True
    print(find_sum_in_unsorted(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 9
    exp = True
    print(find_sum_in_unsorted(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 10
    exp = True
    print(find_sum_in_unsorted(arr, s) == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 11
    exp = True
    print(find_sum_in_unsorted(arr, s)  == exp)

    arr = [1, 1, 3, 5, 7, 8, 8, 9]
    s = 12
    exp = True
    print(find_sum_in_unsorted(arr, s) == exp)

    arr = [-6, 2, 3, 5, 1, 8, 8, 9]
    s = -5
    exp = True
    print(find_sum_in_unsorted(arr, s) == exp)

    arr = [-6, 2, 3, 5, -1, 8, 8, 9]
    s = -7
    exp = True
    print(find_sum_in_unsorted(arr, s) == exp)


print()
tests_unsorted()


"""
assume arr is not sorted. Return True if a pair exists, else return False
Assume arr does not fit in memory but has a limited range.
Hence, assume set fits in memory.

Then, break arr into chunks, send to workers to build complimentary dict where
value is occurance count.
Merge dicts together and send back to workers for eval once more
this time without adding to the dict.
If s - val == val, then
dict[s - va] > 1 to return True, elif dict[s - va] to return True.
This would be Ot(n) and Os(m) where n is chunk on worker and m is length
of dict.
"""


# Ot(m) Os(m + n) where m and n are the key counts of the two dicts
# and m is the longer one.
def merge_dicts(d1: dict, d2: dict) -> dict:
    if not d1 or not d2:
        return {}
    if len(d2) > len(d1):
        d1, d2 = d2, d1
    for key, value in d1.items():
        if key in d2:
            d2[key] += value
        else:
            d2[key] = value
    return d2

print()
d1 = {1: 2, 3: 5, 5: 1}
d2 = {1: 2, 3: 2, 8: 1}
exp = {1: 4, 3: 7, 8: 1, 5: 1}
print(merge_dicts(d1, d2) == exp)

d1 = {1: 2, 3: 5, 5: 1}
d2 = {1: 2, 3: 2, 8: 1, 10: 10}
exp = {1: 4, 3: 7, 5: 1, 8: 1, 10: 10}
print(merge_dicts(d1, d2) == exp)