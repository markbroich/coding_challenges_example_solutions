'''
Construct Quad Tree (leetcode 427: https://leetcode.com/problems/construct-quad-tree/)

Given a n * n matrix grid of 0's and 1's only. We want to represent the grid with a Quad-Tree.
Return the root of the Quad-Tree representing the grid.

Notice that you can assign the value of a node to True or False when leaf is False, and both are accepted 
in the answer.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. 
Besides, each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. 
isLeaf: True if the node is leaf node on the tree or False if the node has the four children.
class Node {
    public boolean val;
    public boolean leaf;
    public Node tl;
    public Node tr;
    public Node bl;
    public Node br;
}
We can construct a Quad-Tree from a two-dimensional area using the following steps:

If the current grid has the same value (i.e all 1's or all 0's) set leaf True and set 
val to the value of the grid and set the four children to Null and stop.
If the current grid has different values, set leaf to False and set val 
to any value and divide the current grid into four sub-grids as shown in the photo.
Recurse for each of the children with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer to the wiki.

Quad-Tree format:
The output represents the serialized format of a Quad-Tree using level order traversal, 
where null signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that 
the node is represented as a list [leaf, val].

If the value of leaf or val is True we represent it as 1 in the list [leaf, val] 
and if the value of leaf or val is False we represent it as 0.

Example 1:
Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Notice that 0 represnts False and 1 represents True in the photo representing the Quad-Tree.

Example 2:
Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The tl, bl and br each has the same value.
The tr have different values so we divide it into 4 sub-grids where each has the same value.


Example 3:
Input: grid = [[1,1],[1,1]]
Output: [[1,1]]

Example 4:
Input: grid = [[0]]
Output: [[1,0]]

Example 5:
Input: grid = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
Output: [[0,1],[1,1],[1,0],[1,0],[1,1]]

Constraints:
n == grid.length == grid[i].length
n == 2^x where 0 <= x <= 6

Background as per 'geek for geeks':
Quadtrees are used in image compression, 
where each node contains the average colour 
of each of its children. The deeper you 
traverse in the tree, the more the detail of the image.
Quadtrees are also used in searching for nodes in a 
two-dimensional area. For instance, 
if you wanted to find the closest point to 
given coordinates, you can do it using quadtrees.
If more than 2 dimensions: use KD tree
Quadtrees typically have contstruct, insert and search functions 
(only contstruct is coded here).
Search is used to locate a node in the given quad. 
It can also be modified to return the closest node 
to the given point. This function is implemented by 
taking the given point, comparing with the boundaries
of the child quads and recursing.
Both functions are O(Log N) where N is size of distance.

'''


class Node:
    def __init__(self, val, leaf=1, tl=None,
                 tr=None, bl=None, br=None):
        self.val = val
        self.leaf = leaf
        self.tl = tl
        self.tr = tr
        self.bl = bl
        self.br = br


class Solution:
    # recursion
    def construct(self, grid):
        if self.is_not_square(grid):
            return -1
        # base case
        if self.is_leaf(grid): 
            return Node(val=grid[0][0])
        # length grid and length grid half
        node = Node(val=999, leaf=0)
        lg = len(grid)
        lgh = int(lg/2)
        qLst = [('tl', 0, lgh, 0, lgh),
                ('tr', lgh, lg, 0, lgh),
                ('bl', 0, lgh, lgh, lg),
                ('br', lgh, lg, lgh, lg)]
        for kind, fc, tc, fr, tr in qLst:
            node.__dict__[kind] = self.add_subnode(grid, fc, tc, fr, tr)
        return node

    # input check
    def is_not_square(self, grid):
        if 2**len(grid) % 2 != 0:
            return True
        return False

    # leaf check 'is pure' (base case)
    def is_leaf(self, grid):
        num = grid[0][0]
        for c in range(0, len(grid)):
            for r in range(0, len(grid[0])):
                if grid[c][r] != num:
                    return False
        return True

    # add subnode
    def add_subnode(self, grid, fc, tc, fr, tr):
        subgrid = [lst[fc:tc] for lst in grid[fr:tr]]
        return self.construct(subgrid)

    # queue in a loop
    # Ot(N)
    def layer_order_traverse(self, root):
        returnLst = []
        if root.leaf == 0:
            returnLst.append([root.leaf, root.val, 'r', ''])
        nodLst = [(root.tl, 'r', 'tl'), (root.tr, 'r', 'tr'),
                  (root.bl, 'r', 'bl'), (root.br, 'r', 'br')]
        while True:
            nodLstNext = []
            for n, parent, kind in nodLst:
                returnLst.append([n.leaf, n.val, parent, kind])
                qLst = ['tl', 'tr', 'bl', 'br']
                nodLstNextPlus = [(n.__dict__[q], q, kind) 
                                  for q in qLst if n.__dict__[q]]
                nodLstNext = nodLstNext + nodLstNextPlus
            if len(nodLstNext) == 0:
                break
            returnLst.append(['next level'])
            nodLst = nodLstNext
        return returnLst


# run code
S = Solution()

# example A:
# image https://assets.leetcode.com/uploads/2020/02/12/e2tree.png
grid = [[1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0]]
exp = [[0, 999, 'r', ''], [1, 1, 'r', 'tl'], [0, 999, 'r', 'tr'], [1, 1, 'r', 'bl'], [1, 0, 'r', 'br'], ['next level'], 
       [1, 0, 'tl', 'tr'], [1, 0, 'tr', 'tr'], [1, 1, 'bl', 'tr'], [1, 1, 'br', 'tr']]

rootNode = S.construct(grid)
print('[isLeaf, val, kind, parent]')
print('a val of 999 == impure, so isLeaf will be 0')
print(S.layer_order_traverse(rootNode))
print(S.layer_order_traverse(rootNode) == exp)


# example B:
grid = [[1,1,1,1,0,0,0,1],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0]]
exp = [[0, 999, 'r', ''], [1, 1, 'r', 'tl'], [0, 999, 'r', 'tr'], [1, 1, 'r', 'bl'], [1, 0, 'r', 'br'], ['next level'], 
      [1, 0, 'tl', 'tr'], [0, 999, 'tr', 'tr'], [1, 1, 'bl', 'tr'], [1, 1, 'br', 'tr'], ['next level'], 
      [1, 0, 'tl', 'tr'], [1, 1, 'tr', 'tr'], [1, 0, 'bl', 'tr'], [1, 0, 'br', 'tr']]

rootNode = S.construct(grid)
print(S.layer_order_traverse(rootNode) == exp)


grid = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
exp = [[0, 999, 'r', ''], [1, 1, 'r', 'tl'], [1, 0, 'r', 'tr'], [1, 0, 'r', 'bl'], [1, 1, 'r', 'br']]
rootNode = S.construct(grid)
print(S.layer_order_traverse(rootNode) == exp)




