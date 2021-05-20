
## Sales Path

## The car manufacturer Trabbi holds their distribution system in the form of a tree 

# Trabbi wishes to find the minimal Sales Path cost in its distribution tree. 
# Given a node rootNode, write a function getCheapestCost that calculates the minimal Sales 
# Path cost in the tree.



# A node 
class Node:

  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
 

  def find_min_cost(self, prune=False):
    if not self.children:
      return self.cost
    
    Q = [(self, self.cost)]
    #  
    costLst = []
    while Q:
        node, cost = Q.pop(0)
        for child in node.children:
            if not child.children:
                costLst.append(child.cost + cost)
            # 
            Q.append((child, child.cost + cost))
    return min(costLst)
  #
  #
  def find_min_cost_dfs_rec(self, node):
    n = len(node.children)
    if (n == 0):
      return node.cost
    # 
    minCost = float('inf')
    for i in range(0,n):
      cost = self.find_min_cost_dfs_rec(node.children[i])
      minCost = min(cost, minCost)
    return minCost+node.cost
  #
  # A good follow up question, is how to determine the 
  # longest or shortest Sales Path path.
  def find_min_max_cost_dfs_rec(self, node):
    n = len(node.children)
    if (n == 0):
      return node.cost, node.cost
    # 
    minCost = float('inf')
    maxCost = float('-inf')
    for i in range(0,n):
      newMinCost, newMaxCost = self.find_min_max_cost_dfs_rec(node.children[i])
      minCost = min(newMinCost, minCost)
      maxCost = max(newMaxCost, maxCost)
    return minCost+node.cost, maxCost+node.cost

  # A good followup question is how to 
  # return all the Sales Paths with 
  # minimal cost in an array
  def find_min_cost_dfs_rec_path(self, node):
    n = len(node.children)
    if (n == 0):
      return node.cost, [node.cost]
    # 
    #
    path = []
    minCost = float('inf')
    for i in range(0,n):
      cost, pathRet = self.find_min_cost_dfs_rec_path(node.children[i])
      if cost == minCost:
        path = [path+[node.cost]] + [pathRet+[node.cost]]
      if cost < minCost:
        minCost = cost
        path = pathRet 
    #
    # if nested lst
    if any(isinstance(i, list) for i in path):
      return minCost+node.cost, path 
    else:
      return minCost+node.cost, path +[node.cost]


def main():
  # Test1
  tree = Node(0)

  n1 = Node(5)
  n2 = Node(20)
  n3 = Node(6)

  n4 = Node(4)
  n5 = Node(1)

  n6 = Node(2)

  tree.children = [n1,n2,n3]
  n1.children = [n4]
  n3.children = [n5]
  n4.children = [n6]

  #            0
  #         /  |  \
  #       5    20   6
  #     /            \ 
  #    4              1
  #  /
  # 2
  print('test1')
  print(tree.find_min_cost() == 7)
  print(tree.find_min_cost_dfs_rec(tree) == 7)
  print(tree.find_min_cost_dfs_rec_path(tree) == (7,[1,6,0]))
  print(tree.find_min_max_cost_dfs_rec(tree) == (7,20))
  #
  # Test2
  tree = Node(0)

  n1 = Node(5)
  n2 = Node(3)
  n3 = Node(6)

  n4 = Node(4)
  n5 = Node(2)
  n6 = Node(0)
  n7 = Node(1)
  n8 = Node(5)


  n9 = Node(1)
  n10 = Node(10)

  n11 = Node(1)

  tree.children = [n1,n2,n3]
  n1.children = [n4]
  n2.children = [n5,n6]
  n3.children = [n7,n8]

  n5.children = [n9]
  n6.children = [n10]
  
  n9.children = [n11]

  #            0
  #         /  |  \
  #       5    3   6
  #     /   /  |   | \ 
  #    4   2   0   1   5
  #      /    /
  #     1    10
  #     | 
  #     1
  # 
  print('test2')
  print(tree.find_min_cost() == 7)
  print(tree.find_min_cost_dfs_rec(tree) == 7)
  print(tree.find_min_cost_dfs_rec_path(tree) == (7,[[1,1,2,3,0],[1,6,0]]))
  print(tree.find_min_max_cost_dfs_rec(tree) == (7,13))

if __name__ == "__main__":
    main()
    

# Qt(n) and Qs(n) given that every node is visited once. 
# The max que length is max layer width -1 + max children 
# # of a node in that wide layer. The max que length will 
# be between > 1 and < n, so Os(n). 

    
# When using recursion (and dfs), the function is applied to 
# every node once. Hence Ot(n). 
# the call stack is at max n deep so we would use space 
# proportional to n. If this was a binary search tree, 
# the depth would be log(n) but in an ordinary tree, all 
# n nodes may be on one branch. 



