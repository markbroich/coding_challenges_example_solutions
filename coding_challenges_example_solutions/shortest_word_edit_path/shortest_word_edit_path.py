## Shortest Word Edit Path

# Given two words source and target, and a list of words words, find the length of the shortest series of edits that transforms source to target.

# Each edit must change exactly one letter at a time, and each intermediate word (and the final target word) must exist in words.

# If the task is impossible, return -1.

# Examples:

# source = "bit", target = "dog"
# words = ["but", "put", "big", "pot", "pog", "dog", "lot"]

# output: 5
# explanation: bit -> but -> put -> pot -> pog -> dog has 5 transitions.
# source = "no", target = "go"
# words = ["to"]

# output: -1
# Constraints:

# [time limit] 5000ms
# [input] string source
# 1 ≤ source.length ≤ 20
# [input] string target
# 1 ≤ target.length ≤ 20
# [input] array.string words
# 1 ≤ words.length ≤ 20
# [output] array.integer



# Ot(len(WordShort)*len(WordShort)*len(Source)) 
# Os(len(WordShort))

def shortestWordEditPath(source, target, words):
    """
    @param source: str
    @param target: str
    @param words: str[]
    @return: int
    """
    #
    if not target in  words: # target not in words
        print('target not in words')
        return -1 
    #
    # Ot(len(words)); Os(len(words))
    words = short_list_words(source, words)
    #
    # populate transDict (graph of translations)
    # Ot(len(WordShort)*len(WordShort)*len(Source))
    # Os(len(WordShort))
    transDict = pop_transDict(source, words)
    if not transDict: # no translations
        print('no translations in dict')
        return -1 
    #
    # BFS
    # Ot(len(words)) (visiting each word at most once)
    # Os(len(words))
    stepC = 1
    Q = transDict[source]
    vistedLst = set(source)
    newQ = []
    #
    while True:
        if target in Q: 
            break # found
        #
        while Q:
            word = Q.pop(0)
            if not word in vistedLst:
                newQ = newQ + transDict[word]
                vistedLst.add(word)
        #
        stepC += 1
        #
        if not newQ:
            return -1
        #
        Q = newQ
        newQ = []
    #
    return stepC
#
# Ot(len(words)); Os(len(words))
def short_list_words(source, words):
    wordsSub = []
    for word in words:
        if len(word) == len(source):
            wordsSub.append(word)
    return wordsSub
#
# Ot(len(WordShort)*len(WordShort)*len(Source))
# Os(len(WordShort))
def pop_transDict(source, words):
    transDict = {}
    #
    wordsAllLst = [source] + words
    for wordI in wordsAllLst:
        if len(wordI) == len(source): 
            for wordJ in wordsAllLst:
                # count matches
                mc = 0
                for k, cI in enumerate(wordI):
                    cJ = wordJ[k]
                    if cI == cJ:
                        mc += 1
                # only words w match count == len(source)-1
                # can be translated
                if mc == len(source)-1:
                    if wordI in transDict:
                        transDict[wordI].append(wordJ)
                    else: 
                        transDict[wordI] = [wordJ]
                    ##
    return transDict


def testing():
    source = "bit"
    target = "dog"
    words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
    expected = 5
    print(shortestWordEditPath(source, target, words) == expected)

    source = "no"
    target = "go"
    words = ["to"]
    expected = -1
    print(shortestWordEditPath(source, target, words) == expected)

    source = "bit"
    target = "pog"
    words = ["but","put","big","pot","pog","pig","dog","lot"]
    expected = 3 
    print(shortestWordEditPath(source, target, words) == expected)

    source = "abc"
    target ="ab"
    words =  ["abc","ab"]
    expected = -1 
    print(shortestWordEditPath(source, target, words) == expected)


    source = "abc"
    target ="ab"
    words =  ["abc","ab"]
    expected = -1 
    print(shortestWordEditPath(source, target, words) == expected)


    source = "aa"
    target ="bbb"
    words =  ["aa", "bbb"]
    expected = -1 
    print(shortestWordEditPath(source, target, words) == expected)


testing()


