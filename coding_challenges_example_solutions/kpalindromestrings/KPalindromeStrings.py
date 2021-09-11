'''

Given a string s and an integer k. You should construct k non-empty palindrome strings using all the characters in s.

Return True if you can use all the characters in s to construct k palindrome strings or False otherwise.
# Palindrome: A word, phrase, verse, or sentence that reads the same backward or forward

 

Example 1:
Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

Example 2:
Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.

Example 3:
Input: s = "yzyzyzyzyzyzyzy", k = 2
Output: true
Explanation: Simply you can put all z's in one string and all y's in the other string. Both strings will be palindrome.

Example 4:
Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.

Example 5:
Input: s = "cr", k = 7
Output: false
Explanation: We don't have enough characters in s to construct 7 palindromes.
 

Constraints:

1 <= s.length <= 10^5
All characters in s are lower-case English letters.
1 <= k <= 10^5
'''

# rephrasing the problem: 
# a single character string is reversable 
# if k strings are the results but s has < k chars, then false
#
# a string can be reversed if zero or one character occures an odd number of times. 
# hence the number of characters that occures an odd number of times can be at most k
# so, the apporach is to create an occurance count dict, count the number of odd occurances
# and compare the number of odd occurances with k



# Ot(s) Os(s)
def k_palindron_string(s, k):
    if len(s) == k: 
        return  True
    if len(s) < k: 
        return False 
    occDict = pop_dict(s)
    oddCnt = count_odd(occDict) 
    res = oddCnt <= k
    return res

# Ot(s) Os(s)
def pop_dict(s):
    myDict = {}
    for i in s:
        if i in myDict:
            myDict[i] +=1
        else:
            myDict[i] = 1
    return myDict

# Ot(s) Os(1)
def count_odd(myDict):
    oddCnt = 0
    for v in myDict.values():
        oddCnt += v%2 > 0
    return oddCnt


# run the code
s = "annabelle"
k = 2
exp = True
print(k_palindron_string(s, k) == exp)

s = "leetcode"
k = 3
exp = False
print(k_palindron_string(s, k) == exp)

s = "yzyzyzyzyzyzyzy"
k = 2
exp = True
print(k_palindron_string(s, k) == exp)

s = "true"
k = 4
exp = True
print(k_palindron_string(s, k) == exp)

s = "cr"
k = 7
exp = False
print(k_palindron_string(s, k) == exp)

s = "messi"
k = 3
exp = True
print(k_palindron_string(s, k) == exp)

