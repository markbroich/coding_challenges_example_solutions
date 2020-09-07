# binary search tree 
# class with insert, find, 
# expanded from: 
# https://www.tutorialspoint.com/python_data_structure/python_binary_search_tree.htm
# also methods to delete, inorder transversal and insert count of nodes below a node + 1

# purpose: fast inset into sorted and fast retrival
# space O(n) where n is element count
# time O(log(n)) for each find and insert, where n is element count
# or O(k) where k is tree depth
#
# inorder transversal is O(n) where n is the node (value) count 

# Last addition: is to return the value of node given an index
# the motivation is to provide a random index to get a random node value w O(log(n)) time complexity
# one way would be to do an inorder travelsal, write the result to
# and array and sample the array. this would have time and space O(n) and where n is element count
# the retNode_at_index method returns a node given a random index with O(log(n)) time 
# and O(1) space (assuming that insertNodecount has already been run 
# (insertNodecount inserts nodecounts with O(2^k) time where k is tree depth) and O(n) space, where n is the nodecount. 
 



class Node:
    def __init__(self, data):
        self._left = None
        self._right = None
        self._data = data
        # count of child nodes + 1 (for self)
        self._count = None 
        
    # Insert method to create nodes
    def insert(self, data):
        if self._data:
            if data < self._data:
                if self._left is None:
                    self._left = Node(data)
                else:
                    self._left.insert(data)
            elif data > self._data:
                if self._right is None:
                    self._right = Node(data)
                else:
                    self._right.insert(data)
        else:
            self._data = data
        
    # findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self._data:
            if self._left is None:
                return str(lkpval)+" Not Found"
            return self._left.findval(lkpval)
        elif lkpval > self._data:
            if self._right is None:
                return str(lkpval)+" Not Found"
            return self._right.findval(lkpval)
        else:
            return str(self._data) + ' is found'

    # Given a non-empty binary search tree, return the node 
    # with minimum data value found in that tree. Note that the 
    # entire tree does not need to be searched  
    def __minValueNode(self): 
        if self._data == None:
            return "substree is empty" 
        elif self._left == None:
            return self
        else:
            return self._left.self.__minValueNode()
        # or as loop when passed a node
        # current = node
        # # loop down to find the leftmost leaf 
        # while(current._left is not None): 
        #     current = current._left  
        # return current  
    
    # Given a binary search tree and a data value, this function delete the data value and returns the new root 
    def deleteNode(self, data): 
        # Base Case 
        if self._data is None: # if tree is empty
            print(str(data)+" Not Found, and tree is empty")
        # If the data to be deleted is smaller than the self's data then it lies in  left subtree 
        if data < self._data:
            if self._left is not None: 
                self._left = self._left.deleteNode(data) # recursion
            else: 
                print(str(data)+" Not Found")
        # If the data to be delete is greater than the self's data then it lies in right subtree 
        elif(data > self._data):
            if self._right is not None: 
                self._right = self._right.deleteNode(data) # recursion
            else: 
                print(str(data)+" Not Found")
        # If data is same as self's data, then this is the node to be deleted 
        else: 
            # Node with only one child or no child 
            if self._left is None : 
                temp = self._right  
                self = None 
                return temp  
            elif self._right is None : 
                temp = self._left  
                self = None
                return temp 
            # Node with two children: Get the inorder successor (smallest in the right subtree) 
            temp = self._right.__minValueNode()  
            # Copy the inorder successor's content to this node 
            self._data = temp._data 
            # Delete the inorder successor 
            self._right = self._right.deleteNode(temp._data) # recursion
        return self  
    
    # Print the tree inorder (so left, root, right starting from leftmost)
    def Inorder(self):
        if self._data == None:
            print('empty tree')
        else:     
            if self._left:
                self._left.Inorder()
            print( self._data),
            if self._right:
                self._right.Inorder()
    
    # return the nodecount
    def retcount(self, anode):
        if anode == None:
            return 0
        return anode._count
    
    # count nodes attached to node +1
    def __nodecount(self): # O(2^k) where k is tree depth
        if self == None: 
            return 0
        if self._left != None and self._right != None:
            return self._left.__nodecount() + self._right.__nodecount() + 1
        elif self._left != None and self._right == None:
            return self._left.__nodecount() + 1
        elif self._left == None and self._right != None:
            return self._right.__nodecount() + 1
        else:
            return 1
    
    # insert nodecount 
    def insertNodecount(self): # O(2^k) where k is tree depth
        if self == None:
            return
        self._count = self.__nodecount()
        if self._left != None:
            self._left.insertNodecount()
        if self._right != None:    
            self._right.insertNodecount()

    def retNode_at_index(self, index):
        if self == None:
            return 'empty tree'
        elif index == self.retcount(self._left):
            return self._data
        elif index < self.retcount(self._left):
            return self._left.retNode_at_index(index)
        return self._right.retNode_at_index(index - self.retcount(self._left) - 1)



# driving the class
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(5)
root.insert(18)
root.insert(13)
print(root.findval(7))
print(root.findval(14))
root.Inorder()
print("")

print('node count head old: ')
print(root._count)
root.insertNodecount()
print('node count head new: ')
print(root._count)

print("del node 3")
root.deleteNode(3)
root.Inorder()
print("")

print("del node 6")
root.deleteNode(6)
print("")
root.Inorder()
print("")

print("del node 14")
root.deleteNode(14)
print("")
root.Inorder()
print("")

print("del node 100")
root.deleteNode(100)
print("")
root.Inorder()
print("")

print('node count head old: ')
print(root.retcount(root))
root.insertNodecount()
print('node count head new: ')
print(root.retcount(root))

# directly accessing private variables for testing
print('node count head right old: ')
print(root.retcount(root._right))
root.insertNodecount()
print('node count head right new: ')
print(root.retcount(root._right))

print('node count head left old: ')
print(root.retcount(root._left))
root.insertNodecount()
print('node head left new: ')
print(root.retcount(root._left))


print("")
root.Inorder()
print("")
print("retrun count root")
print(root.retcount(root))
print("loop over the indices 0 to ")
for i in range(0,root.retcount(root)):
    print("return index ",i)
    print(root.retNode_at_index(i))
print("the above is the same as Inorder result, so working \n")

print("return random node value with O(log(n)) where n is the nodecount")
from random import randint
rand_nodeindex = (randint(0,root.retcount(root)-1))
print(root.retNode_at_index(rand_nodeindex))