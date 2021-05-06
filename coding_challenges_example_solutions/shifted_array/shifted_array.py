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
        mid = int((hi-lo)/2)+lo  
        if shiftArr[mid]== num: 
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
            if num > shiftArr[mid] and num <=shiftArr[hi]:
                lo = mid 
            else: # num must be in left
                hi = mid

    # shiftArr between lo and hi now has len ==2
    if shiftArr[lo] == num:
        return lo
    if shiftArr[hi] == num:
        return hi
    
    return -1


def testing():
    shiftArr = [2]
    num = 2
    expected = 0
    print(shifted_arr_search(shiftArr, num) == expected)
    
    shiftArr = [1,2]
    num = 2
    expected = 1
    print(shifted_arr_search(shiftArr, num) == expected)

    shiftArr = [0,1,2,3,4,5]
    num = 1
    expected = 1
    print(shifted_arr_search(shiftArr, num) == expected)

    shiftArr = [9,12,17,2,4,5]
    num = 17
    expected = 2
    print(shifted_arr_search(shiftArr, num) == expected)

    shiftArr = [9,12,17,2,4,5]
    num = 2
    expected = 3
    print(shifted_arr_search(shiftArr, num) == expected)

    shiftArr = [9,12,17,2,4,5,6]
    num = 4
    expected = 4
    print(shifted_arr_search(shiftArr, num) == expected)

    shiftArr = [17,2,4,5,9,12]
    num = 2
    expected = 1
    print(shifted_arr_search(shiftArr, num) == expected)

    shiftArr = [17,2,4,5,99,12]
    num = 2
    expected = 1
    print(shifted_arr_search(shiftArr, num) == expected)

    shiftArr = [1,2,3,4,5,0]
    num = 0
    expected = 5
    print(shifted_arr_search(shiftArr, num) == expected)
 

testing()



 


