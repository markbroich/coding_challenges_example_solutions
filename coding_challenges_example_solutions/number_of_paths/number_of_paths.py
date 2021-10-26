## Number of Paths

# You’re testing a new driverless car that is located at the Southwest 
# (bottom-left) corner of an n×n grid. 
# The car is supposed to get to the opposite, Northeast (top-right), corner of the grid. 
# Given n, the size of the grid’s axes, write a function numOfPathsToDest that returns 
# the number of the possible paths the driverless car can take.


# For convenience, let’s represent every square in the grid as a pair (i,j). The first 
# coordinate in the pair denotes the east-to-west axis, and the second coordinate denotes 
# the south-to-north axis. The initial state of the car is (0,0), and the destination is (n-1,n-1).

# The car must abide by the following two rules: it cannot cross the border diagonal from 
# Sw to NE across the square. In other words, in every step the position (i,j) needs to maintain 
# i >= j. 
# In every step, it may go one square North (up), or one 
# square East (right), but not both. E.g. if the car is at (3,1), it may go to (3,2) or (4,1).



## dynamic programming using memo
# 
# Ot(n^2) given that we visit each square (even if the valid space in only half the grid)
# hence, Os(n^2).   

def num_of_paths_to_dest(n):

  def explore(i,j, memo = {}):
    #
    if (i, j) == (0,0):
      return 1
    elif i < j:
      return 0
    elif j < 0:
      return 0
    elif (i,j) in memo:
      return memo[(i,j)]

    total =0
    # step left recur
    total += explore(i-1, j, memo)
    # step down recur
    total += explore(i, j-1, memo)

    memo[(i,j)] = total
    return memo[(i,j)]
  #
  return explore(n-1,n-1)

# 

def testing():
    print(num_of_paths_to_dest(1) == 1)
    print(num_of_paths_to_dest(2) == 1)
    print(num_of_paths_to_dest(3) == 2)
    print(num_of_paths_to_dest(4) == 5)
    print(num_of_paths_to_dest(6) == 42)
    print(num_of_paths_to_dest(17) == 35357670)

testing()



# iterative 
# Ot(n^2) 
# Os(n) since we are memoizing only the last two rows.
def num_of_paths_to_dest_it(n):
  if n == 1:
    return 1
  
  lastRow = ['']*n
  for i in range(1, n):
    lastRow[i] = 1
    
  currentRow = ['']*n
  
  for j in range(1, n):
    for i in range(j, n):
      if i == j:
        currentRow[i] = lastRow[i]
      else:
        currentRow[i] = currentRow[i-1] + lastRow[i]
    lastRow = currentRow
  return currentRow[n-1]

n = 4
print(num_of_paths_to_dest_it(n))


def testing():
    print(num_of_paths_to_dest_it(1) == 1)
    print(num_of_paths_to_dest_it(2) == 1)
    print(num_of_paths_to_dest_it(3) == 2)
    print(num_of_paths_to_dest_it(4) == 5)
    print(num_of_paths_to_dest_it(6) == 42)
    print(num_of_paths_to_dest_it(17) == 35357670)

testing()

