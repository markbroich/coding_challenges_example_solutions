## Matching Pairs

# Given two strings s and t of length N, find the maximum number of possible matching pairs 
# in strings s and t after swapping exactly two characters within s.
# A swap is switching s[i] and s[j], where s[i] and s[j] denotes the 
# character that is present at the ith and jth index of s, respectively. 
# The matching pairs of the two strings are defined as the number of 
# indices for which s[i] and t[i] are equal.

# Note: This means you must swap two characters at different indices.

# Input
# s and t are strings 
# Output
# Return an integer denoting the maximum number of matching pairs

# Example 1
# s = "abcd"
# t = "adcb"
# output = 4
# Explanation:
# Using 0-based indexing, and with i = 1 and j = 3, s[1] and s[3] can be swapped, making it  "adcb".
# Therefore, the number of matching pairs of s and t will be 4.

# Example 2
# s = "mno"
# t = "mno"
# output = 1
# Explanation:
# Two indices have to be swapped, regardless of which two it is, only one letter will remain the same. 
# If i = 0 and j=1, s[0] and s[1] are swapped, making s = "nmo", which shares only "o" with t.


# Assuming that two arrays are of the same length, this problem is still rather hard 
# given the range of cases one needs to account for (e.g. tests at the end)

def matchPairs(s,t):
    base = 0 # matched count
    matched = {} 
    mismatched = [] # mismatched indicies
    for i in range(0, len(s)):
        c1 = s[i]
        c2 = t[i]
        if c1 == c2: 
            base += 1
            matched[c1] = 1 + matched.get(c1,0)
        else: mismatched.append(i)
    
    # condition I
    # if all matched and all chars are unique, any swap will result in -2
    if not mismatched and len(matched) == base: return base - 2

    # condition II
    # perfect swap for (c1, c2) if (c2, c1) is also a mismatch
    paired = set()
    for i in mismatched:
        if (s[i], t[i]) in paired: 
            return base + 2
        paired.add((t[i], s[i]))

    # condition III
    # swapping at least one char into place
    seen = set()
    for i in mismatched:
        seen.add(t[i])
    for i in mismatched: #if any(s[i] in seen for i in mismatched):
        if s[i] in seen: 
            return base + 1
    
    # condition IV
    # check if neutral swaps exists
    # So: result unchanged
    if len(mismatched) >= 2:
        return base

    # condition V
    # match occurs > 2 times so neutral swap 
    # So, result
    for count in matched.values():
        if count >= 2:
            return base

    # condition VI
    # a matched character occurs also as a mismatched character. So: result 
    for i in mismatched:
        if s[i] in matched:
            return base

    # condition VII
    # only one mismatched
    # So: result -1 
    return base - 1


### Tests

# condition I
# if all matched and all chars are unique, any swap will result in -2
s = "mno"
t = "mno"
print('Ia', matchPairs(s, t) == 1)
s = "abcd"
t = "abcd"
print('Ib', matchPairs(s, t) == 2)

# condition II
# perfect swap for (c1, c2) if (c2, c1) is also a mismatch, so: result +2
s = "abcdc"
t = "baccd"
print('IIa', matchPairs(s, t) == 3)
s = "abcdx"
t = "abxcc"
print('IIb', matchPairs(s, t) == 4)
s = "abcd"
t = "adcb"
print('IIc', matchPairs(s, t) == 4)
s = "abcde"
t = "adcbe"
print('IId', matchPairs(s, t) == 5)

# condition III
# swapping at least one char into place
s = "mnode"
t = "mnoef"
print('IIIa', matchPairs(s, t) == 4)
s= "mnode"
t= "mnoef"
print('IIIb', matchPairs(s, t) == 4)
s = "abcde"
t = "axcbe"
print('IIIc', matchPairs(s, t) == 4)

# condition VII 
# only one mismatched
# So: result -1 
s = "abcd"
t = "abce"
print('VIIa', matchPairs(s, t) == 2)
s = "abc"
t = "abd"
print('VIIb', matchPairs(s, t) == 1)

# condition IV
# check if neutral swaps exists
# So: result unchanged
s = "abcd"
t = "efgh"
print('IVa', matchPairs(s, t) == 0)
s = "abcd"
t = "abyz"
print('IVb', matchPairs(s, t) == 2)
s = "abczz"
t = "abcee"
print('IVc', matchPairs(s, t) == 3)

# condition V
# match occurs > 2 times so neutral swap 
# So, result
s = "abcda"
t = "axcda"
print('V', matchPairs(s, t) == 4)

# condition VI
# a matched character occurs also as a mismatched character. 
# So: result unchanged given gain 1 loose 1
s = "abcda"
t = "xbcda"
print('VI', matchPairs(s, t) ==4)



# with a lot of inspiration from: 
# https://leetcode.com/discuss/interview-question/632717/Facebook-or-Recruiting-Portal-or-Matching-Pairs



