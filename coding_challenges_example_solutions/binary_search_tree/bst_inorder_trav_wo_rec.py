
## Do inorder travesal w/o using recursion
# task is to populate inOrder() in line 15


# A binary search tree node
class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# Iterative function for inorder tree traversal
def inOrder(root):
    current = root

    stack = []
    while True:
        if current:
            stack.append(current)
            current = current.left
        #
        elif(stack):
            current = stack.pop()
            print(current.data)
            current = current.right
        else: 
            break



 
# Driver program to test above function
 
""" Constructed binary tree is
            1
          /   \
         0     3
       /  \
    -2    -1   """
 
root = Node(1)
root.left = Node(0)
root.right = Node(3)
root.left.left = Node(-2)
root.left.right = Node(-1)
 
inOrder(root)