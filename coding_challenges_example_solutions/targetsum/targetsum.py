"""
Given the root of a binary tree and an integer targetSum, return true 
if the tree has a root-to-leaf path such that adding up all the values 
along the path equals targetSum.

A leaf is a node with no children.

https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg
Input: root = [1,2,3], targetSum = 5
Output: false

Input: root = [1,2], targetSum = 0
Output: false

"""
# Ot(n) 
# Os(log(n)) or Os(k) were k is height

# worth case: 
# Os(n)
#  r
#   r
#    r
#     r
#      r
# for a balanced tree: Os(lon(n)) where n node count
#    

# execting positive and negative cases
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    #
    def eq_targetsum(self, tSum):
        # if None
        if self == None:
          return False
        # exceeded
        elif tSum - self.val < 0:
          return False
        # reach leaf
        elif self.left == None and self.right == None:
          if tSum - self.val == 0:
            return True
          else:
            return False
        #
        # if left and right then
        return self.left.eq_targetsum(tSum-self.val) or self.right.eq_targetsum(tSum-self.val)
    # 
    def eq_targetsum_path(self, tSum, path=[]):
        # if None
        if self == None:
          return False
        # exceeded
        elif tSum - self.val < 0:
          return False
        # reach leaf
        #
        path.append(self.val)
        if self.left == None and self.right == None:
          if tSum - self.val == 0:
            return path  ###############
          else:
            return False
        # if left and right then
        return self.left.eq_targetsum_path(tSum-self.val, path) or self.right.eq_targetsum_path(tSum-self.val, path)
        #
        #
    def inorder(self):
        if self.val == None:
            return -1
        current = self
        stack = []
        while True:
            if current != None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.val)
                current = current.right
            else: 
                break
                
                #

        
            
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# 5,4,8,
bt = TreeNode(5)
bt.left = TreeNode(4)
bt.right = TreeNode(8)
# 11,null,13,4
bt.left.left = TreeNode(11)
#bt.left.right
bt.right.left = TreeNode(13)
bt.right.right = TreeNode(4)
# 7,2, null,null,null,1
bt.left.left.left = TreeNode(7)
bt.left.left.right = TreeNode(2)
bt.right.right.right = TreeNode(1)

bt.inorder()
print()
targetSum = 22
print(bt.eq_targetsum(targetSum))
print()
print(bt.eq_targetsum_path(targetSum))


        




