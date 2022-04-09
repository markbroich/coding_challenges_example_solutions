'''
Longest common prefix:

Write a function to find the longest common prefix string amongst an array of
strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''


# Brute forth solution.
# Ot(n * s), Os(s) where n is number of words
# and s shortest word
def longest_common_prefix(strs: list) -> str:
    if not strs:
        return -1
    if len(strs) == 1:
        return strs[0]
    common_prefix = ''
    idx = 0
    while True:
        cur_letter = strs[0][idx]
        break_flag = 0
        for word in strs:
            if word[idx] != cur_letter:
                break_flag = 1
                break
        if break_flag:
            break
        common_prefix = common_prefix + word[idx]
        idx += 1
    return common_prefix


# A faster solution using binary search:
# Ot(n * log(s) * n) where n is number of words
# and s is the length of the shortest word
# Ot(n + ) where n is len of lst
def longest_common_prefix_binary(strs: list) -> str:
    '''Returns index of longest common substring using bianry search'''
    if not strs:
        return -1
    if len(strs) == 1:
        return strs[0]
    idx_lower = 0
    # Ot(n), Os(1)
    idx_upper = min_word_len(strs) - 1
    # Ot(n * log(s) * n), Os(1)
    idx = binary_search(idx_lower, idx_upper, strs)
    if idx == -1:
        return ''
    return strs[0][0:idx]


# Ot(n) where n is len of lst; Os(1)
def min_word_len(strs: list) -> int:
    '''return length of shortest word.'''
    word_length = float('inf')
    for word in strs:
        word_length = min(word_length, len(word))
    return word_length


# Ot(log(s) * n), Os(1)
# where s is the inital difference between idx_lower and idx_upper
# and n is the len of the lst
def binary_search(idx_lower: int, idx_upper: int, strs: list) -> int:
    '''Returns index of longest common substring.
    Search starts from upper idx 0 and lower idx == idx of the shortes word.
    Returns -1 if longest common substring does not exist.
    '''
    while idx_lower < idx_upper:
        idx = idx_lower + int((idx_upper - idx_lower) / 2)
        cur_letter = strs[0][idx]
        match = True
        for word in strs:
            match = match and word[idx] == cur_letter
            if not match:
                idx_upper = idx - 1
                break
        if match:
            idx_lower = idx
    if not match and idx == 1:
        return -1
    return idx


def tests() -> None:
    # ex 1
    strs = ["flower", "flow", "flight"]
    exp = "fl"
    print(longest_common_prefix(strs) == exp)
    print(longest_common_prefix_binary(strs) == exp)

    # ex 2
    strs = ["dog", "racecar", "car"]
    exp = ""
    print(longest_common_prefix(strs) == exp)
    print(longest_common_prefix_binary(strs)  == exp)

    # ex 3
    strs = ["dog"]
    exp = "dog"
    print(longest_common_prefix(strs) == exp)
    print(longest_common_prefix_binary(strs) == exp)


def main():
    tests()


if __name__ == "__main__":
    main()