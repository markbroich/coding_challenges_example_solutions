#########################################################
# CODE INSTRUCTIONS:                                    #
# 1) The method findInOrderSuccessor you're asked       #
#    to implement is located at line 30.                #
# 2) Use the helper code below to implement it.         #
# 3) In a nutshell, the helper code allows you to       #
#    to build a Binary Search Tree.                     #
#########################################################


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
    
  def find_in_order_successor(self, inputNode):
    # runcode get the input node so that node exists
    # node parent is known
    #
    # case 1: has right child: go right and then all the way 
    # left to find successor
    #
    # case 2: does not have right child, so successor must be 
    # somewhere between the partent and the root., se we need to go up.
    # specifically, when we 'come up' from the left, we know that 
    # the parent is > child, hence a successor
    #
    #       20
    #      /  \     
    #     9    25
    #   /  \
    #  5   12
    #     /  \
    #    11   14
    #
    # case 1 (find min of right subtree):
    if inputNode.right:
        current = inputNode.right
        while current.left:
            current = current.left
        return current
    
    # case 2 (find parent node reached from a left child):
    current = inputNode
    # while there is a parent and we are not comming up from 
    # the left: 
    while current.parent and current.parent.left != current: 
        # keep comming up
        current = current.parent
    # once we have come up form the left or if there is no parent, 
    # we found the successor:
    return current.parent
    
  
  # Given a binary search tree and a number, inserts a
  # new node with the given number in the correct place
  # in the tree. Returns the new root pointer which the
  # caller should then use(the standard trick to avoid 
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
    while(currentNode is not None):
      
      if(key < currentNode.key):
        if(currentNode.left is None):
          currentNode.left = newNode
          newNode.parent = currentNode
          break
        else:
          currentNode = currentNode.left
      else:
        if(currentNode.right is None):
          currentNode.right = newNode
          newNode.parent = currentNode
          break
        else:
          currentNode = currentNode.right

  # Return a reference to a node in the BST by its key.
  # Use this method when you need a node to test your
  # findInOrderSuccessor function on
  def getNodeByKey(self, key):
    
    currentNode = self.root
    while(currentNode is not None):
      if(key == currentNode.key):
        return currentNode
        
      if(key < currentNode.key):
        currentNode = currentNode.left
      else:
        currentNode = currentNode.right
        
    return None
        
######################################### 
# Driver program to test above function #
#########################################

# Create a Binary Search Tree
bst  = BinarySearchTree()
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
bst.insert(11)  
bst.insert(14)    

#       20
#      /  \     
#     9    25
#   /  \
#  5   12
#     /  \
#    11   14

def printing(test, succ):
    # Print the key of the successor node
    if succ is not None:
        print ("\nInorder Successor of %d is %d " \
                %(test.key , succ.key))
    else:
        print ("\nInorder Successor doesn't exist")

def testing():
    # Find the in order successor of test
    # Get a reference to the node whose key is 9
    test = bst.getNodeByKey(9)
    succ = bst.find_in_order_successor(test)
    printing(test, succ)
    
    # Get a reference to the node whose key is 12
    test = bst.getNodeByKey(12)
    succ = bst.find_in_order_successor(test)
    printing(test, succ)
    
    # Get a reference to the node whose key is 14
    test = bst.getNodeByKey(14)
    succ = bst.find_in_order_successor(test)
    printing(test, succ)

    # Get a reference to the node whose key is 20
    test = bst.getNodeByKey(20)
    succ = bst.find_in_order_successor(test)
    printing(test, succ)

    # Get a reference to the node whose key is 25
    # test = bst.getNodeByKey(25)
    # succ = bst.find_in_order_successor(test)
    # printing(test, succ)


#       20
#      /  \     
#     9    25
#   /  \
#  5   12
#     /  \
#    11   14

# run testing
testing()

#####
# Time Complexity: at most we travel down the height of the BST looking for 
# the smallest in the right subtree or up the parents until at max the root. 
# so Ot(log n) as a binary search tree's height is log(n)
# space complexity of the find_in_order_successor method is Os(1)



# task by Pramp.com