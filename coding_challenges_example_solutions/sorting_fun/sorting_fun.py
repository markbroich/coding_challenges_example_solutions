'''
Sorting fun (done 3 ways)

The tax office needs to prioritize cases for review.
The cases all have a alphanumeric id and metadata.
Urgent cases have metadata that consist of a space separated lowercase characters.  
None urgent cases have metadata consisting of space separated positive integers. 
Each case thus has a alphanumeric id followed by a space followed
by space delimited metadata.

Task: First return urgent cases sorted lexicographically on their 
Metadata. if there are ties, items are to be sorted by id  
None priority cases are to be return second in their original order
'''


# Ot(n*c + k*m*log(m)) where n is items in lst and c is number of metadata
# chars, m is length of priority ID lst and k the number of sorting criteria
# (here either the average or the max number of metadata chars)
# Os(n)
def sort_ordersA(orderLst):
    priorityLst, noPriorityLst = split_by_priorityA(orderLst)
    # Ot(kmlogm), Os(1)
    priorityLst.sort(key=lambda a: (a[1], a[0]))
    # Os(n)
    orderLstSorted = priorityLst + noPriorityLst
    # Ot(n), Os(1)
    orderLstSorted = [' '.join(sublst) for sublst in orderLstSorted]
    return orderLstSorted


# Ot(n*c) where n is items in lst and c is number of metadata chars
# Os(n)
def split_by_priorityA(lst):
    priorityLst = []
    noPriorityLst = []
    for order in lst:
        subLst = order.split(' ')
        if any([subLst[i].isalpha() for i in range(1, len(subLst))]):
            priorityLst.append(subLst)
        else:
            noPriorityLst.append(subLst)
    return priorityLst, noPriorityLst


#####################################################################
# Ot(n*c + k*m*log(m)) where n is items in lst and c is number of metadata
# chars, m is length of priority ID lst and k the number of sorting criteria
# (here either the average or the max number of metadata chars)
# Os(n)
def sort_ordersB(orderLst):
    priorityLst, noPriorityLst = split_by_priorityB(orderLst)
    # Ot(kmlogm), Os(1)
    priorityLst.sort()
    # flips the order od Lst items back to desired order and converts to string
    # Ot(m*2), Os(1) where m is len of priority lst
    priorityLst = [' '.join(sublst[::-1]) for sublst in priorityLst]
    # Os(n)
    return priorityLst + noPriorityLst


# Ot(n*c) where n is items in lst and c is number of metadata chars
# Os(n)
def split_by_priorityB(lst):
    priorityLst = []
    noPriorityLst = []
    for order in lst:
        subLst = order.split(' ')
        # only one check for alpha is needed
        if subLst[-1].isalpha():
            # a Lst with two slots: metadata as string, id
            # (takes len of parts c to create)
            priorityLst.append([' '.join(subLst[1:]), subLst[0]])
        else:
            # Lst of strings
            # (takes len of parts c to create)
            noPriorityLst.append(' '.join(subLst))
    return priorityLst, noPriorityLst


#####################################################################
# Ot(n*c + m*log(m) * g*log(h)) where n is items in lst and c is number of
# metadata chars, g is the number of items with duplicated metadata string
# and  h is the avergae or max number of IDs per metadata string
# Os(n)
def sort_ordersC(lst):
    priorityLst = []
    priorityID, IdDict, noPriorityLst = split_by_priorityC(orderLst)
    # Ot(mlogm) where m is length of priority ID lst
    priorityID.sort()
    seen = set()
    # Ot(g* hlog(h))
    for pId in priorityID:
        if pId not in seen:
            # Ot(glogh) where c is length numbers per ID
            for currNo in sorted(IdDict[pId]):
                priorityLst.append(currNo + ' ' + pId)
            seen.add(pId)
    return priorityLst + noPriorityLst

# Ot(n*c) where n is items in lst and c is number of metadata chars
# Os(n)
def split_by_priorityC(lst):
    priorityID = []
    IdDict = {}
    noPriorityLst = []
    for order in lst:
        subLst = order.split(' ')
        if subLst[-1].isalpha():
            priorityID.append((' '.join(subLst[1:])))
            id = ' '.join(subLst[1:])
            if id in IdDict:
                IdDict[id] = (IdDict[id], subLst[0])
            else:
                IdDict[id] = (subLst[0])
        else:
            noPriorityLst.append(' '.join(subLst))
    return priorityID, IdDict, noPriorityLst


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
print(sort_ordersA(orderLst) == exp)
print(sort_ordersB(orderLst) == exp)
print(sort_ordersC(orderLst) == exp)


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
print(sort_ordersA(orderLst) == exp)
print(sort_ordersB(orderLst) == exp)
print(sort_ordersC(orderLst) == exp)

# ex3
orderLst = [
    '3 9 8 7',
    '2 1 2 3'
]

exp = [
    '3 9 8 7',
    '2 1 2 3'
]
print(sort_ordersA(orderLst) == exp)
print(sort_ordersB(orderLst) == exp)
print(sort_ordersC(orderLst) == exp)



# ex4
orderLst = []
exp = []
print(sort_ordersA(orderLst) == exp) 
print(sort_ordersB(orderLst) == exp) 
print(sort_ordersC(orderLst) == exp) 




# urgents = [(a b c), (b b c), (b,b,c), (z,y,x,w)]
# non_urgent = [    '3 9 8 7',  '2 1 2 3']
# id = {
#     (b,b,c) -> [8, 7],
#     (z,y,x,w) -> [1],
#     (a b c) -> [9]
# }

# urgents.sort()

# visited = set()
# sorted_urgents = []
# for urgent in urgents:
#     if urgent is not in visited:
#         for curr_id in sorted(id[urget]):
#             sorted_urgents.append(' '.join((curr_id) + urgent)
#     visited.add(urgent)
                      
# return sorted_urgents + non_urgents

