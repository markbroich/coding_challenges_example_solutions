'''
Given an iterator of iterators, implement an interleaving iterator

Background: Iterator defined

In object-oriented programming, the iterator pattern is a design pattern
in which an iterator is used to traverse a container and access the
container's elements. The iterator pattern decouples algorithms from
containers; in some cases, algorithms are necessarily container-specific
and thus cannot be decoupled. This code snippet illustrates:


int[] arr = [1, 2, 3];
Iterator<Integer> it = arr.iterator();
while(it.hasNext()){
  print it.next();
}
// 123
hasNext() // returns whether or not the iterator has additional elements
next() // returns next element in iterator, throws NoSuchElementException
otherwise.


Your challenge, should you choose to accept it...

Given an iterator of iterators, implement an interleaving iterator that takes
in an iterator of iterators, and emits elements from the nested iterators in
interleaved order. That is, if we had the iterators i and j iterating over the
elements [ia, ib, ic] and [ja, jb] respectively, the order in which your
interleaving iterator should emit the elements would be [ia, ja, ib, jb, ic].

Your interleaving iterator should implement the Iterator interface, take in
the iterator of iterators in its constructor, and provide the next and hasNext
methods. Assume that there are no additional methods offered by the iterator.

Given the following three iterators put into an array of iterators…

arr1 = [1, 2, 3]
arr2 = [4, 5]
arr3 = [6, 7, 8, 9]

exp = [1, 4, 6, 2, 5, 7, 3, 8, 9]
'''

import collections


class my_iter:
    # Ot(1) Os(1)
    def __init__(self, arr):
        self.index = 0
        self.length = len(arr)

    # Ot(1) Os(1)
    def hasnext(self):
        if self.index < self.length:
            return True
        return False

    # Ot(1) Os(1)
    def next(self):
        result = self.index
        self.index += 1
        return result


class Interleaving_Flattener:
    # init Ot(k) Os(k) where k is number of arrays.
    def __init__(self, iter_list):
        self.my_iter_dict = {}
        self.queue = collections.deque()
        for key in range(0, len(iter_list)):
            arr = iter_list[key]
            if len(arr) > 0:
                self.my_iter_dict[key] = my_iter(arr)
                self.queue.append(key)

    # flattern Ot(x) Os(x) where x is sum of all input list length
    def flattern(self, iter_list):
        result = []
        while self.queue:
            key = self.queue.popleft()
            my_iter = self.my_iter_dict[key]
            if my_iter.hasnext():
                idx_next = my_iter.next()
                result.append(iter_list[key][idx_next])
                self.queue.append(key)
            else:
                del self.my_iter_dict[key]
        return result


def tests():
    arr1 = [1, 2, 3]
    arr2 = [4, 5]
    arr3 = [6, 7, 8, 9]
    exp = [1, 4, 6, 2, 5, 7, 3, 8, 9]
    iter_list = [arr1, arr2, arr3]
    interleaving_flattener = Interleaving_Flattener(iter_list)
    print(interleaving_flattener.flattern(iter_list) == exp)

    arr1 = [1, 2, 3]
    arr2 = [4]
    arr3 = [6, 7, 8, 9]
    exp = [1, 4, 6, 2, 7, 3, 8, 9]
    iter_list = [arr1, arr2, arr3]
    interleaving_flattener = Interleaving_Flattener(iter_list)
    print(interleaving_flattener.flattern(iter_list) == exp)

    arr1 = [1, 2, 3]
    arr2 = []
    arr3 = [6, 7, 8, 9]
    exp = [1, 6, 2, 7, 3, 8, 9]
    iter_list = [arr1, arr2, arr3]
    interleaving_flattener = Interleaving_Flattener(iter_list)

    arr1 = []
    arr2 = [4, 5]
    arr3 = [6, 7, 8, 9]
    exp = [4, 6, 5, 7, 8, 9]
    iter_list = [arr1, arr2, arr3]
    interleaving_flattener = Interleaving_Flattener(iter_list)
    print(interleaving_flattener.flattern(iter_list) == exp)

    arr1 = []
    arr2 = []
    arr3 = [6, 7, 8, 9]
    exp = [6, 7, 8, 9]
    iter_list = [arr1, arr2, arr3]
    interleaving_flattener = Interleaving_Flattener(iter_list)
    print(interleaving_flattener.flattern(iter_list) == exp)

    arr1 = []
    arr2 = []
    arr3 = []
    exp = []
    iter_list = [arr1, arr2, arr3]
    interleaving_flattener = Interleaving_Flattener(iter_list)
    print(interleaving_flattener.flattern(iter_list) == exp)

    arr1 = [1, 2, 3]
    arr2 = [4, 5]
    arr3 = [6, 7, 8, 9]
    arr4 = [10, 11]
    arr5 = [12, 13, 14, 15]
    exp = [1, 4, 6, 10, 12, 2, 5, 7, 11, 13, 3, 8, 14, 9, 15]
    iter_list = [arr1, arr2, arr3, arr4, arr5]
    interleaving_flattener = Interleaving_Flattener(iter_list)
    print(interleaving_flattener.flattern(iter_list) == exp)


tests()

# alternative approach: https://stackoverflow.com/questions/1966591/has-next-in-python-iterators
