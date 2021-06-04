## Shifted Array Search

# A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset 
# and you don’t have a pre-shifted copy of it. For instance, the sequence 1, 2, 3, 4, 5 
# becomes 3, 4, 5, 1, 2, after shifting it twice to the left.

# Given shiftArr and an integer num, implement a function shiftedArrSearch 
# that finds and returns the index of num in shiftArr. If num isn’t in shiftArr, 
# return -1. Assume that the offset can be any value between 0 and arr.length - 1.

# Explain your solution and analyze its time and space complexities.

# Example:

# input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
#                                                  # outcome of shifting
#                                                  # [2, 4, 5, 9, 12, 17]
#                                                  # three times to the left

# output: 3.  since it’s the index of 2 in arr


# brute forth is Ot(n)

# for a better solution using binary search (Ot(logn), Os(1)):
# need to ask if arr prior to shift was sorted

def shifted_arr_search(shiftArr, num):
    if not shiftArr:
        return -1

    if len(shiftArr) == 1:
        if shiftArr[0] == num:
            return 0
        else:
            return -1

    # binary search
    lo = 0
    hi = len(shiftArr)-1
    # while remaining section of arr longer 2
    while lo+1 < hi:
        mid = int((hi+lo)/2)
        if shiftArr[mid] == num:
            return mid

        # if left is sortred
        if shiftArr[lo] < shiftArr[mid]:
            # if num in left
            if num >= shiftArr[lo] and num < shiftArr[mid]:
                hi = mid
            else: # num must be in right
                lo = mid
        else: # right is sorted
            # if num in right
            if num > shiftArr[mid] and num <= shiftArr[hi]:
                lo = mid
            else: # num must be in left
                hi = mid

    # shiftArr between lo and hi now has len ==2
    if shiftArr[lo] == num:
        return lo
    if shiftArr[hi] == num:
        return hi
    
    return -1

#### a different implementation

def shifted_arr_search_other_imp(arr, num):
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        if arr[0] == num:
            return 0
        elif arr[1] == num:
            return 1
        else:
            return -1
    #
    pivot = bin_search_pp(arr)
    if not pivot == -1:
        lo, hi = get_hi_low(arr, pivot, num)
    else:
        lo = 0
        hi = len(arr)-1
    return bin_search(arr, num, lo, hi)


def bin_search_pp(arr):
    lo = 0
    hi = len(arr)-1
    while lo <=hi:
        mid = int((lo+hi)/2)     
        if arr[mid] < arr[mid-1]:
            # if pivot point
            return mid
        elif arr[0] < arr[mid]:
            # if right isde is sorted
            lo = mid+1
        elif arr[mid] < arr[len(arr)-1]:
            # if left side is sorted
            hi = mid
    return -1

def get_hi_low(arr, pivot, num):
    # find which section of arr num is in
    lo = 0
    hi = len(arr)-1
    if num >= arr[lo] and num <= arr[pivot-1]:
        hi = pivot-1
    elif num >= arr[pivot] and num <= arr[hi]:
        lo = pivot
    return lo, hi
    
def bin_search(arr, num, lo, hi):
    while lo <=hi:
        mid = int((lo+hi)/2)
        if arr[mid] == num:
            return mid
        elif mid < num:
            lo = mid+1
        else:
            hi = mid -1
    return -1


def testing():
    shiftArr = [2]
    num = 2
    expected = 0
    print(shifted_arr_search(shiftArr, num) == expected)
    print(shifted_arr_search_other_imp(shiftArr, num) == expected)
    
    shiftArr = [1,2]
    num = 2
    expected = 1
    print(shifted_arr_search(shiftArr, num) == expected)
    print(shifted_arr_search_other_imp(shiftArr, num) == expected)

    shiftArr = [0,1,2,3,4,5]
    num = 1
    expected = 1
    print(shifted_arr_search(shiftArr, num) == expected)
    print(shifted_arr_search_other_imp(shiftArr, num) == expected)

    shiftArr = [9,12,17,2,4,5]
    num = 17
    expected = 2
    print(shifted_arr_search(shiftArr, num) == expected)
    print(shifted_arr_search_other_imp(shiftArr, num) == expected)

    shiftArr = [9,12,17,2,4,5]
    num = 2
    expected = 3
    print(shifted_arr_search(shiftArr, num) == expected)
    print(shifted_arr_search_other_imp(shiftArr, num) == expected)

    shiftArr = [9,12,17,2,4,5,6]
    num = 4
    expected = 4
    print(shifted_arr_search(shiftArr, num) == expected)
    print(shifted_arr_search_other_imp(shiftArr, num) == expected)

    shiftArr = [17,2,4,5,9,12]
    num = 2
    expected = 1
    print(shifted_arr_search(shiftArr, num) == expected)
    print(shifted_arr_search_other_imp(shiftArr, num) == expected)

    shiftArr = [17,2,4,5,99,12]
    num = 2
    expected = 1
    print(shifted_arr_search(shiftArr, num) == expected)
    print(shifted_arr_search_other_imp(shiftArr, num) == expected)

    shiftArr = [1,2,3,4,5,0]
    num = 0
    expected = 5
    print(shifted_arr_search(shiftArr, num) == expected)
    print(shifted_arr_search_other_imp(shiftArr, num) == expected)

testing()



 


