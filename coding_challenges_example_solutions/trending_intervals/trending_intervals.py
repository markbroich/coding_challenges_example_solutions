"""
Trending Intervals
Problem
Imagine you want to build an application that can visually show popularity trends. 
For a given movie, we are able to get access to a timeperiod’s worth of page-view traffic. 
But the data is sporadic in practice, so we want to be able to smooth it out when 
we’re visualizing it using configurable overlapping intervals
Find Sum
What this looks like in practice is...
([1,3,2,4,6,5], 3) => [6,9,12,15]

"""

# is arr > window?  retrun empty list

# brute forth that gets expensive for large fitler size
# Ot((len(arr)-size)*size) 
# Os(len(arr)-size)
def smoothSum(arr, size=3):
  ret = []
  if len(arr) < size:
    return ret
  
  for i in range(0,len(arr)-size+1):
    mySection = arr[i:i+size]
    ret.append(sum(mySection))
  return ret


# optimizing by adjsuting sum dropping prior value and adding 
# new value at head of filter  
# Ot(size + len(arr)-size) so Ot(len(arr)-size)
# Os(size + len(arr)-size)    
def smoothSumOpt(arr, size=3):
  if len(arr) < size:
    return []
  
  ret = []
  # Ot(size)
  # Os(size)
  mySum = sum(arr[0:size])
  ret.append(mySum)
  
  # Ot(len(arr)-size)
  # Os(len(arr)-size)
  for i in range(1,len(arr)-size+1):
    mySum -= arr[i-1]
    mySum += arr[i+size-1] 
    ret.append(mySum)
  return ret


"""
This customer would like a new representation of the data, and would now like us to report the max value in the sliding window. What that looks like in practice is...
([1,3,2,4,6,5], 3) => [3,4,6,6]
"""

# Ot(n*log(n)) as oppoed to 
# burte forth: Ot((len(arr)-size)*size) 
# Os(len(arr)-size))

import heapq

def smoothMaxOptInbuilt(arr, size=3):
  if len(arr) < size:
    return []
  
  hq = []
  heapq.heapify(hq)
  ret = []
  for i in range(0,size):
    # is set up as minheap so needs -x as inputs
    heapq.heappush(hq,-arr[i])
  ret.append(-hq[0])
  
  for i in range(1,len(arr)-size+1):
    heapq.heappush(hq,-arr[i+size-1])
    # if the item to depart the filter == max, 
    # drop it from the heap
    # return a s -x to use minheap as maxheap
    if arr[i-1] == -hq[0]:
      drop = heapq.heappop(hq)
    # append the max
    # return a s -x to use minheap as maxheap
    ret.append(-hq[0])  

  return ret




# using my own heap
# public methods: push, peak, pop
# private methods: __swap, __floatUp, __bubbleDown
class Heap():
    def __init__(self, items=[], min= True):
        ##
        self.minHeap = min
        self.heap = ['x']
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap)-1)
    # #
    def push(self, num):
        self.heap.append(num)
        self.__floatUp(len(self.heap)-1)
    #
    def peak(self):
        if len(self.heap) > 1:
            return self.heap[1]
    #
    def pop(self):
        if len(self.heap) == 1:
            return False
        elif len(self.heap) == 2:
            return self.heap.pop()
        # swap top w last
        self.__swap(1,len(self.heap)-1)
        # pop last
        ret = self.heap.pop()
        # bubble down top
        self.__bubbleDown(1)
        return ret
    # #
    #
    def __swap(self, i, j):
        self.heap[j], self.heap[i] = self.heap[i], self.heap[j]
    #
    def __floatUp(self, idx):
        parent = idx //2
        if idx <= 1:
            return 
        elif self.minHeap and self.heap[idx] < self.heap[parent]: 
            # is minheap and needs more floating 
            self.__swap(idx, parent)
            self.__floatUp(parent)
        elif not self.minHeap and self.heap[idx] > self.heap[parent]:
            # is maxheap and needs more floating
            self.__swap(idx, parent)
            self.__floatUp(parent)  
        return 
    #
    def __bubbleDown(self, idx):
        idxToSwap = idx
        lc = idx * 2
        rc = idx * 2 + 1
        if len(self.heap) > lc:
            # left child exists and needs bubbeling
            if self.minHeap and self.heap[idxToSwap] > self.heap[lc]:
                idxToSwap = lc
            elif not self.minHeap and self.heap[idxToSwap] < self.heap[lc]:
                idxToSwap = lc
        if len(self.heap) > rc:
            if self.minHeap and self.heap[idxToSwap] > self.heap[rc]:
                idxToSwap = rc
            elif not self.minHeap and self.heap[idxToSwap] < self.heap[rc]:
                idxToSwap = rc
        # if swap is needed
        if idx != idxToSwap:
            self.__swap(idx, idxToSwap)
            self.__bubbleDown(idxToSwap)    


# Ot and Os are the same as for the inbuilt version
# Ot(n*log(n)) as oppoed to 
# burte forth: Ot((len(arr)-size)*size) 
# Os(len(arr)-size))

def smoothMaxOptMyheap(arr, size=3):
  if len(arr) < size:
    return []
  myHeap = Heap(arr[0:size], min=False)

  ret = [myHeap.peak()]
  for i in range(1,len(arr)-size+1):
    myHeap.push(arr[i+size-1])
    # if the item to depart the filter == max, 
    # drop it from the heap
    if arr[i-1] == myHeap.peak():
      drop = myHeap.pop()
    # append the max
    ret.append(myHeap.peak())  

  return ret



########
def testing():
  print('sumtests')
  arr = [1,3,2,4,6,5]
  size = 3
  ex =[6,9,12,15]
  print(smoothSum(arr,size) == ex)
  print(smoothSumOpt(arr, size) == ex)

  arr = [1,3]
  size = 3
  ex =[]
  print(smoothSum(arr,size) == ex)
  print(smoothSumOpt(arr, size) == ex)
  
  arr = [1,1,1]
  size = 3
  ex =[3]
  print(smoothSum(arr,size) == ex)
  print(smoothSumOpt(arr, size) == ex)
  print()
  
  print('maxtest')
  arr = [1,3,2,4,6,5]
  size = 3
  ex = [3,4,6,6]
  print(smoothMaxOptInbuilt(arr, size) == ex)
  print(smoothMaxOptMyheap(arr, size) == ex)

########  
testing()

