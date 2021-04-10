
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
    self.parent = None
 

  def find_min_cost(self, prune=False):
    if not self.children:
      return self.cost
    
    Q = [(self, self.cost)]
    #  
    costLst = []
    while Q:
        node, cost = Q.pop(0)
        print(node.cost)
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
        print(node.cost)
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
  
if __name__ == "__main__":
    main()
    

# Qt(n) and Qs(n) given that every node is visited once. 
# the prune option will not explore a branch further if the cost > cur min cost
# hence, the number of nodes will be fewer but the runtime will still be O(n) at max
    
