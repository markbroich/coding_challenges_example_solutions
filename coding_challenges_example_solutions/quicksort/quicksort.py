# quickSort: 

# O(n log n) time complexity given:
#  n elements * log(n) partitioning levels

# space O(1) 'in place'

# Inner workings: we pick a pivot element
# the crux is that we move all elements < pivot 
# to the left and all all elements < pivot to the right
# then we no longer need to compare left of pivot w right
# of pivot and have hence ~halfed the remaining problem 
# this is where the log(n) comes from. 
# we then recursively call the algo on left and right of the pivot, 
# respectivley. 

# Pivot choice issue: pivot first or last can cause O(n^2) time if array is already sorted 
# (or reverse sorted). 
# random pivot implementation to avoid O(n^2)

 
# Specifically, this function takes last or random element as pivot, 
# places all elements smaller than pivot before
# pivot and all greater after pivot. 
# Then moves pivot into correct position. 
# Lastly, recursively calls quickSort on
# before and after pivot part of array
 
# location of sorting action
def partition(arr, low, high, pi):
    i = (low-1) # index of next element in list > pivot
    for j in range(low, high):
        if arr[j] <= pi:
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    # move pivot into correct slot
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1, arr

# pickPivot. simple but non ideal case is:
# pi = arr[high] 
def pickPivot(arr, low, high, highP=False):
    # either use high point as pivot
    # or pick an random pivot
    if highP:
        pi = arr[high]     
    else: 
        indexPi = random.randint(low,high)
        pi = arr[indexPi]  
        arr[indexPi], arr[high] = arr[high], arr[indexPi]
    return pi, arr

# quickSort her majesty 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi, arr = pickPivot(arr, low, high)
        pi, arr = partition(arr, low, high, pi)
        # recursive call on arr before and after pivot
        arr = quickSort(arr, low, pi-1)
        arr = quickSort(arr, pi+1, high)
    return arr


# run the code
import random
arr = [101, 5, 87, 7, 9, -1, 3]
n = len(arr)
print("Sorted array in place: ", quickSort(arr, 0, n-1))

#####
# quickSort with space O(n)
def quickSortOutOfPlace(arr):
    if len(arr) <= 1:
        return arr
    # mid-point pivot
    pi = arr[int(len(arr)/2)]
    left = [x for x in arr if x < pi]
    mid = [x for x in arr if x == pi]
    right = [x for x in arr if x > pi]
    return quickSortOutOfPlace(left)+mid+quickSortOutOfPlace(right)

# run the code
arr = [101, 5, 87, 7, 9, -1, 3]
print("Sorted array out of place: ", quickSortOutOfPlace(arr))

