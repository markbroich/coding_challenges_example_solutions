
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
  def find_min_cost_prune(self):
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
            # only que if path cost < min cost so far
            if(len(costLst) > 0 and 
                child.cost + cost > min(costLst)):
                continue
            else:
                Q.append((child, child.cost + cost))
    return min(costLst)
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

def main():
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

  print(tree.find_min_cost() == 7)
  print()
  print(tree.find_min_cost_prune() == 7)
  print()
  print(tree.find_min_cost_dfs_rec(tree) == 7)
  
if __name__ == "__main__":
    main()
    

# Qt(n) and Qs(n) given that every node is visited once. 
# The max que length is max layer width -1 + max children 
# # of a node in that wide layer. The max que length will 
# be between > 1 and < n, so Os(n). 

# The prune option will not explore a branch further if the 
# cost > cur min cost hence, the number of nodes will be 
# fewer but the runtime will still be O(n) at max
    
# When using recursion (and dfs), the function is applied to 
# every node once. Hence Ot(n). 
# the call stack is at max n deep so we would use space 
# proportional to n. If this was a binary search tree, 
# the depth would be log(n) but in an ordinary tree, all 
# n nodes may be on one branch. 







