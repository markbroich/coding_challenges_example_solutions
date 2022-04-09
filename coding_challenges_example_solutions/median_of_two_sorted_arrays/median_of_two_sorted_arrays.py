
'''
==================================================================================

# Median of two sorted arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''


# Ot(len(arr1) + len(arr2)), Os(len(arr1) + len(arr2))
def median_of_sorted_arrays(arr1: list, arr2: list) -> float:
    '''Return the median of two sorted arrays.
    Array is calcualted as average if there is a tie'''
    # Ot(len(arr1) + len(arr2)), Os(len(arr1) + len(arr2))
    arr_sorted = merge(arr1, arr2)
    # Ot(1), Os(1)
    return get_median(arr_sorted)


def merge(arr1: list, arr2: list) -> list:
    '''Return the sorted merge of arr1 and arr2, both of which are sorted'''
    result = [''] * (len(arr1) + len(arr2))
    i = j = k = 0
    while i <= len(arr1) - 1 and j <= len(arr2) - 1:
        if arr1[i] < arr2[j]:
            result[k] = arr1[i]
            i += 1
        else:
            result[k] = arr2[j]
            j += 1
        k += 1
    # empty out either arr1 or arr2
    while i <= len(arr1) - 1:
        result[k] = arr1[i]
        i += 1
        k += 1
    while j <= len(arr2) - 1:
        result[k] = arr2[j]
        j += 1
        k += 1
    return result


# Ot(1), Os(1)
def get_median(arr_sorted: list) -> float:
    '''Calcualtes and retuns the median of arr_sorted'''
    if len(arr_sorted) % 2 > 0:
        idx = int(len(arr_sorted) / 2)
        return arr_sorted[idx]
    else:
        idx_upper = int(len(arr_sorted) / 2)
        idx_lower = idx_upper - 1
        return (arr_sorted[idx_lower] + arr_sorted[idx_upper]) / 2


def test():
    # Example 1:
    arr1 = [1, 3]
    arr2 = [2]
    # Explanation: merged array = [1,2,3] and median is 2.
    exp = 2.0
    print(median_of_sorted_arrays(arr1, arr2) == exp)

    # Example 2:
    arr1 = [1, 2]
    arr2 = [3, 4]
    # Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
    exp = 2.5
    print(median_of_sorted_arrays(arr1, arr2) == exp)


# run the test
test()