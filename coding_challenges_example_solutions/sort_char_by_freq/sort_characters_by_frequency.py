
# Sort Characters By Frequency

# Given a string, sort it in decreasing order based on the frequency of characters.

# Example 1:
# Input:
# "tree"

# Output:
# "eert"


# using python in builds

# Ot(nlogn) Os(n)
def sort_by_freq(string):
    # sort string (Ot(nlogn), Os(n))
    lstSortedSt = sorted(string)
    # concat string (Ot(n), Os(n))
    stSorted = concat_sting(lstSortedSt)
    # break up string (Ot(n), Os(n))
    lstOfSt = break_string(stSorted)
    # sort list (Ot(nlogn), Os(1))
    lstOfSt.sort(key=len, reverse=True)
    # concat string (Ot(n), Os(n))
    return concat_sting(lstOfSt)

def break_string(stSorted):
    lstOfSt = []
    lastIndex = 0
    for i in range(1,len(stSorted)):
        if stSorted[i] != stSorted[i-1]:
               lstOfSt.append(stSorted[lastIndex:i]) 
               lastIndex = i
    lstOfSt.append(stSorted[lastIndex:]) 
    return lstOfSt

def concat_sting(lst):
    result = ""
    for i in range(0,len(lst)):
        result = result+str(lst[i])
    return result

# or using in built
def listToString(lst):
    return ("".join(lst))

def testing():
    string = "cccaaa"
    expected = "aaaccc"
    print(sort_by_freq(string) == expected)

    string = "tree"
    expected = "eert"
    print(sort_by_freq(string) == expected)

    string = "Aabb"
    expected = "bbAa"
    print(sort_by_freq(string) == expected)

testing()

