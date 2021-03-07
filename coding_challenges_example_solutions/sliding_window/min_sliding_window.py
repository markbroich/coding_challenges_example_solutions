# the brute forth approach is to generate all substrings 

# Given a set of integers, e.g. {1,3,2}, and an array of random integers, e.g. 
#                                   |
# [1, 2, 2, -5, -4, 0, 1, 1, 2, 2, 0, 3,3]
# Find the shortest continuous subarray that contains all of the values from the set. If the subarray can not be found, return an empty array.
# Result: [1, 2, 2, 0, 3]

# between length tArr and length sArr and check which once 
# pass the test and find the shortest

# so for len(sArr) = 10 and len(tArr) = 3
# this would be the following sums of combinations:
# 10!/3!*(10-3)! + 10!/4!*(10-4)! + 10!/5!*(10-5)! +
# 10!/6!*(10-6)! + 10!/7!*(10-7)! + 10!/8!*(10-8)! +
# 10!/9!*(10-9)! + 1 = 968
# so, O(n!)

# e.g. 
tArr = [1,3,2]
sArr = [1, 2, 2, -5, -4, 0, 1, 1, 2, 2]

# calculate number of possible subarrays of sArr with len >= len(tArr)
def fact(n):
    res = 1
    i = 1
    while i <= n:
        res *= i
        i +=1
    return res 

def combination_sum(n, k):
    mySum = 0
    for i in range(k, n+1):
        # summing up combinations of i out of n
        mySum += fact(n) / (fact(i) * fact(n-i))
    return int(mySum)
print('calculate number of possible subarrays of sArr with len '+str(len(sArr))+'>= '+str(len(tArr))+'(len(tArr)):')
print(combination_sum(10,3))
print()


# Ot(n) Os(n) solution: 
# 1) move right pointer until subarr contains all of tArr
# 2) note result if shorter than prior
# 3) while subarr contains all of tArr, 
#    move left pointer
# 4) go back to #1. 
# 5) return shortest subarr containing all of tArr
# 
def find_shortest_sub_On(tArr, sArr):
    countT, countSub = {}, {}
    # populate countT
    for c in tArr:
        countT[c] = 1 + countT.get(c,0)
    
    resLen = float("infinity")
    resL = resR = -1
    l = r = matchCount = 0

    # move right index to expand subarr
    for r in range(0, len(sArr)):
        c = sArr[r]
        if c in countT:
            countSub[c] = 1 + countSub.get(c,0)
            if countSub[c] == countT[c]:
                matchCount += 1
        # move left index to shrink subarr
        while matchCount == len(countT):
            # update result if shorter
            if r-l+1 < resLen:
                resLen = r-l+1
                resL = l
                resR = r
            # 
            c = sArr[l]
            if c in countT:
                countSub[c] -= 1
                if countSub[c] < countT[c]:
                    matchCount -= 1
            l +=1 
    if resLen == float("infinity"):
        return -1
    else: 
        return sArr[resL:resR+1]

# sample data
tArr = [1,3,2]
sArr = [1, 2, 2, -5, -4, 0, 1, 1, 2, 2, 0, 3,3]

print(find_shortest_sub_On(tArr, sArr))

#
## O(n^2) for min length of tArr > 1
#
def compare_dicts(tDict, sDict):
    if len(tDict) == len(sDict):
        for key in tDict:
            if sDict[key] < tDict[key]:
                return False
        return True
    return False
#
def find_shortest_sub_Onsquared(tArr,sArr):
    # populate tDict
    tDict = {}
    for i in range(0,len(tArr)):
        tDict[tArr[i]] = 1 + tDict.get(tArr[i],0)  
    #
    minL = 9999
    iSt = iEn = 0
    for i in range(0,len(sArr)):
        sDict = {}
        if sArr[i] in tDict:
            sDict[sArr[i]] = 1 + sDict.get(sArr[i],1)  
        #
        for j in range(i,len(sArr)):
            if sArr[j] in tDict:
                sDict[sArr[j]] = 1 + sDict.get(sArr[j],0) 
                if compare_dicts(tDict, sDict):
                    if minL > j-i+1:
                        minL = j-i+1
                        iSt = i
                        iEn = j
    if minL == 9999:
        return -1 
    return sArr[iSt: iEn+1]
#


print(find_shortest_sub_Onsquared(tArr,sArr))

# w inspiration from:
# https://leetcode.com/problems/minimum-window-substring/discuss/1085584/O(n)-Solution-with-Detailed-Explanation


