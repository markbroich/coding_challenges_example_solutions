## A different version w a few extra rules

## Given an array A of integers, find the index of values that satisfy A + B = C + D, where A,B,C & D are integers values in the array

# 1) Return the indices `A1 B1 C1 D1`, so that 
#   A[A1] + A[B1] = A[C1] + A[D1]
#   A1 < B1, C1 < D1
#   A1 < C1, B1 != D1, B1 != C1 

# 2) If there are more than one solutions, 
#    then return the tuple of values which are lexicographical smallest. 

# Assume we have two solutions
# S1 : A1 B1 C1 D1 ( these are values of indices int the array )  
# S2 : A2 B2 C2 D2

# S1 is lexicographically smaller than S2 iff
#   A1 < A2 OR
#   A1 = A2 AND B1 < B2 OR
#   A1 = A2 AND B1 = B2 AND C1 < C2 OR 
#   A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2
# Example:

# Input: [3, 4, 7, 1, 2, 9, 8]
# Output: [0, 2, 3, 5] (O index)
# If no solution is possible, return an empty list.


# O(n^2 + length(d) * klogk) where d is the length 
# of the dict and k is the length of the average list of 
# quats per dict key. 
#  so O(n^2)

def fillDict(arr):
    myDict = {}
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            res = arr[i] + arr[j] # i**3 + j**3
            if (res in myDict):
                myDict[res] = [myDict[res][0], myDict[res][1], i, j]
            else:
                myDict[res] = [i, j]
    return myDict


def printRes(myDict):
    for res in myDict:
        resList = []
        for i in range(0,len(myDict[res]),2): 
            ia = myDict[res][i]
            ib = myDict[res][i+1]
            for j in range(2,len(myDict[res]),2): 
                ic = myDict[res][j]
                id = myDict[res][j+1]
                if ib != id and ib != ic:
                    resList.append(str(ia)+"_"+str(ib)+"_"+str(ic)+"_"+str(id)+"_:_"+str(res))
        if len(resList) > 1:
            reslist = sorted(resList)
        if resList:
            print(resList[0])

# 
def my_run(arr):
    myDict = fillDict(arr)
    printRes(myDict)

arr = [3, 4, 7, 1, 2, 9, 8]
my_run(arr)
