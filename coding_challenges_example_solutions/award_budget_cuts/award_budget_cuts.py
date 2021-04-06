## Award Budget Cuts

# The awards committee of your alma mater (i.e. your college/university) 
# asked for your assistance with a budget allocation problem they’re facing. 
# Originally, the committee planned to give N research grants this year. 
# However, due to spending cutbacks, the budget was reduced to newBudget 
# dollars and now they need to reallocate the grants. 
# The committee made a decision that they’d like to impact as 
# few grant recipients as possible by applying a maximum cap on all grants. 
# Every grant initially planned to be higher than cap will now be exactly cap dollars. 
# Grants less or equal to cap, obviously, won’t be impacted.

# Given an array grantsArray of the original grants and the reduced budget newBudget, 
# write a function findGrantsCap that finds in the most efficient manner a cap such 
# that the least number of recipients is impacted and that the new budget constraint 
# is met (i.e. sum of the N reallocated grants equals to newBudget).

# Analyze the time and space complexities of your solution.

# Example:
# input:  grantsArray = [2, 100, 50, 120, 1000], newBudget = 190
# output: 47


# The desired 'cap' is a value that affects the minimum number of grants. 
# the 'cap' is what remains to be divided accross the 'larger than' 
# after the 'smaller than' haven been fully funded. 

# Ot(nlog(n)+n) so O(nlog(n)) 
# Os(1)
def find_grants_cap(grantsArray, newBudget):
    if not grantsArray:
        return -1
        
    # reverse sort   
    sortedgrantsArray = sorted(grantsArray, reverse=True)
    
    if sum(sortedgrantsArray) < newBudget:
        return sortedgrantsArray[0] # largest is cap
    
    # if smallerst > newBudget
    if sortedgrantsArray[-1] > newBudget:
        return newBudget/len(sortedgrantsArray) # all grants get the same

    # pad w a zero (a zero budget grant)
    sortedgrantsArray.append(0)
    
    # loop over arr
    for i in range(0,len(sortedgrantsArray)):
        # leave out the (next) highest one
        if sum(sortedgrantsArray[i+1:]) < newBudget:

            # what remainsafter the 'smaller than' haven been fully funded  
            remains = (newBudget - sum(sortedgrantsArray[i+1:])) 
            # be divided accross the 'larger than' = the 'cap'
            cap = remains/ (i+1)
            # must ensure that cap does not grossly underfund a large grant. e.g. 
            # grantsArray = [8, 4, 2, 2, 2], newBudget = 10, cap could be 0 so we would pay 
            # 0 to the 8, and 4,2,2,2 to the rest
            # so cap must be > largest none-capped
            if cap > sortedgrantsArray[i+1]: 
                    return cap
    # 
    

        
# input:  grantsArray = [2, 100, 50, 120, 1000], newBudget = 190


def testing():
    grantsArray = [2, 2, 2, 2, 2] 
    newBudget = 10
    output = 2
    print(0, find_grants_cap(grantsArray, newBudget) == output)
    grantsArray = [2, 100, 50, 120, 1000] 
    newBudget = 190
    output = 47
    print(1, find_grants_cap(grantsArray, newBudget) == output)
    grantsArray = [2,4]
    newBudget = 3
    output = 1.5
    print(2, find_grants_cap(grantsArray, newBudget) == output)
    grantsArray = [2,4,6]
    newBudget = 3
    output = 1
    print(3, find_grants_cap(grantsArray, newBudget) == output)
    grantsArray = [2,100,50,120,167]
    newBudget = 400
    output = 128.0
    print(4, find_grants_cap(grantsArray, newBudget) == output)
    grantsArray = [21,100,50,120,130,110]
    newBudget = 140
    output = 23.8
    print(5, find_grants_cap(grantsArray, newBudget) == output)
    grantsArray = [210,200,150,193,130,110,209,342,117]
    newBudget = 1530
    output = 211
    print(6, find_grants_cap(grantsArray, newBudget) == output)
    grantsArray = [2, 2, 2, 2, 2] 
    newBudget = 12
    output = 2
    print(7, find_grants_cap(grantsArray, newBudget) == output)
    grantsArray = [2, 2, 4, 2, 2] 
    newBudget = 16
    output = 4
    print(8, find_grants_cap(grantsArray, newBudget) == output)
    grantsArray = [101, 102, 103, 104, 105] 
    newBudget = 100
    output = 20
    print(9, find_grants_cap(grantsArray, newBudget) == output)

# run tests
testing()


