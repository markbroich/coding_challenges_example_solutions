"""
Find K Closest Ints
Given a sorted integer array arr, two integers k and x, return the k closest
integers to x in the array. The result should also be sorted in ascending
order.

An integer a is closer to x than an integer b if:
|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

Example 3:
Input: arr = [1,2,3,4,5], k = 2, x = 2
Output: [1,2]]

Constraints:
1 <= k
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
"""


# Ot(n + n log(n) + k + k log (k)) Os(n + k)
# reduces to: O(n)
def k_closest(arr: list, x: int, k: int) -> list:
    if k > len(arr):
        return arr
    # O(n)
    diff_and_idx = [((abs(arr[i] - x), i)) for i in range(len(arr))]
    # Ot(n log n) Os(1)
    diff_and_idx.sort(key=lambda e: (e[0], e[1]))
    # O(k)
    res = [arr[diff_and_idx[i][1]] for i in range(k)]
    # Ot(k log(k)) Os(1)
    res.sort()
    return res


# Ot(log(n)) were n is len of arr
# Os(k)
def k_closest_fast_short(arr: list, x: int, k: int) -> list:
    if k > len(arr):
        return arr
    elif x < arr[0]:
        return arr[0: k]
    elif x > arr[len(arr) - 1]:
        return arr[-k:]

    left = 0
    right = len(arr) - 1
    # move in to find min difference
    while left < right:
        mid = left + int((right - left) / 2)
        if abs(arr[mid] - x) >= abs(arr[mid + 1] - x):
            left = mid + 1
        else:
            right = mid - 1

    # move out from min difference
    # until k, favoring left if tie.
    left = right = mid
    while right - left < k - 1:
        if abs(arr[left] - x) <= abs(arr[right] - x):
            if left > 0:
                left -= 1
            else:
                right += 1
        else:
            if right < len(arr) - 1:
                right += 1
            else:
                left -= 1
    return arr[left: right + 1]


# Ot(log(n)) were n is len of arr Os(1) +  Ot(k log(k)) Os(k)
def k_closest_fast(arr: list, x: int, k: int) -> list:
    if not arr or not x or not k:
        return []
    if k > len(arr):
        return arr

    # Ot(log(n)) were n is len of arr Os(1)
    idx_of_closest = find_closest_idx(arr, x)

    # Ot(k) Os(k)
    if idx_of_closest == 0:
        return arr[:k]
    elif idx_of_closest == len(arr) - 1:
        return arr[-k:]

    # Ot(k) Os(k)
    ret = populate_return(arr, x, k, idx_of_closest)
    # Ot(k log(k)) Os(1)
    ret.sort()
    return ret


# Ot(log(n)) were n is len of arr Os(1)
def find_closest_idx(arr: list, x: int) -> int:
    if x < arr[0]:
        return 0
    elif x > arr[len(arr) - 1]:
        return len(arr) - 1

    left = 0
    right = len(arr) - 1
    mid = int(len(arr) / 2)
    prior_mid = mid + 1
    while mid != prior_mid:
        if arr[mid] == x:
            return mid
        if x - arr[mid] < 0:
            right = mid - 1
        else:
            left = mid
        prior_mid = mid
        mid = right + int((left - right) / 2)
    return mid


# Ot(k) Os(k)
def populate_return(arr: list, x: int, k: int, idx_of_closest: int) -> list:
    ret = [''] * k
    i = 0
    left_idx = idx_of_closest
    right_idx = left_idx + 1
    while k > 0:
        chosen_idx = a_vs_b(arr, x, left_idx, right_idx)
        ret[i] = arr[chosen_idx]
        if chosen_idx == left_idx:
            if left_idx - 1 >= 0:
                left_idx -= 1
            else:
                left_idx = right_idx
                right_idx += 1
        else:
            if right_idx + 1 < len(arr):
                right_idx += 1
            else:
                right_idx = left_idx
                left_idx -= 1
        i += 1
        k -= 1
    return ret


def a_vs_b(arr: list, x: int, a: int, b: int) -> int:
    if abs(arr[a] - x) < abs(arr[b] - x) or abs(arr[a] - x) == abs(arr[b] - x):
        return a
    return b


def tests():
    # # full test of k_closest_fast
    arr = [1,2,3,4,5]
    k = 8
    x = 3
    exp = [1,2,3,4,5]
    print(k_closest(arr, x, k) == exp)
    print(k_closest_fast_short(arr, x, k) == exp)
    print(k_closest_fast(arr, x, k) == exp)

    arr = [1,2,3,4,5]
    k = 4
    x = 3
    exp = [1,2,3,4]
    print(k_closest(arr, x, k) == exp)
    print(k_closest_fast_short(arr, x, k) == exp)
    print(k_closest_fast(arr, x, k) == exp)

    arr = [1,2,3,4,5]
    k = 4
    x = -1
    exp = [1,2,3,4]
    print(k_closest(arr, x, k) == exp)
    print(k_closest_fast_short(arr, x, k) == exp)
    print(k_closest_fast(arr, x, k) == exp)

    arr = [1,2,3,4,5]
    k = 2
    x = 2
    exp = [1,2]
    print(k_closest(arr, x, k) == exp)
    print(k_closest_fast_short(arr, x, k) == exp)
    print(k_closest_fast(arr, x, k) == exp)

    arr = [1,2,3,4,5]
    k = 3
    x = 4
    exp = [3,4,5]
    print(k_closest(arr, x, k) == exp)
    print(k_closest_fast_short(arr, x, k) == exp)
    print(k_closest_fast(arr, x, k) == exp)

    arr = [1,2,3,4,5]
    k = 2
    x = 7
    exp = [4,5]
    print(k_closest(arr, x, k) == exp)
    print(k_closest_fast_short(arr, x, k) == exp)
    print(k_closest_fast(arr, x, k) == exp)


   # # find_closest_idx
    # arr = [1,2,3,4,5]
    # x = 3
    # print(find_closest_idx(arr, x) == 2)

    # arr = [1,2,3,4,5]
    # x = -1
    # print(find_closest_idx(arr, x) == 0)

    # arr = [1,2,3,4,5]
    # x = 2
    # print(find_closest_idx(arr, x) == 1)

    # arr = [1,2,3,4,5]
    # x = 4
    # print(find_closest_idx(arr, x) == 3)

    # arr = [1,2,3,4,5]
    # x = 1
    # print(find_closest_idx(arr, x) == 0)

    # arr = [1,2,3,4,5]
    # x = 5
    # print(find_closest_idx(arr, x) == 4)

    # arr = [1,2,3,4,5]
    # x = 6
    # print(find_closest_idx(arr, x) == 4)

    # arr = [1,2,4,5]
    # x = 3
    # print(find_closest_idx(arr, x) == 1)

    # arr = [1,4,8,9]
    # x = 6
    # print(find_closest_idx(arr, x) == 1)

    # arr = [0,1,2,3,4,8,9]
    # x = 6
    # print(find_closest_idx(arr, x) == 4)

    # arr = [0,1,2,3,4,8,9]
    # x = 7
    # print(find_closest_idx(arr, x) == 4)


tests()
