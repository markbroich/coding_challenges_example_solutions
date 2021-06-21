'''
Validate Binary Search Tree [#57](https://codebasil.com/problems/validate-binary-search-tree) 

    Given a binary tree, validate if it's a binary search tree (BST).
    A binary search tree is a tree data structure that has the following properties:
        The left subtree of a node contains only nodes with keys smaller than the node’s key.
        The right subtree of a node contains only nodes with keys greater than the node’s key.
        The left and right subtree each must also be a binary search tree.
    EXAMPLE:
        Input: [4,2,5,null,null,null,6]
        Output: true    
    """
    Node {
        val: int
        left: Node
        right: Node
    }
    """
'''

class Node():
    def __init__(self, int):
        self.key = int
        self.left = None
        self.right = None

def validate_bst(node, minKey=None, maxKey=None):
  if not node:
    return True
  else:
    withinBound = (minKey == None or node.key > minKey) \
                    and (maxKey == None or node.key < maxKey)
    if not withinBound:
        return False
    return validate_bst(node.left, minKey, node.key) and validate_bst(node.right, node.key, maxKey)



def testing():
    # ex 1
    #       4
    #     2   5
    #           6
    #
    tree = Node(4)
    tree.left = Node(2)
    tree.right = Node(5)
    tree.right.right = Node(6)
    print(validate_bst(tree) == True)

    # ex 2
    #            4 
    #          /   \
    #        2       5 
    #              /  \
    #             3    6 
    #
    tree = Node(4)
    tree.left = Node(2)
    tree.right = Node(5)
    tree.right.right = Node(6)
    tree.right.left = Node(3)
    print(validate_bst(tree) == False)

testing()


# https://leetcode.com/problems/validate-binary-search-tree/