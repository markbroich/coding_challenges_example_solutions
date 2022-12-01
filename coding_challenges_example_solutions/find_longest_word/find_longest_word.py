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


def find_longest_word(s: str, d: set) -> str:
    word_map = create_dict(d)

    max_length_word = ''
    max_length = float('-inf')
    for char in s:
        if char in word_map:
            update = []
            for word, count in word_map[char].items():
                count += 1
                if count == len(word):
                    if len(word) > max_length:
                        max_length_word = word
                        max_length = len(word)
                else:
                    update.append((word, count))
            word_map = update_dict(word_map, update)
    return max_length_word


def update_dict(word_map: dict, update: list) -> dict:
    for word, count in update:
        if word[count] in word_map:
            word_map[word[count]][word] = count
        else:
            word_map[word[count]] = {word: count}
        if word[count - 1] != word[count]:
            del word_map[word[count - 1]][word]
    return word_map


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
