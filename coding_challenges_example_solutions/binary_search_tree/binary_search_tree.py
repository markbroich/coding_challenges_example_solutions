# binary search tree 
# class with insert, find, delete and inorder transversal

# expanded from: 
# https://www.tutorialspoint.com/python_data_structure/python_binary_search_tree.htm

# purpose: fast inset into sorted and fast retrival
# space O(n) where n is element count
# time O(log(n)) for each find and insert, where n is element count
# or O(k) where k is tree depth


class Node:
    def __init__(self, data):
        self._left = None
        self._right = None
        self._data = data
        
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
    def minValueNode(self): 
        if self._data == None:
            return "substree is empty" 
        elif self._left == None:
            return self
        else:
            return self._left.self.minValueNode()
        # or as loop when passed a node
        # current = node
        # # loop down to find the leftmost leaf 
        # while(current._left is not None): 
        #     current = current._left  
        # return current  
    
    #
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
            temp = self._right.minValueNode()  
            # Copy the inorder successor's content to this node 
            self._data = temp._data 
            # Delete the inorder successor 
            self._right = self._right.deleteNode(temp._data) # recursion
        return self  
    
    # Print the tree inorder (so left, root, right starting from leftmost)
    def Inorder(self):
        if self._data == None:
        else:     
            if self._left:
                self._left.Inorder()
            print( self._data),
            if self._right:
                self._right.Inorder()
    

    # 


# driving the class
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(5)
root.insert(18)
root.insert(13)
print("")
print(root.findval(7))
print("")
print(root.findval(14))
print("")
root.Inorder()
print("")

root.deleteNode(3)
print("")
root.Inorder()
print("")

root.deleteNode(6)
print("")
root.Inorder()
print("")

root.deleteNode(14)
print("")
root.Inorder()
print("")