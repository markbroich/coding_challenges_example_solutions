from random import randint

'''
Sort Colors
Given an array nums with n objects colored red, white, or blue, 
[sort them in-place] 
    so that objects of the same color are adjacent, with the 
colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]

Ot(n) one pass, Os(1)
'''

def sort_3_inplace(nums):
    if len(nums) == 0:
        return -1
    l = i = 0
    r = len(nums) - 1
    while i < r: 
        if nums[i] == 0:
            nums[l], nums[i] = nums[i], nums[l]
            l += 1
            i += 1 
        elif nums[i] == 2:
            nums[r], nums[i] = nums[i], nums[r]   
            r -= 1
        else:
            i += 1
    return nums

nums = [2,2,0,1,1,0]
print(sort_3_inplace(nums))

nums = [2,2,0,1,1,0]
print(sort_3_inplace(nums))

nums = [randint(0,2) for i in range(20)]
print(sort_3_inplace(nums))