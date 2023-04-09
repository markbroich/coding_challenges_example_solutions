'''Largest Smaller BST Key

Given a root of a Binary Search Tree (BST) and a number num, implement
an efficient function findLargestSmallerKey that finds the largest key
in the tree that is smaller than num. If such a number does
not exist, return -1. Assume that all keys in the tree are nonnegative.

Analyze the time and space complexities of your solution.



Constraints:
[time limit] 5000ms
[input] Node rootNode
[output] integer
'''

##########################################################
# CODE INSTRUCTIONS:                                     #
# 1) The method findLargestSmallerKey you're asked       #
#    to implement is located at line 30.                 #
# 2) Use the helper code below to implement it.          #
# 3) In a nutshell, the helper code allows you to        #
#    to build a Binary Search Tree.                      #
# 4) Jump to line 71 to see an example for how the       #
#    helper code is used to test findLargestSmallerKey.  #
##########################################################


# A node
class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


# A binary search tree

class BinarySearchTree:
    # Constructor to create a new BST
    def __init__(self):
        self.root = None
        self.max_seen = -1

    def find_largest_smaller_key(self, num):
        if not self.root:
            return -1
        cur = self.root
        while cur:
            if num > cur.key:
                # as I go right, the key < num and getting larger
                self.max_seen = cur.key
                cur = cur.right
            else:
                # as key > num, go left
                cur = cur.left
        return self.max_seen

    # Given a binary search tree and a number, inserts a
    # new node with the given number in the correct place
    # in the tree. Returns the new root pointer which the
    # caller should then use (the standard trick to avoid
    # using reference parameters)
    def insert(self, key):
        # 1) If tree is empty, create the root
        if (self.root is None):
            self.root = Node(key)
            return

        # 2) Otherwise, create a node with the key
        #    and traverse down the tree to find where to
        #    to insert the new node
        currentNode = self.root
        newNode = Node(key)

        while currentNode is not None:
            if key < currentNode.key:
                if currentNode.left is None:
                    currentNode.left = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.right

#########################################
# Driver program to test above function #
#########################################
bst  = BinarySearchTree()
 
# Create the tree given in the above diagram 
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
bst.insert(11)
bst.insert(14)    

result = bst.find_largest_smaller_key(17) # exp 14
print ("Largest smaller number is %d " %(result))


bst  = BinarySearchTree()
bst.insert(20)
bst.insert(18)
bst.insert(25)
bst.insert(19)
bst.insert(15)  
result = bst.find_largest_smaller_key(26)
print (result == 25)

bst  = BinarySearchTree()
bst.insert(20)
bst.insert(18)
bst.insert(25)
bst.insert(19)
bst.insert(15)
result = bst.find_largest_smaller_key(20)
print (result == 19)

bst  = BinarySearchTree()
bst.insert(20)
bst.insert(18)
bst.insert(25)
bst.insert(19)
bst.insert(15)
result = bst.find_largest_smaller_key(18)
print (result == 15)

bst  = BinarySearchTree()
bst.insert(20)
bst.insert(18)
bst.insert(25)
bst.insert(19)
bst.insert(15)
result = bst.find_largest_smaller_key(19)
print (result == 18)

bst  = BinarySearchTree()
bst.insert(20)
bst.insert(18)
bst.insert(25)
bst.insert(19)
bst.insert(15)
result = bst.find_largest_smaller_key(15)
# print('res', result)
print (result == -1)

bst  = BinarySearchTree()
bst.insert(20)
bst.insert(18)
bst.insert(25)
bst.insert(19)
bst.insert(15)
result = bst.find_largest_smaller_key(2)
# print (result)
print (result == -1)
