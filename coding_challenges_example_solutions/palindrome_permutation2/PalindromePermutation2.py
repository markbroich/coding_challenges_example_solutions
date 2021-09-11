'''
Palindrome Permutation II
Leedcode 267


Given a string s, return all the palindromic permutations (without duplicates) 
of it.

You may return the answer in any order. If s has no palindromic permutation, 
return an empty list.

Example 1:
Input: s = 'aabb'
Output: ['abba','baab']

Example 2:
Input: s = 'abc'
Output: []
'''

import collections


# Ot(e!) Os(e) where e are items in list
# of evenly occuring items
# in the worth case e = n/2
def generatePalindromes(s):
    if not palindron_string(s):
        return -1
    else:
        # Ot(s) Os(s)
        myDict = pop_dict(s)
        # Ot(k) Os(k/2) where k is keycount
        evenLst, oddItem = evenlst_and_odditem(myDict)
        # Ot(e!) Os(e!) where e are items in evenLst
        permLst = permute_rec([], evenLst, [])
        # Ot(p * c/2) where p are permutations and c are
        # chars per permutation
        paliPermLst = [add_rev_and_odd(perm, oddItem) for perm in permLst]
        return [''.join(r) for r in paliPermLst]


# Ot(s) Os(s)
def palindron_string(s):
    occDict = pop_dict(s)
    oddCnt = count_odd(occDict)
    return oddCnt <= 1


# Ot(s) Os(s)
def pop_dict(s):
    myDict = {}
    for i in s:
        if i in myDict:
            myDict[i] += 1
        else:
            myDict[i] = 1
    return myDict


# Ot(s) Os(1)
def count_odd(myDict):
    oddCnt = 0
    for v in myDict.values():
        oddCnt += v % 2 > 0
    return oddCnt


# Ot(k) Os(k/2) where k is keycount
def evenlst_and_odditem(myDict):
    # at most one oddItem
    evenLst = []
    oddItem = None
    for key in myDict.keys():
        if myDict[key] % 2 == 1:
            oddItem = key
        f = int(myDict[key] / 2)
        evenLst = evenLst + ([key] * f)
    return evenLst, oddItem


# number of resulting permutations is n! if all n are different
# Ot(n!) Os(n) given that I need do and track all permutions
def permute_rec(prefix, remains, res):
    # if no more to permute, append combo
    if len(remains) == 0:
        res.append(prefix)
        return res
    else:
        myset = set()
        for i in range(0, len(remains)):
            # take out i element and append to prefix
            num = remains[i]
            # only recur if num has not yet been permuted
            # aka is not a duplicate
            if num not in myset:
                myset.add(num)
                remainsNew = remains[:i]+remains[i+1:]
                res = permute_rec(prefix+[num], remainsNew, res)
        return res


# Ot(n/2) # Os(2n)
def add_rev_and_odd(lst, oddItem=None):
    lenLst = len(lst)
    # there is at most one odd item
    if oddItem:
        lst.append(oddItem)
    # make slots for even items and bring in rev of even
    lst = lst + [''] * lenLst
    for i in range(0, lenLst):
        lst[-1 - i] = lst[i]
    return lst


# found this much shorter and faster code online...
def generatePalindromes_short(s):
    ans = []
    n = len(s)
    counter = collections.Counter(s)

    def helper(tmp):
        if len(tmp) == n:
            ans.append(tmp)
            return
        for k, v in counter.items():
            if v > 0:
                counter[k] -= 2
                helper(k + tmp + k)
                counter[k] += 2

    odd = [key for key, value in counter.items() if value % 2 != 0]
    if len(odd) > 1:
        return []
    if len(odd) == 1:
        counter[odd[0]] -= 1
        helper(odd[0])
    else:
        helper('')
    return ans


# run and test code
s = 'aabb'
exp = ['abba', 'baab']
print('1', generatePalindromes(s) == exp)

s = 'abc'
exp = -1
print('2', generatePalindromes(s) == exp)

s = 'aacbb'
exp = ['abcba', 'bacab']
print('3', generatePalindromes(s) == exp)

s = 'aaaacbb'
exp = ['aabcbaa', 'abacaba', 'baacaab']
print('4', generatePalindromes(s) == exp)

s = 'aaaaaaaacbb'
exp = ['aaaabcbaaaa', 'aaabacabaaa', 'aabaacaabaa', 'abaaacaaaba', 
       'baaaacaaaab']
print('5', generatePalindromes(s) == exp)

s = 'aaaaaaaacbbbb'
exp = ['aaaabbcbbaaaa', 'aaababcbabaaa', 'aaabbacabbaaa', 'aabaabcbaabaa', 
       'aababacababaa', 'aabbaacaabbaa', 'abaaabcbaaaba', 'abaabacabaaba', 
       'ababaacaababa', 'abbaaacaaabba', 'baaaabcbaaaab', 'baaabacabaaab', 
       'baabaacaabaab', 'babaaacaaabab', 'bbaaaacaaaabb']
print('6', generatePalindromes(s) == exp)

s = 'aabbccdd'
exp = ['abcddcba', 'abdccdba', 'acbddbca', 'acdbbdca', 'adbccbda', 'adcbbcda', 
       'bacddcab', 'badccdab', 'bcaddacb', 'bcdaadcb', 'bdaccadb', 'bdcaacdb', 
       'cabddbac', 'cadbbdac', 'cbaddabc', 'cbdaadbc', 'cdabbadc', 'cdbaabdc', 
       'dabccbad', 'dacbbcad', 'dbaccabd', 'dbcaacbd', 'dcabbacd', 'dcbaabcd']
print('7', generatePalindromes(s) == exp)

s = 'aaabb'
exp = ['ababa', 'baaab']
print('8', generatePalindromes(s) == exp)

s = 'aaacbb'
exp = -1
print('9', generatePalindromes(s) == exp)

# much faster code...
s = 'aaaaaaaacbbbb'
exp = ['bbaaaacaaaabb', 'babaaacaaabab', 'abbaaacaaabba', 'baabaacaabaab', 
       'ababaacaababa', 'aabbaacaabbaa', 'baaabacabaaab', 'abaabacabaaba', 
       'aababacababaa', 'aaabbacabbaaa', 'baaaabcbaaaab', 'abaaabcbaaaba', 
       'aabaabcbaabaa', 'aaababcbabaaa', 'aaaabbcbbaaaa']
print('10', generatePalindromes_short(s) == exp)
