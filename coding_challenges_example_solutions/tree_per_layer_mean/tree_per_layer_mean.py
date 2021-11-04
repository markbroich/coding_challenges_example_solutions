# return per layer mean of binary tree

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

    def per_layer_mean(self):
        mean_lst = []
        level = lSum = cnt = 0
        queue = [self.root, -999]
        while queue:
            cur = queue.pop(0)
            if cur == -999:
                mean_lst.append([(level, lSum/cnt)])
                if queue:
                    queue.append(-999)
                    level += 1
                    lSum = cnt = 0
            else: 
                cnt += 1
                lSum += cur.key
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return mean_lst

    def insert(self, key):
        if (self.root is None):
            self.root = Node(key)
            return

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


#########################################
# Driver program to test above function #
#########################################
bst = BinarySearchTree()

# Create the tree given in the above diagram
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
bst.insert(11)
bst.insert(14)
print(bst.per_layer_mean())
'''
      20
     /  \
    9   25
   / \
  5  12
    /  \
   11  14
'''
