import collections

"""Given a set of words (without duplicates),
find all word squares you can build from them.
A sequence of words forms a valid word square if the kth row and column
read the exact same string, where 0 ≤ k < max(numRows, numColumns).
"""

"""
Input = ["area","lead","wall","lady","ball"]

Output =
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Input = ["abat","baba","atan","atal"]

Output =
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

Explanation:
The output consists of two word squares.
The order of output does not matter
(just the order of words in each word square matters).
"""


def word_square(arr: list) -> list:
    res = []

    # O(n! / (n-k)!) where n is words
    # implifies to Ot(n!) if n is large and
    # the number of words k in the cube is small
    # for each attempt, we need to loop over the length of
    # the word in skip_word()
    def backtrack(choices: list) -> list:
        if len(choices) == 0 or (len(res) and len(res) == len(res[0])):
            return True
        for i in range(0, len(choices)):
            if len(res) > 0 and skip_word(choices[i]):
                continue
            if len(res) > 0 and len(choices[i]) != len(res[0]):
                # skip if subsequent words not of equal length
                continue
            res.append(choices[i])
            # keep all choices
            # if not backtrack(choices[:i] + choices[i + 1:]):
            if not backtrack(choices):
                res.pop()
            else:
                return True
        return False

    # Ot(l) Os(1) where l is length of word
    def skip_word(word: list) -> bool:
        char = ''
        for j in range(0, len(res)):
            char += res[j][len(res)]
        if char != word[0:len(char)]:
            return True
        return False

    if backtrack(arr):
        return res
    else:
        return []


def word_square_faster(arr: list, use_trie=False) -> list:
    res = []

    # Ot(k) where k is length of letters in arr (the word list)
    # Os(wl * wc) where wl and wc are word length and word count respectivley.
    # access is O(1)
    if use_trie:
        trie = Trie()
        for word in arr:
            trie.insert(word)
    else:
        prefix = build_dict(arr)

    # O(n! / (n-k)!) where n is words
    # implifies to Ot(n!) if n is large and
    # the number of words k in the cube is small
    # for each attempt, we need to look up either the dict (Ot(1)) or the
    # more ram efficient trie (Ot(prefeix length + number of words that
    # are children to prefix))
    def backtrack(choices: list) -> list:
        if len(choices) == 0 or (len(res) and len(res) == len(res[0])):
            return True
        char = ''
        for j in range(0, len(res)):
            char += res[j][len(res)]
        if use_trie:
            words = trie.query(char)
        else:
            words = prefix[char]
        for word in words:
            if len(res) > 0 and len(word) != len(res[0]):
                # skip if subsequent words not of equal length
                continue
            res.append(word)
            if not backtrack(choices):
                res.pop()
            else:
                return True
        return False

    if backtrack(arr):
        return res
    else:
        return []


# to build:
# Ot(k) where k is length of letters in arr (the word list)
# Os(wl * wc) where wl and wc are word length and word count respectivley.
# to access: Ot(1)
def build_dict(arr: list) -> dict:
    prefix = collections.defaultdict(list)
    for word in arr:
        for i in range(0, len(word)):
            prefix[word[:i]].append(word)
    return prefix


class Trie_Node:
    def __init__(self):
        self.children = {}
        self.word = ''


class Trie:
    def __init__(self):
        self.root = Trie_Node()

    # Ot(c) where c is character count Os(c + c) for each word
    def insert(self, word):
        if not word:
            return
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Trie_Node()
            current = current.children[char]
        current.word = word

    # Ot(s + gather_word) Os(1 + gather_word) where s is length of string
    def query(self, string):
        current = self.root
        for i, char in enumerate(string):
            if char not in current.children:
                return []
            else:
                current = current.children[char]
        res = []

        # Ot(w) Os(w) where w is the number of words stored in current
        # and its children
        def gather_words(current):
            if current.word:
                res.append(current.word)
            if not current.children:
                return
            for child in current.children:
                gather_words(current.children[child])

        gather_words(current)
        return res


def tests():
    Output1 = ["wall", "area", "lead", "lady"]
    Output2 = ["ball", "area", "lead", "lady"]
    Input = ["area", "lead", "wall", "lady", "ball"]
    # print(word_square(Input))
    print(word_square(Input) == Output1 or word_square(Input) == Output2)
    print(word_square_faster(Input, use_trie=False) == Output1
          or word_square_faster(Input, use_trie=False) == Output2)
    print(word_square_faster(Input, use_trie=True) == Output1
          or word_square_faster(Input, use_trie=True) == Output2)

    Input = ["wall", "area", "lady", "lead", "ball"]
    # print(word_square(Input))
    print(word_square(Input) == Output1 or word_square(Input)
          == Output2)
    print(word_square_faster(Input, use_trie=False) == Output1
          or word_square_faster(Input, use_trie=False) == Output2)
    print(word_square_faster(Input, use_trie=True) == Output1
          or word_square_faster(Input, use_trie=True) == Output2)

    Input = ["ball", "area", "lead", "wall", "lady"]
    # print(word_square(Input))
    print(word_square(Input) == Output1 or word_square(Input)
          == Output2)
    print(word_square_faster(Input, use_trie=False) == Output1
          or word_square_faster(Input, use_trie=False) == Output2)
    print(word_square_faster(Input, use_trie=True) == Output1
          or word_square_faster(Input, use_trie=True) == Output2)

    Input = ["area", "lead", "ball", "wall", "lady"]
    # print(word_square(Input))
    print(word_square(Input) == Output1 or word_square(Input) == Output2)
    print(word_square_faster(Input, use_trie=False) == Output1
          or word_square_faster(Input, use_trie=False) == Output2)
    print(word_square_faster(Input, use_trie=True) == Output1
          or word_square_faster(Input, use_trie=True) == Output2)        
    # Output = [["wall", "area", "lead", "lady"], ["ball", "area", "lead", "lady"]]

    Input = ["abat", "baba", "atan", "atal"]
    Output1 = ["baba", "abat", "baba", "atan"]
    Output2 = ["baba", "abat", "baba", "atal"]
    # Output = [["baba", "abat", "baba", "atan"], ["baba", "abat", "baba", "atal"]]
    print(word_square(Input) == Output1 or word_square(Input) == Output2)
    print(word_square_faster(Input, use_trie=False) == Output1
          or word_square_faster(Input, use_trie=False) == Output2)
    print(word_square_faster(Input, use_trie=True) == Output1
          or word_square_faster(Input, use_trie=True) == Output2)       

    # unequal length
    Output1 = ["wall", "area", "lead", "lady"]
    Output2 = ["ball", "area", "lead", "lady"]
    Input = ["ara", "area", "lead", "wall", "lady", "ball"]
    print(word_square(Input) == Output1 or word_square(Input) == Output2)
    print(word_square_faster(Input, use_trie=False) == Output1
          or word_square_faster(Input, use_trie=False) == Output2)
    print(word_square_faster(Input, use_trie=True) == Output1
          or word_square_faster(Input, use_trie=True) == Output2)

    # need to use input word twice
    Output1 = ["that", "hash", "asia", "that"]
    Input = ["fool", "asia", "hash", "that"]
    print(word_square(Input) == Output1)
    print(word_square_faster(Input, use_trie=False) == Output1)
    print(word_square_faster(Input, use_trie=True) == Output1)

    # empty input
    Output1 = []
    Input = []
    print(word_square(Input) == Output1)
    print(word_square_faster(Input, use_trie=False) == Output1)
    print(word_square_faster(Input, use_trie=True) == Output1)

    # single input
    Output1 = []
    Input = ['alone']
    print(word_square(Input) == Output1)
    print(word_square_faster(Input, use_trie=False) == Output1)
    print(word_square_faster(Input, use_trie=True) == Output1)


tests()
