'''
Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''


from collections import defaultdict


def group_anagrams(words: list) -> list:
    dict_of_sets = defaultdict(set)
    for word in words:
        encoding = [0] * 26
        for char in word:
            encoding[ord(char) - ord('a')] += 1
        dict_of_sets[tuple(encoding)].add(word)
    return [v for v in dict_of_sets.values()]


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
expected = [{"eat", "tea", "ate"}, {"tan", "nat"},  {"bat"}]
print(group_anagrams(words) == expected)

words = [""]
expected = [{""}]
print(group_anagrams(words) == expected)

words = ["a"]
expected = [{"a"}]
print(group_anagrams(words) == expected)
