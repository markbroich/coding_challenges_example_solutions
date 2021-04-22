# Path Sum


# Given the root of a binary tree and an integer targetSum, return true if the tree 
# has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

# Example 1:
# Input: root = [5,4,8, 11,null,13,4, 7,2,null,null,null,1], targetSum = 22
# Output: true

# Example 2:
# Input: root = [1,2,3], targetSum = 5
# Output: false

# Example 3:
# Input: root = [1,2], targetSum = 0
# Output: false


#Ot(N) as we visit each node once

# Os(N) for recursive calls if each node has one child
# Os(logN) if tree is balances
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def path_sum_eq_x(self, targetSum):
        if not self:
            return False
        targetSum -= self.data
        # found child
        if not self.left and not self.right:
                return targetSum == 0
        return (bool(self.left) and self.left.path_sum_eq_x(targetSum))\
             or (bool(self.right) and self.right.path_sum_eq_x(targetSum))

       # 

def testing():
    # example 1
    targetSum = 22
    tree = Node(5)
    tree.left = Node(4)
    tree.right = Node(8)

    tree.left.left = Node(11)
    tree.right.left = Node(13)
    tree.right.right = Node(4)

    tree.left.left.left = Node(7)
    tree.left.left.right = Node(2)
    tree.right.right.right = Node(1)

    print(tree.path_sum_eq_x(targetSum) == True)

    # example 2
    targetSum = 5
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)

    print(tree.path_sum_eq_x(targetSum) == False)

    # example 3
    targetSum = 0
    tree = Node(1)
    tree.left = Node(2)

    print(tree.path_sum_eq_x(targetSum) == False)

testing()