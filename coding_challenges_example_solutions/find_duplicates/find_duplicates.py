## Find The Duplicates

# Given two sorted arrays arr1 and arr2 of passport numbers, 
# implement a function findDuplicates that returns an array of all 
# passport numbers that are both in arr1 and arr2. Note that the 
# output array should be sorted in an ascending order.

# Let N and M be the lengths of arr1 and arr2, respectively. 
# Solve for two cases and analyze the time & space complexities 
# of your solutions: M ≈ N - the array lengths are approximately 
# the same M ≫ N - arr2 is much bigger than arr1.

## Example:
# input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]
# output: [3, 6, 7] 


# I assume that there are no duplicates in each array


# Ot(1)
# Os(1)
def find_sh_ln(arr1,arr2):
    if len(arr1) < len(arr2):
        return arr1, arr2
    else:
        return arr2, arr1

# Ot(len(shorter array) + len(longer array))
# Os( len(duplicates))
def find_dubs_two_pnts(arr1, arr2):
    # find shorter and longer
    shorter, longer = find_sh_ln(arr1,arr2)

    resLst = []
    i = j = 0
    while i < len(shorter) and j < len(longer):        
        if shorter[i] == longer[j]:
            resLst.append(shorter[i])
            i += 1
            j += 1
        else:
            j += 1
    
    return resLst



# if the longer array is much longer than the short arr, 
# running an binary search on the long is worthwhile

# Ot(len(shorter) * log(len(longer)))
# Os(len(duplicates))
def find_dubs_binsearch(arr1, arr2):
    resLst = []

    # find shorter and longer
    shorter, longer = find_sh_ln(arr1,arr2)

    for i in range(0,len(shorter)):
        ixd = bi_search(longer, shorter[i])
        if ixd != -1:
            resLst.append(shorter[i])
    return resLst


# O(log(len(arr)))
def bi_search(arr, val):
    lo = 0
    hi = len(arr)-1

    while lo <= hi: 
        mid = int((hi + lo) / 2)
        if arr[mid] == val:
            return mid
        elif arr[mid]  < val:
            lo = mid+1
        else:
            hi = mid-1
    return -1



def testing():
  arr1 = [11]
  arr2 = [11]
  exp = [11]
  print(find_dubs_two_pnts(arr1, arr2) == exp)
  print(find_dubs_binsearch(arr1, arr2) == exp)

  arr1 =[1,3,5,9] 
  arr2 = [2,4,6,10]
  exp = []
  print(find_dubs_two_pnts(arr1, arr2) == exp)
  print(find_dubs_binsearch(arr1, arr2) == exp)

  arr1 = [1,2,3,5,6,7]
  arr2 =  [3,6,7,8,20]
  exp = [3,6,7]
  print(find_dubs_two_pnts(arr1, arr2) == exp)
  print(find_dubs_binsearch(arr1, arr2) == exp)

  arr1 = [1,2,3,5,6,7]
  arr2 =  [7,8,9,10,11,12]
  exp = [7] 
  print(find_dubs_two_pnts(arr1, arr2) == exp)
  print(find_dubs_binsearch(arr1, arr2) == exp)

  arr1 = [10,20,30,40,50,60,70,80]
  arr2 =  [10,20,30,40,50,60]
  exp =  [10,20,30,40,50,60]  
  print(find_dubs_two_pnts(arr1, arr2) == exp)
  print(find_dubs_binsearch(arr1, arr2) == exp)

  arr1 = [10,20,30,40,50,60,70]
  arr2 =  [10,20,30,40,50,60,70]
  exp =  [10,20,30,40,50,60,70]
  print(find_dubs_two_pnts(arr1, arr2) == exp)
  print(find_dubs_binsearch(arr1, arr2) == exp)

testing()
  

