'''
Decode Variations

A letter can be encoded to a number in the following way:

'A' -> '1', 'B' -> '2', 'C' -> '3', ..., 'Z' -> '26'
A message is a string of uppercase letters, and it is encoded first using this scheme. For example, 'AZB' -> '1262'

Given a string of digits S from 0-9 representing an encoded message, return the number of ways to decode it.

Examples:

input:  S = '1262'
output: 3
explanation: There are 3 messages that encode to '1262': 'AZB', 'ABFB', and 'LFB'.
Constraints:

[time limit] 5000ms

[input] string S

1 ≤ S.length ≤ 12
[output] integer
'''

# Memoization prunes the complexity which would otherwise be exponential.

# Ot:
# O(N), where is length of the string. Memoization pruns the
# recursion tree and hence I decode a substring only once.
# Would be O(2^n) given that each recusions calls 2 new recursions

# Os:
# # O(N). The memo takes the space
# equal to the length of the string. There would be an entry for each
# substring. The recursion stack would also be equal to the length
# of the string.


def decodeVariations(S):
    memo = {}
    def dfs(S):
        if S not in memo:    
            if len(S) == 0:
                return 1
            out = 0
            num = ''
            for i in [0, 1]:
                if i < len(S): 
                    num = num + S[i]
                    if int(num) > 26 or int(num) == 0:
                        break
                    out += dfs(S[i+1:])
            memo[S] = out
        return memo[S]
    return dfs(S)


# Test Case #1
S = "1262"
exp = 3
print(decodeVariations(S) == exp)
# Test Case #2
S = "26"
exp = 2
print(decodeVariations(S) == exp)
# Test Case #3
S = "127"
exp = 2
print(decodeVariations(S) == exp)
# Test Case #4
S = "1270"
exp = 0
print(decodeVariations(S) == exp)
# Test Case #5
S = "83778549129"
exp = 2
print(decodeVariations(S) == exp)
# Test Case #6
S = "8254779486"
exp = 2
print(decodeVariations(S) == exp)
# Test Case #7
S = "122231131122"
exp = 120
print(decodeVariations(S) == exp)
# Test Case #8
S = "122212313113"
exp = 126
print(decodeVariations(S) == exp)
# Test Case #9
S = "321121311231"
exp = 65
print(decodeVariations(S) == exp)


