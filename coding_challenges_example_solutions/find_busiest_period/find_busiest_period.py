## Busiest Time in The Mall

# The Eastwestfield Mall management is trying to figure 
# out what the busiest moment at the mall was last year. 
# You’re given data extracted from the mall’s door detectors. 
# Each data point is represented as an integer array 
# whose size is 3. 
# The values at indices 0, 1 and 2 are the timestamp, 
# the count of visitors, and whether the visitors entered 
# or exited the mall (0 for exit and 1 for entrance), 
# respectively. 
# Here’s an example of a data point: 
# [ 1440084737, 4, 0 ].

# Note that time is given in a Unix format called Epoch, 
# which is a nonnegative integer holding the number of 
# seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.

# Given an array, data, of data points, write a function 
# findBusiestPeriod that returns the time at which the 
# mall reached its busiest moment last year. 
# The return value is the timestamp, e.g. 1480640292. Note that if 
# there is more than one period with the same visitor peak, 
# return the earliest one.

# Assume that the array data is sorted in an ascending order by the timestamp. 

# Example:
# input:  data = [ [1487799425, 14, 1], 
#                  [1487799425, 4,  0],
#                  [1487799425, 2,  0],
#                  [1487800378, 10, 1],
#                  [1487801478, 18, 0],
#                  [1487801478, 18, 1],
#                  [1487901013, 1,  0],
#                  [1487901211, 7,  1],
#                  [1487901211, 7,  0] ]

# output: 1487800378 # since the increase in the number of people
#                    # in the mall is the highest at that point

# Ot(n)
# Os(1)
def find_busiest_period(data):
  currentIn = 0
  maxIn = float('-inf')
  maxT = ''
  
  for i in range(0,len(data)):
    t = data[i][0]
    cnt = data[i][1]
    io = data[i][2]
    
    # entry
    if io:
      currentIn += cnt
    else:
      currentIn -= cnt
    
    # only budget if next is diff time
    if i+1 < len(data) and data[i+1][0] != t:
       maxIn, maxT = accounting(currentIn, maxIn, maxT, t)
  
  # do last accounting
  maxIn, maxT = accounting(currentIn, maxIn, maxT, t)
  return maxT  


def accounting(currentIn, maxIn, maxT, t):
  if currentIn > maxIn: 
    maxIn = currentIn
    maxT = t
  return maxIn, maxT


def testing(): 
    data =[[1487799426,21,1]]
    exp =  1487799426
    print(find_busiest_period(data) == exp)

    data =[[1487799425,21,0],[1487799427,22,1],[1487901318,7,0]]
    exp =  1487799427
    print(find_busiest_period(data) == exp)

    data =[[1487799425,21,1],[1487799425,4,0],[1487901318,7,0]]
    exp =  1487799425
    print(find_busiest_period(data) == exp)

    data =[[1487799425,14,1],[1487799425,4,0],[1487799425,2,0],[1487800378,10,1],[1487801478,18,0],[1487801478,18,1],[1487901013,1,0],[1487901211,7,1],[1487901211,7,0]]
    exp =  1487800378
    print(find_busiest_period(data) == exp)

    data =[[1487799425,14,1],[1487799425,4,1],[1487799425,2,1],[1487800378,10,1],[1487801478,18,1],[1487901013,1,1],[1487901211,7,1],[1487901211,7,1]]
    exp =  1487901211
    print(find_busiest_period(data) == exp)

    data =[[1487799425,14,1],[1487799425,4,0],[1487799425,2,0],[1487800378,10,1],[1487801478,18,0],[1487801478,19,1],[1487801478,1,0],[1487801478,1,1],[1487901013,1,0],[1487901211,7,1],[1487901211,8,0]]
    exp =  1487801478
    print(find_busiest_period(data) == exp)

testing()