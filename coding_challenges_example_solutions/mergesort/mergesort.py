# Mergesort 

# time complexity is O(n log(n)): 
# given that each merge step touches each of n items (so O(n))
# and we do log(n) merge steps (so, O(n * log(n)) 
# space complexity is O(n) as we copy all items 

# while space complexity is > quicksort, parallelization of mergesort
# is relatively easy (e.g. https://gist.github.com/stephenmcd/39ded69946155930c347 )

# assumptions I am making here: 
# only numbers
# no NA
# can fit in memory
# small enough that multi-threading is not beneficial

# e.g. arr = [9,3,1,-20,100,20,19]


# input into the merge function are two sorted arrays. return is 
# the two inputs sorted together

# merge has O(n) 
def merge(left, right):  
    # init result array and pointers
    sorted_arr = [""] * (len(left) + len(right))
    i = j = k = 0
    # while there are still fresh values in left and right
    while i < len(left) and j < len(left):
        if left[i] <= right[j]:
            sorted_arr[k] = left[i]
            i += 1
        else: 
            sorted_arr[k] = right[j]
            j += 1
        k += 1
    # deal with what remaining values in left or right 
    while i < len(left):
        sorted_arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        sorted_arr[k] = right[j]
        j += 1
        k += 1
    #
    return sorted_arr


# recursive function that takes in an unsorted array and 
# returns a sorted array after calling itself and the merge function
# O(n 'for merge as n elements are merged' * log(n) 'for splitting as array is halved w every split' )
def merge_sort(arr):
    # recursion base case
    if len(arr) <= 1:
        return arr
    else:
        # start of slitting 
        # splitting has O(log(n))
        mid = int(len(arr)/2)
        left = arr[:mid]
        right = arr[mid:]
        # recursive calls
        left = merge_sort(left)
        right = merge_sort(right)
        # end of slitting 
        #
        # merge call has O(n) 
        return merge(left, right) 


# create_random_number_array
def create_random_number_array(size=10, min=-100, max=100):
    from random import randint
    return [randint(min,max) for _ in range(size)]


# bubbleSort as a benchmark (O(n^2) time with O(1) space)
# e.g.( https://www.geeksforgeeks.org/python-program-for-bubble-sort/ )
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(0, n): 
        for j in range(0, n-1):     
        # for j in range(0, n-i-1): # Last i elements are already in place but still O(n^2) even if we exclude them when advancing i
            # Swap if the element found is greater 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
  



def main():
    print("testing the creation for 10 random numbers: ")
    print(create_random_number_array(size=10, min=0, max=10))
    print("")
    #
    print("testing the merge function: ")
    left = [1,2,4,9]
    right = [3,10]
    print("input sorted left: ", left, " and right: ", right)
    print("result of sorting left and right together: ")
    print(merge(left, right))
    print("")
    #
    print("testing mergesort: ")
    arr = [9,3,1,20,100,-20,19]
    print("unsorted input: ", arr)
    print(merge_sort(arr))
    print("")
    #
    print("timing mergesort and bubblesort w increasing array size: ")
    n = [10,100,1000,10000]
    times = [""]*len(n)
    from time import time
    for i in range(0,len(n)):
        size = n[i] 
        arr = create_random_number_array(size=size, min=-10000, max=100000)
        t0 = time(); merge_sort(arr); t1 = time()
        times[i] = [(t1-t0),""]
        t0 = time(); bubbleSort(arr); t1 = time()
        times[i][1] = t1-t0
    #
    print ("size | secs mergesort | secs bubblesort ")
    for i in range(len(n)):
        print('{:6}'.format(n[i]), "| ", "{:.5f}".format(times[i][0]), "| ", "{:.5f}".format(times[i][1]))
    print("")
    print("the O(n log(n)) 'effect' of mergesort vs O(n^2) of bubble becomes more obvious with inceasing array size")

if __name__ == "__main__":
    main()