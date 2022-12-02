'''Given a string S and a set of words D, find the longest word in D that is
a subsequence of S.

Word W is a subsequence of S if some number of characters, possibly zero, can
be deleted from S
to form W, without reordering the remaining characters.

Note: D can appear in any format (list, hash table, prefix tree, etc.

For example, given the input of S = "abppplee" and
D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would
be "apple"

The words "able" and "ale" are both subsequences of S, but they are shorter
than "apple".
The word "bale" is not a subsequence of S because even though S has all the
right letters, they are not in the right order.
The word "kangaroo" is the longest word in D, but it isn't
a subsequence of S.'''


# Ot(s + a) Os(s + a) where is is the length of the string
# and a the number of letters in all words in d.
def find_longest_word(s: str, d: set) -> str:
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
    to: {'b': {"able":1}, 'l':{"ale":0}, 'p':{"apple":0}}
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



S = "abppplee"
D = {"able", "ale", "apple", "bale", "kangaroo"}
exp = "apple"
print(find_longest_word(S, D) == exp)

S = "bpppleea"
D = {"able", "ale", "apple", "bale", "kangaroo"}
exp = ""
print(find_longest_word(S, D) == exp)
