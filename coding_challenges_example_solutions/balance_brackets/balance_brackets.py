'''
Balance Brackets

A bracket is any of the following characters: (, ), {, }, [, or ].
We consider two brackets to be matching if the first bracket is an
open-bracket, e.g., (, {, or [, and the second bracket is a close-bracket of
the same type. That means ( and ), [ and ], and { and } are the only pairs of
matching brackets.
Furthermore, a sequence of brackets is said to be balanced if the following
conditions are met:
1) The sequence is empty, or
2) The sequence is composed of two or more non-empty sequences, all of which are
balanced, or
3) The first and last brackets of the sequence are matching, and the portion of
the sequence without the first and last elements is balanced.
You are given a string of brackets. Your task is to determine whether each
sequence of brackets is balanced. If a string is balanced, return true,
otherwise, return false

Signature
bool isBalanced(String s)

Input
String s with length between 1 and 1000

Output
A boolean representing if the string is balanced or not

Example 1
s = {[()]}
output: true

Example 2
s = {}()
output: true

Example 3
s = {(})
output: false

Example 4
s = )
output: false
'''

# Ot(n) 
# Os(n) if all chars are opeining brackets
def isBalanced(s):
    st = []
    i = 0
    for i in range(0, len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            st.append(s[i])
        elif (s[i] == ')' or s[i] == '}' or s[i] == ']'):
            if not st:
                return False
            ob = st.pop()
            if (s[i] == ')' and ob != '(' or
                s[i] == '}' and ob != '{' or
                s[i] == ']' and ob != '['):
                return False
    if st:
        return False
    return True

# Example 1
s = '{[()]}'
exp = True
print(isBalanced(s) == exp)

# Example 2
s = '{}()'
exp = True
print(isBalanced(s) == exp)

# Example 3
s = '{(})'
exp = False
print(isBalanced(s) == exp)

# # Example 4
s = ')'
exp = False
print(isBalanced(s) == exp)

# Example 5
s = ''
exp = True
print(isBalanced(s) == exp)

# Example 6
s = '912f'
exp = True
print(isBalanced(s) == exp)

# Example 7
s = '9(12f'
exp = False
print(isBalanced(s) == exp)

# Example 8
s = '912}f'
exp = False
print(isBalanced(s) == exp)

# Example 9
s = '912}f'
exp = False
print(isBalanced(s) == exp)

# Example 10
s = '(9{1[]2}f)'
exp = True
print(isBalanced(s) == exp)