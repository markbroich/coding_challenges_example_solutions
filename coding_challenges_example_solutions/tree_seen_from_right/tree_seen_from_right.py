# tree seen from the right

# return all node values when the tree is seen from the right


#           5
#       3       8   
#    1   4    9   2

# result: [5, 8 , 2]



#           5
#       3       8   
#    1   4    9   2
#   0          6 
#     7
#    9   

# result: [5, 8, 2, 6, 7, 9]


# DFS approach
# Ot(n) as I go over the entire tree
# Os(n) worth case as a tree that is a line of nodes 
# would fill the stack memory or stack proportional to the nodecount 

# loop option will be faster fro larger trees as no stack overhead

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    #
    def right_view(self, depth, maxdepth, nodeLst):
        if self.data == None:
            return maxdepth, nodeLst
        #
        depth += 1
        if depth > maxdepth:
            nodeLst.append(self.data)
            maxdepth = depth

        # a leaf
        if self.left == None and self.right == None:
            return maxdepth, nodeLst
        #
        # if right an option, go right
        if self.right:
            maxdepth, nodeLst = self.right.right_view(depth, maxdepth, nodeLst)
        # else go left
        if self.left:
            maxdepth, nodeLst = self.left.right_view(depth, maxdepth, nodeLst)
        return maxdepth, nodeLst
    #
    def right_view_loop(self):
        depth = maxdepth = 0 
        nodeLst = []
        if self.data == None:
            return nodeLst
        
        current = self
        stack = []

        while True:
            if not current == None:
                depth += 1
                stack.append((current, depth))                
                #
                if depth > maxdepth:
                    nodeLst.append(current.data)
                    maxdepth = depth
                current = current.right
            #
            elif stack:
                current, depth = stack.pop()
                current = current.left
            else:
                break
            #   
        return nodeLst
    #
    def right_view_bfs(self):
        if self.data == None:
            return -1
        #
        # create queue w seperator 
        Q = [self, float('inf')]
        rightViewLst = []
        while True:
            while Q[0] != float('inf'):
                current = Q.pop(0)   
                if not current.left == None:
                    Q.append(current.left)
                if not current.right == None:
                    Q.append(current.right)  
            # 
            # when end of level 
            Q.pop(0)  
            rightViewLst.append(current.data)
            #
            # if more to do
            if Q:
                Q.append(float('inf'))
            else:
                break

        return rightViewLst



tree = Node(5)
tree.left = Node(3)
tree.right = Node(8)

tree.left.left = Node(1)
tree.left.right = Node(4)

tree.right.left = Node(9)
tree.right.right = Node(2)

tree.left.left.left = Node(0)

tree.right.left.right = Node(6)

tree.left.left.left.right = Node(7)
tree.left.left.left.right.left = Node(9)

maxdepth, nodeLst = tree.right_view(depth=0, maxdepth=0, nodeLst=[])
print('right_view recursion')
print(nodeLst)
print('right_view loop')
print(tree.right_view_loop())
print('right_view bfs')
print(tree.right_view_bfs())
