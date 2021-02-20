# Majority Element
# Given an array of size n, find the majority element. 
# The majority element is the element that appears 
# more than floor(n/2) times.

# You may assume that the array is non-empty and the 
# majority element always exist in the array.

# Example :
# Input : [2, 1, 2]
# Return  : 2 which occurs 2 times which is greater than 3/2. 

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# brute forth
# nested loops so for each element count the number of 
# times it occurs and append it to two lists if it occurs 
# more than flood(n/2) times. one list with the element and 
# one list with the occurrence counts.

# Then, pass over the list and find the max occurrence and track 
# the associated element. 

# this would be O(n^2)+O(m) so On^2
# Where m is the length of the list of elements 
# that pass the flood(n/2) threshold


# O(n+m) option using dict so m additional memory
# here m is the number of keys in a dict
nums = [2,2,1,1,1,2,2]

def populate_dict(nums):
    myDict={}
    for i in nums:
        if i in myDict:
            myDict[i] += 1
        else:
            myDict[i] = 1
    return myDict

def find_max(myDict):
    myMaj = myOcc = -999
    for key in myDict:
        if myDict[key] > myOcc:
            myOcc = myDict[key] 
            myMaj = key
    return myMaj, myOcc

def check_condition(myMaj, myOcc, nums):
    if myOcc > int(len(nums)/2):
        return myMaj
    return -1

# main function
def find_maj(nums):
    if not nums:
        return -1
    myDict = populate_dict(nums)
    myMaj, myOcc = find_max(myDict)
    myMaj = check_condition(myMaj, myOcc, nums) 
    return myMaj
# 
print(find_maj(nums))
print()

## Hint for Ot(n) Os(1) solution
# Lets say you find 2 elements x and y which are different in the array. 
# If you removed those 2 elements, would the majority element change ? NO

## Solution approach
# -If we cancel out each occurrence of an element e with all the other 
# elements that are different from e then e will exist till end if 
# it is a majority element. 
# -Loop through each element and maintain a count of the element 
# that has the potential of being the majority element. 
# If next element is same then increments the count, 
# otherwise decrements the count. If the count reaches 0 then 
# update the potential index to the current element and reset count to 1.



# 3 given solution
def majorityElement(A, option=3):
    # Ot(n) but Os(n)
    if option == 1:
        intDict = dict()
        n = len(A)
        for a in A:
            intDict[a] = intDict.get(a,0) + 1
        for key in intDict:
            if intDict[key] > n/2:
                return key
        return -1
    #
    # Ot(nlogn) and O(s(1))
    if option == 2:
        n = len(A)
        if n == 1:
            return A[0]
        A = list(A)
        A.sort()
        return A[int(n/2)]
    #
    # Ot(n) and O(s(1))
    if option == 3:
        majority_idx = 0
        count = 1
        n = len(A)
        for i in range(1,n):
            if A[majority_idx] == A[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                majority_idx = i
                count = 1
        ret = A[majority_idx]
        count = 0
        for a in A:
            if a == ret:
                count += 1
        if count >= n/2:
           return ret
        return -1


print(majorityElement(nums,1))
print(majorityElement(nums,2))
print(majorityElement(nums,3))