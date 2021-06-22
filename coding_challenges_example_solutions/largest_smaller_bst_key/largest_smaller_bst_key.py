##########################################################
# CODE INSTRUCTIONS:                                     #
# 1) The method findLargestSmallerKey you're asked       #
#    to implement is located at line 30.                 #
#    it should find the largest key in the tree that     #
#    is smaller than num                                 #
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

    def find_largest_smaller_key(self, key):
        # task is to populate this function
        if not self.root:
            return -1
        current = self.root
        while current:
            res = current.key
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            if not current or key == current.key:
                return res

    def insert(self, key):
        # Given a binary search tree and a number, inserts a
        # new node with the given number in the correct place
        # in the tree. Returns the new root pointer which the
        # caller should then use(the standard trick to avoid
        # using reference parameters)
        #
        # 1) If tree is empty, create the root
        if (self.root is None):
            self.root = Node(key)
            return

        # 2) Otherwise, create a node with the key
        #    and traverse down the tree to find where to
        #    to insert the new node
        currentNode = self.root
        newNode = Node(key)

        while(currentNode is not None):
            if(key < currentNode.key):
                if(currentNode.left is None):
                    currentNode.left = newNode
                    newNode.parent = currentNode
                    return currentNode
                    break
                else:
                    currentNode = currentNode.left
            else:
                if(currentNode.right is None):
                    currentNode.right = newNode
                    newNode.parent = currentNode
                    return currentNode
                    break
                else:
                    currentNode = currentNode.right


######################################### 
# Driver program to test above function #
#########################################
bst = BinarySearchTree()


result = bst.find_largest_smaller_key(20)
print("Largest smaller number of 20 is %d " % (result))
print(result == -1)

# Create the tree given in the above diagram
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
bst.insert(11)
bst.insert(14)

result = bst.find_largest_smaller_key(9)
print("Largest smaller number of 9 is %d " % (result))
print(result == 20)
result = bst.find_largest_smaller_key(12)
print("Largest smaller number of 12 is %d " % (result))
print(result == 9)
result = bst.find_largest_smaller_key(17)
print("Largest smaller number of 17 is %d " % (result))
print(result == 14)
result = bst.find_largest_smaller_key(10)
print("Largest smaller number of 10 is %d " % (result))
print(result == 11)
result = bst.find_largest_smaller_key(3)
print("Largest smaller number of 3 is %d " % (result))
print(result == 5)
result = bst.find_largest_smaller_key(100)
print("Largest smaller number of 100 is %d " % (result))
print(result == 25)

'''
result = bst.find_largest_smaller_key(17)
print ("Largest smaller number is %d " %(result))
ans = 14

      20
     /  \
    9   25
   / \
  5  12
    /  \
   11  14


   num = 10, 3


'''
