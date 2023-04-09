"""
Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""


# Ot(n)
def is_palindromic_str(s):
    return s == s[::-1] 


# Ot(n**3)
def find_longest_palindromic_str(s):
    max_length = float('-inf')
    i_longest = 0
    j_lognest = 0
    for i in range(len(s) - 1):
        for j in range(i + 2, len(s)):
            if is_palindromic_str(s[i:j]):
                if max_length < j - i:
                    max_length = j - i
                    i_longest = i
                    j_lognest = j
    return s[i_longest:j_lognest]


# Ot(n**2)
def find_longest_palindromic_str_faster(s):
    longest = left_longest = right_longest = 0
    for i in range(len(s)):
        left, right = left_right_of_palindromic_str(s, i)
        if right - left > longest:
            longest = right - left
            left_longest = left
            right_longest = right
    return s[left_longest: right_longest + 1]


# helper: Ot(n)
def left_right_of_palindromic_str(s, i):
    if i == 0 or i == len(s) - 1:
        return i, i
    left = right = i
    while left > 0 and right < len(s) - 1:
        if s[left - 1] == s[right + 1]:
            left -= 1
            right += 1
        elif s[left - 1] == s[right]:
            left -= 1
        else:
            break
    return left, right


def tests():
    s = "babad"
    expected = "bab"
    # Explanation: "aba" is also a valid answer.
    print(find_longest_palindromic_str(s) == expected)
    print(find_longest_palindromic_str_faster(s) == expected)

    s = "cbbd"
    expected = "bb"
    print(find_longest_palindromic_str(s) == expected)
    print(find_longest_palindromic_str_faster(s) == expected)

    s = "fogrgeeksskeegfor"
    expected = "geeksskeeg"
    print(find_longest_palindromic_str(s) == expected)
    print(find_longest_palindromic_str_faster(s) == expected)

    s = "forgeeksskeegfor"
    expected = "geeksskeeg"
    print(find_longest_palindromic_str(s) == expected)
    print(find_longest_palindromic_str_faster(s) == expected)

    s = "Geeks"
    expected = "ee"
    print(find_longest_palindromic_str(s) == expected)
    print(find_longest_palindromic_str_faster(s) == expected)


tests()
