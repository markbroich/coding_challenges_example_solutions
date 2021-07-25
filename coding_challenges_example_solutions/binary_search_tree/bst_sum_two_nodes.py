
# write an algo to check if two BST node sum to number
# e.g.
# num: 9
# tree:
#       5
#    3    6
# 2   4     7
# retrun: True (given that 7+4=9 or 3+6=9)

# Ot(n) where nis elems in bst
# Os( numerb of unique keys)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_two_elem_eq_num(bst, num):
    remainSet = set()
    # in order traversal
    stack = []
    while True:
        if bst:
            stack.append(bst)
            bst = bst.left
        elif stack:
            bst = stack.pop()
            ## check against set
            # if yes, return True
            # else add remainder to set
            if bst.val in remainSet:
                return True
            else:
                remainSet.add(num-bst.val)
            bst = bst.right
        else:
            break
    return False


def find_two_elem_eq_num_rec(bst, num, remainSet):
    # using recusion
    if not bst:
        return False
    # check against set
    if bst.val in remainSet:
        return True
    else:
        remainSet.add(num-bst.val)
    # in order traversal
    if find_two_elem_eq_num_rec(bst.left, num, remainSet):
        return True
    if find_two_elem_eq_num_rec(bst.right, num, remainSet):
        return True
    return False


# run code
bst = TreeNode(5)
bst.left = TreeNode(3)
bst.right = TreeNode(6)

bst.left.left = TreeNode(2)
bst.left.right = TreeNode(4)

bst.right.right = TreeNode(7)

num = 9
print(find_two_elem_eq_num(bst, num))

remainSet = set()
print(find_two_elem_eq_num_rec(bst, num, remainSet))
