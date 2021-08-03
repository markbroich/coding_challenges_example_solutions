# Sorting fun 

# The tax office needs to prioritize cases for review.
# The cases all have a alphanumeric id and metadata.
# Urgent cases have metadata that consist of a space separated lowercase characters.  
# None urgent cases have metadata consisting of space separated positive integers. 
# Each case thus has a alphanumeric id followed by a space followed
# by space delimited metadata.

# Task: First return urgent cases sorted lexicographically on their 
# Metadata. if there are ties, items are to be sorted by id  
# None priority cases are to be return second in their original order


# Ot(n*c) where n is items in lst and c is number of metadata chars
# Os(n)
def split_by_priority(lst):
    priorityLst = []
    noPriorityLst = []
    for order in lst:
        subLst = order.split(' ')
        if any([subLst[i].isalpha() for i in range(1, len(subLst))]):
            priorityLst.append(subLst)
        else:
            noPriorityLst.append(subLst)
    return priorityLst, noPriorityLst

# Ot(n*c) where n is items in lst and c is number of metadata chars
# or Ot(nlogn)
# Os(n)
def sort_orders(orderLst):
    priorityLst, noPriorityLst = split_by_priority(orderLst)
    # Ot(nlogn), Os(1)
    priorityLst.sort(key=lambda a: (a[1], a[0]))
    
    # Os(n)
    orderLstSorted = priorityLst + noPriorityLst
    # Ot(n), Os(1)
    orderLstSorted = [' '.join(sublst) for sublst in orderLstSorted]
    return orderLstSorted


# ex1
orderLst = [
    '8 b b c',
    '1 z y x w',
    '3 9 8 7', 
    '7 b b c',
    '9 a b c',
    '2 1 2 3'
]

exp = [
    '9 a b c',
    '7 b b c',
    '8 b b c',
    '1 z y x w',
    '3 9 8 7', 
    '2 1 2 3'
]
print(sort_orders(orderLst) == exp) 


# ex2
orderLst = [
    '8 b b c',
    '1 z y x w',
    '7 b b c',
    '9 a b c'
]

exp = [
    '9 a b c',
    '7 b b c',
    '8 b b c',
    '1 z y x w'
]
print(sort_orders(orderLst) == exp) 


# ex3
orderLst = [
    '3 9 8 7', 
    '2 1 2 3'
]

exp = [
    '3 9 8 7', 
    '2 1 2 3'
]
print(sort_orders(orderLst) == exp) 



# ex4
orderLst = []
exp = []
print(sort_orders(orderLst) == exp) 

