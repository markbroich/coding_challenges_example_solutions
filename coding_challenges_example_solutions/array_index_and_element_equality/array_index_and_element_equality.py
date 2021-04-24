## Array Index & Element Equality

# Given a sorted array arr of distinct integers, write a function 
# indexEqualsValueSearch that returns the lowest index i for 
# which arr[i] == i. Return -1 if there is no such index. 
# 
# Analyze the time and space complexities of your solution and explain its correctness.


# Examples:

# input: arr = [-8,0,2,5]
# output: 2 # since arr[2] == 2

# input: arr = [-1,0,3,6]
# output: -1 # since no index in arr satisfies arr[i] == i.


# Approach is binary search on the logic that:
# if index < arr[index], a match can only be left
# if index > arr[index], a match can only be right

# Ot(log(n))
# Os(n)
def index_equals_value_search_mine(arr, offset=0, minmatch=float('inf')):
  mid = int(len(arr)/2)
  if len(arr) == 1:
    if offset+mid == arr[0]:
        return min(offset+mid, minmatch)
    elif offset+mid != arr[0]:
      return -1
      
  elif offset+mid == arr[mid]:
    minmatch = min(offset+mid, minmatch)
    return index_equals_value_search_mine(arr[0:mid], offset, minmatch)
  
  elif offset + mid < arr[mid]:
     # look left
     return index_equals_value_search_mine(arr[0:mid], offset, minmatch)
  else:
    # look right
    return index_equals_value_search_mine(arr[mid+1:len(arr)], offset+mid+1, minmatch)
      
# Ot(log(n))
# Os(n)
def index_equals_value_search_tuned(arr, offset=0):
  mid = int(len(arr)/2)
  if len(arr) == 1:
    if offset+mid == arr[0]:
        return offset + mid
    else:
      return -1
  
  elif offset + mid > arr[mid]:
    # look right
    return index_equals_value_search_tuned(arr[mid+1:len(arr)], offset+mid+1)

  # if match and index left is > arr left, so
  # no match to left possible
  elif offset+mid == arr[mid] and offset+mid-1 > arr[mid-1]:
    return offset+mid
    
  else:  
    # look left
    return index_equals_value_search_tuned(arr[0:mid], offset)


# solution provided by pramp: 
# Ot(log(n))
# Os(1)
def index_equals_value_search_pr(arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        i = int((start+end)/2)
        if arr[i] - i < 0:
            start = i+1
        elif arr[i] - i == 0 and (i == 0 or arr[i-1] - (i-1) < 0):
            return i
        else:
            end = i-1

    return -1


def testing():
    arr = [0]
    print(index_equals_value_search_mine(arr) == 0)
    print(index_equals_value_search_tuned(arr) == 0)
    print(index_equals_value_search_pr(arr) == 0)

    arr = [0,3]
    print(index_equals_value_search_mine(arr) == 0)
    print(index_equals_value_search_tuned(arr) == 0)
    print(index_equals_value_search_pr(arr) == 0)

    arr = [-8,0,1,3,5]
    print(index_equals_value_search_mine(arr) == 3)
    print(index_equals_value_search_tuned(arr) == 3)
    print(index_equals_value_search_pr(arr) == 3)

    arr = [-5,0,2,3,10,29]
    print(index_equals_value_search_mine(arr) == 2)
    print(index_equals_value_search_tuned(arr) == 2)
    print(index_equals_value_search_pr(arr) == 2)

    arr = [-5,0,3,4,10,18,27]
    print(index_equals_value_search_mine(arr) == -1)
    print(index_equals_value_search_tuned(arr) == -1)
    print(index_equals_value_search_pr(arr) == -1)

    arr = [-6,-5,-4,-1,1,3,5,7]
    print(index_equals_value_search_mine(arr) == 7)
    print(index_equals_value_search_tuned(arr) == 7)
    print(index_equals_value_search_pr(arr) == 7)

testing()

# challenge by pramp