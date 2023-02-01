'''
Longest Substring Without Repeating Characters


Given a string s, find the length of the longest
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a
subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''


# Ot(n) Os(k) where n is len of string and k is unique letters in string
def longest_substr_no_repeat(s: list) -> int:
    if not s:
        return -1
    longest = float('-inf')
    str_start = 0
    bookkeeping = {}
    for i in range(len(s)):
        if s[i] in bookkeeping and bookkeeping[s[i]] >= str_start:
            longest = max(longest, i - str_start)
            str_start = bookkeeping[s[i]] + 1
        bookkeeping[s[i]] = i
    return longest


def tests():
    s = "abcabcbb"
    expected = 3
    print(longest_substr_no_repeat(s) == expected)

    s = "bbbbb"
    expected = 1
    print(longest_substr_no_repeat(s) == expected)

    s = "pwwkew"
    expected = 3
    print(longest_substr_no_repeat(s) == expected)

    s = "abcaxyzbcbb"
    expected = 6
    print(longest_substr_no_repeat(s) == expected)

    s = "fabcaxyzbfcbb"
    expected = 7
    print(longest_substr_no_repeat(s) == expected)

    s = "pwwkepw"
    expected = 4
    print(longest_substr_no_repeat(s) == expected)


tests()
