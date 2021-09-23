'''
291. Word Pattern II

Given a pattern and a string s, return true if s matches the pattern.

A string s matches a pattern if there is some bijective mapping of single
characters to strings such that if each character in pattern is replaced
by the string it maps to, then the resulting string is s. A bijective
mapping means that no two characters map to the same string, and no
character maps to two different strings.


Example 1:
Input: pattern = "abab", s = "redblueredblue"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "red"
'b' -> "blue"

Example 2:
Input: pattern = "aaaa", s = "asdasdasdasd"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "asd"

Example 3:
Input: pattern = "abab", s = "asdasdasdasd"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "a"
'b' -> "sdasd"
Note that 'a' and 'b' cannot both map to "asd" since the mapping is a bijection.

Example 4:
Input: pattern = "aabb", s = "xyzabcxzyabc"
Output: false 

Constraints:
1 <= pattern.length, s.length <= 20
pattern and s consist of only lower-case English letters.
'''




def solve(p, s):
    if not s or not p:
        return False

    def dfs(p, s, mapping):
        if not s and not p:
            return True
        elif not s or not p:
            return False
        
        if p[0] in mapping:
            if s[:len(mapping[p[0]])] != mapping[p[0]]: 
                return False
            return dfs(p[1:], s[len(mapping[p[0]]):], mapping)
        for i in range(1, len(s)-len(p)):
            # len(s)-len(p) speeds up code given that 
            # by the time i reaches end of s, 
            # the at least len(p) chars would have been mapped
            # if correct solution so, no need to consider them
            mapping[p[0]] = s[:i]
            if dfs(p[1:], s[len(mapping[p[0]]):], mapping): 
                return True
            del mapping[p[0]]
        return False

    return dfs(p, s, {})        

pattern = "abab"
s = "redblueredblue"
print(solve(pattern, s) == True)

pattern = "aaaa"
s = "asdasdasdasd"
print(solve(pattern, s) == True)


pattern = "abab"
s = "asdasdasdasd"
print(solve(pattern, s) == True)

pattern = "aabb"
s = "xyzabcxzyabc"
print(solve(pattern, s) == False)







