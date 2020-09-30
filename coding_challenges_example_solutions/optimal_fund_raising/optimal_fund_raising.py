## Optimal fund raising

# A mayor in a remote mountain village faced an emergency and he needs your help. He just learned a poor boy is very sick, 
# and will need to go to the city hospital immediately.
# He only has one night to collect the contribution from the villagers, so that he can escort the boy and his family to the city next morning. 
# Luckily, he has kept a 'secret list' of each family's "financial status + willingness to help" in his file over the years.

# So the challenge is how to find the starting family in the narrow and linearly populated mountain valley, making sure he can collect maximum funds.

# The goal is to help the mayor to collect the maximum contribution and determine which families to start (and end). These are the key elements of this mission:

# To find the families in the closest neighborhood in the village with best possible donations that he can collect. 
# You can think of this closest neighborhood as - "contiguous families block" in the "list", without circulating back. 
# Since time is essence in this matter, he wants to get the funds quickly and prepare for next day's trip.


# Let's make some concrete examples to illustrate these points:

# Input: the list represents that each family's 'capacity' to contribute in $dollars_amount: it could be one of these values: 
# positive, negative, or zero. For example: [0, 1, 2, 4, -3, -3]

# Note - the mountain village could have hundreds of families scattered around in wide area, so he would just go in one-direction. 
# Therefore he prefers one-way trips (not circular!) - one pass. (this is known in CS as O(n) time requirement)

# Output: 3 items he needs to know - the maximum contribution (amount), startingfamily, endingfamily (eg. by its index). See below examples.
# Bonus - it will be great if you can help him find out the possibility of positive donations - e.g. there is at least one family can 
# contribute before he starts the night trip. If the "donations" are negative - meaning all families are poor - then you could give him a warning message: 
# "Mission impossible. No one can contribute.", exiting the program with (0, 0, 0) - see example 4 below.

# ###### Example 1
# input:
#    village =  [0, -3, 2, 1, -7, 5, 3, -1, 6]
#      # index   0  1   2  3  4   5  6  7  8
#      #                          ************
# >>> max_fund(village)
#    (13, 6, 9)      
#    fund: 13;
#    starting at 6;  index 5 + 1
#    ending at 9;    indext 8 + 1 (from mayor's perspective - the first potion should be ONE)

# ###### Example 2
# input:
#    One  = [0, 1, -1, -5, 0, 4, -3, -2]

# >>> max_fund(one)
#   (4, 6, 6))

# ###### Example 3
# input:
#    penniless = [0, 0, 0, 0, 1, -5, -2, -1, -3]
# >>> max_fund(penniless)
#   (1, 5, 5))

# ###### Example 4
# input:
#    extremes  = [-1, -2, -3, -4, -5]
# >>> max_fund(extremes)
#    'Mission Impossible. No one can contribute!'
#   (0, 0, 0)

#####
# so we are looing for the maximum amount when summing betwee a starting and an ending index along a list of numbers

# O(n**2) space is O(1))
def donation_n_squared(village):
    max_ = -99999
    i_ = -1
    j_ = -1
    for i in range(0, len(village)):
        for j in range(0, len(village)+1):    
            if sum((village[i:j])) > max_:
                max_ = sum(village[i:j])
                i_ = i
                j_ = j
    return max_, i_, j_

print("donation_n_squared")
village =  [0, -3, 2, 1, -7, 5, 3, -1, 6]
max_, i_, j_ = donation_n_squared(village)
print('max_amount: ', max_)
print('starting index: ', i_)
print('ending index: ', j_)
print("")

# O(n) algo (space is O(1))
def donation_O_of_n(village):
    max_ = -99999
    i_ = -1
    j_ = -1
    count = 0
    for j in range(0, len(village)+1):
        for i in range (j, 0, -1):
            count += 1
            if(sum(village[i:j]) > max_):
                max_ = sum(village[i:j])
                i_ = i
                j_ = j
    if max_ <= 0:
        print("Mission Impossible. No one can contribute!")
        return 0, 0, 0, count
    else: 
        print("positive donation possible")
        return max_, i_, j_, count

print("donation_O_of_n")
village =  [0, -3, 2, 1, -7, 5, 3, -1, 6]
max_, i_, j_, count = donation_O_of_n(village)
print("donation_O_of_n took: ", count, "steps to calc vs ", len(village)*len(village), "steps for the brute force algo")
print('max_amount: ', max_)
print('starting index: ', i_)
print('ending index: ', j_)
print("")



### more tests
# One
print("One")
village  = [0, 1, -1, -5, 0, 4, -3, -2]
max_, i_, j_, count = donation_O_of_n(village)
print("donation_O_of_n took: ", count, "steps to calc vs ", len(village)*len(village), "steps for the brute force algo")
print('max_amount: ', max_)
print('starting index: ', i_)
print('ending index: ', j_)
print("")

# penniless
print("penniless")
village = [0, 0, 0, 0, 1, -5, -2, -1, -3]
max_, i_, j_, count = donation_O_of_n(village)
print("donation_O_of_n took: ", count, "steps to calc vs ", len(village)*len(village), "steps for the brute force algo")
print('max_amount: ', max_)
print('starting index: ', i_)
print('ending index: ', j_)
print("")

# extremes
print("extremes")
village  = [-1, -2, -3, -4, -5]
max_, i_, j_, count = donation_O_of_n(village)
print("donation_O_of_n took: ", count, "steps to calc vs ", len(village)*len(village), "steps for the brute force algo")
print('max_amount: ', max_)
print('starting index: ', i_)
print('ending index: ', j_)
print("")


### to demonstrate the runtime

# a way to calc the number of steps reqired. 
# showing that the runtime increase in O(n) where n is the size of the array
def stepcounter(village):
    steps = 0
    for i in range(0, len(village)):
        steps += len(village)-i
    print(steps, " is the number of steps it takes to cacl the max donation for ", village)

stepcounter(village)

# and graphically 
village = [1,2,3,4,5,6]
stepcounter(village)

# [1,  2,  3,  4,  5,  6]
# |_| |_| |_| |_| |_| |_| # 6 slots of width 1
#   |__|                  # 5 slots of width 2
#       |__|
#           |__|
#               |__|
#                  |__|
# |________|              # 4 slots of width 3
#      |________|              
#          |________|   
#              |________|  
# |__________|            # 3 slots of width 4            
#      |__________|           
#          |__________|         
# |______________|        # 2 slots of width 5
#      |______________|         
# |___________________|   # 1 slots of width 6
# 6 + 5 + 4 + 3 + 2 + 1 = 21 

# challenge by PyBites. https://codechalleng.es/bites/paths/algorithms
