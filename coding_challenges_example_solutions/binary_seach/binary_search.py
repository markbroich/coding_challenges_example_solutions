# write a binary search algo

# example:
arr = [i for i in range(1,101)]

# only prints found or not found and returns 1 or -1
def bin_search(arr,elem):
    if len(arr)==1:
        if arr[0] == elem:
            print('found')
            return 1
        else:
            print('not found')
            return -1
    else:
        mid = int(len(arr)/2)
        if elem < arr[mid]:
            arr = bin_search(arr[:mid],elem)
        else:
            arr = bin_search(arr[mid:],elem)

elem = 23
bin_search(arr,elem)
elem = 233
bin_search(arr,elem)
print('')


#  prints found or not found and returns index or -1
def bin_search_index(arr,elem):
    start = 0
    end = len(arr)-1
    while (start<= end):
        mid =int((start+end)/2)
        if (elem>arr[mid]):
            start = mid+1
        elif (elem<arr[mid]):
            end = mid-1
        elif (elem == arr[mid]):
            print('found at index: ', mid)
            return mid
    print('not found')
    return -1
	

elem = 23
print('bin_search_index')
index = bin_search_index(arr,elem)
print(index)
print('')

elem = 233
print('bin_search_index')
index = bin_search_index(arr,elem)
print(index)