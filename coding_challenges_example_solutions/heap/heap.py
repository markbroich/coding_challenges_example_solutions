# heap class
# Os(n)
# push Ot(log(n))
# pop Ot(log(n))
# peak O(1)

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

items = [5,7,-1,10]
# maxheap
myHeap = Heap(items, min=False)
print('peak', myHeap.peak())
myHeap.push(100)
print(myHeap.pop())
print(myHeap.pop())
print(myHeap.pop())
print(myHeap.pop())
print(myHeap.pop())

# minheap
myHeap = Heap(items, min=True)
print('peak', myHeap.peak())
myHeap.push(100)
print(myHeap.pop())
print(myHeap.pop())
print(myHeap.pop())
print(myHeap.pop())
print(myHeap.pop())




# w inspiration from: 
# https://github.com/joeyajames


# using inbuild (called heapq)
import heapq


# Maxheap (all goes in and comes out as negative as in build is 
# imlemented as minheap) 
items = [5,7,-1,10]
for i in range(0,len(items)):
    items[i] = -items[i]
heapq.heapify(items)
print()
print('peak', -items[0])
heapq.heappush(items,-100)
while items:
    print(-heapq.heappop(items))

# MinHeap (no modification needed)
items = [5,7,-1,10]
heapq.heapify(items)
print()
print('peak', items[0])
heapq.heappush(items,100)
while items:
    print(heapq.heappop(items))






