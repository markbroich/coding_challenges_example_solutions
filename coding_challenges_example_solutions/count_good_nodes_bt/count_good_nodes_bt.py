"""
Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:
[Image: https://assets.leetcode.com/uploads/2020/04/02/test_sample_1.png]
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
[Image: https://assets.leetcode.com/uploads/2020/04/02/test_sample_2.png]
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.
"""



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

            
def count_larger(root, maxSeen=-99999):  
  if root is None:
    return 0
  if root.val >= maxSeen:
    maxSeen = root.val
    return 1 + count_larger(root.left, maxSeen) + count_larger(root.right, maxSeen)
  else: 
    return count_larger(root.left, maxSeen) + count_larger(root.right, maxSeen)



def testing():
  # Example 1:
  # [Image: https://assets.leetcode.com/uploads/2020/04/02/test_sample_1.png]
  # Input: root = [3,1,4,3,null,1,5]
  # Output: 4

  # [3,1,4,3,null,1,5]
  tree = TreeNode(3)
  tree.left = TreeNode(1)
  tree.right = TreeNode(4)
  tree.left.left = TreeNode(3)
  tree.right.left = TreeNode(1)
  tree.right.right = TreeNode(5)
  expected = 4
  print(count_larger(tree) == expected)

  #Example 2:
  #[Image: https://assets.leetcode.com/uploads/2020/04/02/test_sample_2.png]
  # Input: root = [3,3,null,4,2]
  # Output: 3
  # Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
  tree = TreeNode(3)
  tree.left = TreeNode(3)
  tree.left.left = TreeNode(4)
  tree.left.right = TreeNode(2)
  expected = 3
  print(count_larger(tree) == expected)

  # Example 3:
  # Input: root = [1]
  # Output: 1
  # Explanation: Root is considered as good.
  tree = TreeNode(1)
  expected = 1
  print(count_larger(tree) == expected)


testing()

"""
https://leetcode.com/problems/count-good-nodes-in-binary-tree/
"""
  
