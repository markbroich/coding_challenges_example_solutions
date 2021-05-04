# Name occurrence 

# task is to return a list of tupels formed by 
# names and their occurrence counts 


# The return list should only include names that 
# either do not occur in the synonyms (e.g. Max) or occur only 
# on the right and side in the synonyms (e.g. Mike, Jennifer)

names = [
    ('Jen',1), 
    ('Jenny',2), 
    ('Tom',9), 
    ('Max',8), 
    ('Thomas',12),
    ('Jennifer',3), 
    ('Evi',1), 
    ('Luc',5), 
    ('Lisa',3)
]

synonyms = [
    ('Jen','Jenny'),
    ('Michael','Mike'),
    ('Thomas','Tom'),
    ('Jenny','Jennifer'),
    ('Eva','Evi')
]

expected = [
    ('Evi', 1),
    ('Jennifer',6),
    ('Lisa', 3),
    ('Luc', 5),
    ('Max',8),
    ('Tom',21),
    ]

# time O(len(synonyms))
# space O(len(synonyms) * 2)
def init_dicts(synonyms):
    cntDict = {}
    transDict = {}
    for l,r in synonyms:
        # final count dict w key = rhs
        if not r in cntDict:
            cntDict[r] = 0
        # translation dict
        if not l in transDict:
            transDict[l] = r
    return cntDict, transDict

# time O(len(names)) 
# space O(1)
def pop_cntDict(names, cntDict, transDict):
    for name, cnt in names:
        # if name w/o synonym and not yet seen in names Lst
        if name not in cntDict and not name in transDict:
            cntDict[name] = cnt
        # # if rhs name simply add
        elif name in cntDict:
            cntDict[name] += cnt
        elif name in transDict: 
            # translate to rhs
            name = transDict[name]
            cntDict[name] += cnt
    return cntDict

# time: O(len(cntDict)) ~ len(synonyms)
# space O(1)
def remap_false_rhs(cntDict, transDict):
    for name in cntDict:
        if name in transDict: 
            cnt = cntDict[name]
            # translate to rhs
            nameRhs = transDict[name]               
            cntDict[nameRhs] += cnt
            cntDict[name] = 0
    return cntDict

# time: O(len(cntDict)) ~ len(synonyms)
# space: O(len(cntDict)) ~ len(synonyms)
def app_gr_zero_cnt_to_resLst(cntDict):
    retLst = []
    for name in cntDict:
        if cntDict[name] > 0:
            retLst.append((name, cntDict[name])) 
    return retLst


# Main function: 

# total time and space complexity:
# time: O(max(len(synonyms)), O(len(names))) given: 
# O(len(synonyms)) + O(len(names)) + O(len(synonyms) 
# + O(len(cntDict)) ~ len(synonyms) + O(nlogn) 
# [O(nlogn) can be dropped as it is only cosmetical]

# space: O(len(synonyms))+len(unique names not in synonyms)) 
# given: O(len(synonyms)) * 2 + 
# O(len(unique names not in synonyms)) + 
# O(1) + O(len(synonyms)) + O(1)

def name_occ(names, synonyms):
    if not names or not synonyms:
        # bad input
        return -1

    # time O(len(synonyms))
    # space O(len(synonyms)) * 2
    cntDict, transDict = init_dicts(synonyms)
    #
    # time O(len(names)) 
    # space O(len(unique names not in synonyms))
    cntDict = pop_cntDict(names, cntDict, transDict)

    # there are false rhs keys (that in turn have a rhs)
    # e.g. Jenny is a rhs but in turn has rhs Jennifer
    # time: O(len(cntDict)) ~ len(synonyms)
    # space O(1)
    cntDict = remap_false_rhs(cntDict, transDict)
    #
    # time: O(len(cntDict)) ~ len(synonyms)
    # space: O(len(cntDict)) ~ len(synonyms) 
    # could be space O(1) if we return an existing dict
    retLst = app_gr_zero_cnt_to_resLst(cntDict)

    # sort for appearacne 
    # can be dropped as it drive up the time complexity
    # time O(nlogn)
    # space O(1)
    retLst.sort()
    # 
    return retLst

    
def testing():
    # test 1
    names = [
        ('Jen',1), 
        ('Jenny',2), 
        ('Tom',9), 
        ('Max',8), 
        ('Thomas',12),
        ('Jennifer',3), 
        ('Evi',1), 
        ('Luc',5), 
        ('Lisa',3)
    ]

    synonyms = [
        ('Jen','Jenny'),
        ('Michael','Mike'),
        ('Thomas','Tom'),
        ('Jenny','Jennifer'),
        ('Eva','Evi')
    ]

    expected = [
        ('Evi', 1),
        ('Jennifer',6),
        ('Lisa', 3),
        ('Luc', 5),
        ('Max',8),
        ('Tom',21),
        ]
    print('test 1:', name_occ(names, synonyms) == expected)


# run test
testing()