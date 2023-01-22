'''Given a string S and a set of words D, find the longest word in D that is
a subsequence of S.

Word W is a subsequence of S if some number of characters, possibly zero, can
be deleted from S
to form W, without reordering the remaining characters.

Note: D can appear in any format (list, hash table, prefix tree, etc).

For example, given the input of S = "abppplee" and
D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would
be "apple"

The words "able" and "ale" are both subsequences of S, but they are shorter
than "apple".
The word "bale" is not a subsequence of S because even though S has all the
right letters, they are not in the right order.
The word "kangaroo" is the longest word in D, but it isn't
a subsequence of S.

From: https://techdevguide.withgoogle.com/resources/former-interview-question-find-longest-word/#!
'''


'''
Solution ideas:

1) Brute force
Generate all 2^n possible subsequences, and check each one against
the dictionary for a match.
A slight optimization is to at least ensure the dictionary is represented by
a hash table or prefix tree so that lookups are efficient.


2) Check each dictionary word using a greedy algorithm
You can prove that a greedy algorithm that checks if a word w is a subsequence
of S.
Scan S from the beginning for w[0].
After you find it, continue scanning from that point for w[1], and so on,
until either you run out of characters in S
(w is not a subsequence), or you find all the characters in w
(w is a subsequence).

You could sort the dictionary words in order of descending length,
run the above decision procedure for each word,
and take the first word that is a subsequence of S.
The running time is O(N*W) where W is the number of words in D and N
is the number of characters in S.

O(N*W) is asymptotically optimal if most dictionary words are close to size N
(because then the size of the input is O(N*W)).
However, it is far from optimal in a worst-case scenario where S may be long
and the dictionary strings quite short.

Define L to be the total number of characters in the dictionary over all
words. Then the best possible time complexity
(assuming words shorter than S) is O(N + L).
However, the existing algorithm is O(N * W),
which might be O(N * L) in the case where dictionary words are a small
constant in size.


3) Improving the greedy approach using bianry search
Notice that to check a dictionary word w, you end up needing to know,
for each character c in w, the least index i in S where S[i] == c,
such that i is greater than some given index j
(the index of the previously-matched letter).
Observe that the greedy algorithm is slow precisely
because it naively scans for this index i.
This improved approach requires one binary search per dictionary letter.


4) An optimal O(N + L) approach for any alphabet
Instead of processing the words one at a time,
we will process all words simultaneously.
'''


################################################################
# 1) Brute force
# O(2**n) where n is length of s.
def find_longest_word_brute_forth(s: str, d: set) -> str:
    # O(d) where d is length of d
    min_word_length = min(len(w) for w in d)

    # O(2**n) where n is length of s.
    def rec(sub_st: str, i: int) -> tuple:
        if not sub_st or len(sub_st) < min_word_length or i == len(sub_st):
            return 0, sub_st
        if sub_st in d:
            return len(sub_st), sub_st
        len_a, w_a = rec(sub_st[:i] + sub_st[i + 1:], i)
        len_b, w_b = rec(sub_st, i + 1)
        if len_a > len_b:
            return len_a, w_a
        return len_b, w_b
    res = rec(s, 0)
    if res[0] == 0:
        return ''
    return res[1]


# 2) Check each dictionary word using a greedy algorithm
# Ot(nlog(n) + n * k) where n is length of s and k is len of d.
# is ~optimal if length of most words in d is ~ len(s). But:
# for a long s and lots of short words in d, Ot is bad.
# Runtime complexity is O(n * l) in the case where
# words are a small constant in size but with many words.
# (l is total number of characters in the dictionary over all words)
# Os(1)
def find_longest_word_greedy(s: str, d: set) -> str:
    max_length = 0
    longest_word = ''
    # sorting in decrerasing length
    d = [i for i in d]
    d.sort(key=lambda a: -len(a))

    for word in d:
        i = 0
        for char in s:
            if char == word[i]:
                i += 1
            # if s is a subsequence of word
            if i == len(word) - 1:
                if len(word) > max_length:
                    max_length = len(word)
                    longest_word = word
                break
    return longest_word


# 3) Improving the greedy approach using bianry search
# Ot(n log(n) + n + l * log(n)) where
# l is total number of characters in the dictionary over all words
# Os(s) the letter_occurance_indices takes additonal space proportinal to s.
def find_longest_word_greedy_faster(s: str, d: set) -> str:
    # sorting in decrerasing length
    d = [i for i in d]
    d.sort(key=lambda a: -len(a))
    # e.g. 'abppplee' becomes: {'a': [0], 'b': [1], 'c': [2, 3, 4], 'l': [5],
    # 'e': [6, 7]}
    letter_occurance_indices = build_index_of_letter_occurance(s)
    longest_word = ''
    for word in d:
        last_matched_idx = -1
        for char in word:
            if char not in letter_occurance_indices\
                    or letter_occurance_indices[char][-1]\
                    < last_matched_idx:
                last_matched_idx = -1
                break
            idx_list = letter_occurance_indices[char]
            if idx_list[0] > last_matched_idx:
                last_matched_idx = idx_list[0]
            else:
                target_idx = binary_search(idx_list, last_matched_idx)
                last_matched_idx = idx_list[target_idx + 1]

        if last_matched_idx > -1:
            if len(word) > len(longest_word):
                longest_word = word
    return longest_word


# O(s)
def build_index_of_letter_occurance(s: str) -> dict:
    # e.g. 'abppplee' becomes: {'a': [0], 'b': [1], 'c': [2, 3, 4], 'l': [5],
    # 'e': [6, 7]}
    letter_occurance_indices = {}
    for i, char in enumerate(s):
        if char not in letter_occurance_indices:
            letter_occurance_indices[char] = [i]
        else:
            letter_occurance_indices[char].append(i)
    return letter_occurance_indices


# O(log(len(space)) Ot(1)
def binary_search(space: list, target: int):
    left = 0
    right = len(space)
    while left < right:
        mid = left + int((right - left) / 2)
        if space[mid] == target:
            break
        elif space[mid] < target:
            left = mid
        else:
            right = mid
    return mid


# 4) An optimal O(n + l) approach:
# Instead of processing the words one at a time,
# we will process all words simultaneously.
# Ot(n + l) Os(n + l) where n is the length of the string
# and  is total number of characters in the dictionary over all words. 
def find_longest_word_optimal(s: str, d: set) -> str:
    # Ot(w) Os(w) were w is count of words
    word_map = create_dict(d)

    max_length_word = ''
    max_length = float('-inf')
    # when looping over s, the idx (position) and
    # location in the dict are updated with eventually
    # up to 'a' moves.
    for char in s:
        if char in word_map:
            update = []
            for word, idx in word_map[char].items():
                idx += 1
                if idx == len(word):
                    # word found as candidate for longest word.
                    if len(word) > max_length:
                        max_length_word = word
                        max_length = len(word)
                else:
                    update.append((word, idx))
            word_map = update_dict(word_map, update)
    return max_length_word


# Ot(w) Os(1) where w is count of words in update and
# space is 1 given that dict items are only moved around
def update_dict(word_map: dict, update: list) -> dict:
    '''Each word and its current idx (letters already found)
    in update are moved to the 'key letter' of that idx.
    And removed from its prior idx 'key letter'.
    e.g. If current letter in s was 'a'
    update would be [("able",1), ("ale",1), ("apple",1)].
    word_map would be updated from:
    {'a': {"able":0, "ale":0, "apple":0}}
    to: {'b': {"able":1}, 'l':{"ale":1}, 'p':{"apple":1}}
    as after the first a, all 3 words would be at idx 1.
    '''
    for word, idx in update:
        if word[idx] in word_map:
            word_map[word[idx]][word] = idx
        else:
            word_map[word[idx]] = {word: idx}
        if word[idx - 1] != word[idx]:
            del word_map[word[idx - 1]][word]
    return word_map


# Ot(w) Os(w) were w is count of words
def create_dict(d: set) -> dict:
    word_map = {}
    for word in d:
        if word[0] in word_map:
            word_map[word[0]][word] = 0
        else:
            word_map[word[0]] = {word: 0}
    return word_map


def tests():
    S = "abppplee"
    D = {"able", "ale", "apple", "bale", "kangaroo"}
    exp = "apple"
    print(find_longest_word_brute_forth(S, D) == exp)
    print(find_longest_word_greedy(S, D) == exp)
    print(find_longest_word_greedy_faster(S, D) == exp)
    print(find_longest_word_optimal(S, D) == exp)

    S = "bpppleea"
    D = {"able", "ale", "apple", "bale", "kangaroo"}
    exp = ""
    print(find_longest_word_brute_forth(S, D) == exp)
    print(find_longest_word_greedy(S, D) == exp)
    print(find_longest_word_greedy_faster(S, D) == exp)
    print(find_longest_word_optimal(S, D) == exp)


tests()
