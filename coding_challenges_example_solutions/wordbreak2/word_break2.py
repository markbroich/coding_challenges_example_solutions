'''
Given a string s and a dictionary of strings wordDict, add spaces in s to
construct a sentence where each word is a valid dictionary word.
Return True if s can be split into the dictionary word.

Note that the same word in the dictionary may be reused multiple times
in the segmentation.

Input: s = "catsanddog", wordDict = ["cat", "cats", "and", "sand", "dog"]
Output: True
'''


def solve(s, wordDict):
    mySet = set(wordDict)

    def rec(post):
        if not post:
            return True

        for i in range(1, len(post) + 1):
            if post[:i] in mySet:
                resNew = rec(post[i:])
                if resNew:
                    return True
        return False

    return rec(s)


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(solve(s, wordDict) is True)

s = "catsanddogs"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(solve(s, wordDict) is False)


'''
Wordbreak2

Given a string s and a dictionary of strings wordDict, add spaces in s to
construct a sentence where each word is a valid dictionary word.
Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times
in the segmentation.

Input: s = "catsanddog", wordDict = ["cat", "cats", "and", "sand", "dog"]
Output: ["cats and dog", "cat sand dog"]
'''


# w/ o a memo.
def solve(s, wordDict):
    mySet = set(wordDict)
    result = []

    def rec(pre, post):
        if not post:
            result.append(" ".join(pre))
            return

        for i in range(1, len(post) + 1):
            if post[:i] in mySet:
                rec(pre + [post[:i]], post[i:])

    rec([], s)
    return result


s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog", "d", "og", "c", "at"]
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(solve(s, wordDict) == ['cat sand dog', 'cats and dog'])


'''
Wordbreak2 time and space complexity:
We can reformulate the problem as finding all the paths from the root
to the leaf nodes in a tree consisting of postfixes using DFS.

We might visit certain nodes multiple times (hence we use a memo), but we
visit each edge once and only once (when populating the memo). Therefore,
the time complexity of the algorithmis proportional to the number of edges
(to populate the memo), which depends on the construction of the input
string and the word dictionary.

In the worst case e.g. s = 'aaa' worddict = set(['a', 'aa', 'aaa']),which
results in a lot of edges...

The recursions would be Ot(2**n): the nodes to visit.
Populating a memo we
would decrease the runtime to Ot(n**2), which is the time it takes to explore
all edges and populate the 'node' memo. (hence no need to recur on known nodes)

In addition, at each visit to an edge, we need to iterate through the number of
solutions that are brought back by the edge. In the above worst case, each
postfix of length i would have 2**(i-1) number of solutions,i.e. each edge
brings back 2**(i-1) number of solution from the target postfix.

Therefore, in total, we need Sum i to N of: 2**(i-1) hence Ot(2**N)
iterations to construct the final solutions.
E.g.
s = 'aaa' wordDict = ["a", "aa", 'aaa'] calls 'result.append(" ".join(pre))'
on ['a', 'a', 'a'] ['a', 'aa'] ['aa', 'a'] ['aaa'] which is 8 items
== 2**N == 2**3.

Hence total Ot(2**N + 2**N) without memo and Ot(N**2 + 2**N) when using a memo.
Os == Ot given that in the worst case our recursion stack for traversing all
tree edges (and populating the memo) is N**2 deepand we would aggregate a
result that is 2**N long.'''

s = 'aaa'
wordDict = ["a", "aa", 'aaa']
print(solve(s, wordDict))
print(2**len(s))
print()


# with a memo, the way I return the results changes
def solve(s, wordDict):
    mySet = set(wordDict)
    # maxlength = max([len(w) for w in mySet])
    memo = {}

    def rec(post):
        if post not in memo:
            sentencesList = []
            if not post:
                return sentencesList
            for i in range(1, len(post) + 1):
                # to stop early
                # if i > maxlength:
                #    memo[post] = sentencesList
                #    return memo[post]
                if post[:i] in mySet:
                    if i == len(post):
                        sentencesList.append(post[:i])
                    for s in rec(post[i:]):
                        sentencesList.append(post[:i] + ' ' + s)
            memo[post] = sentencesList
        return memo[post]
    return rec(s)


s = 'aa'
mySet = ["a", "aa"]
exp = ['a a', 'aa']
print('----')
print(solve(s, mySet) == exp)

# the stress test that does take a long time w/o a memo!
s = 'aaaaaaaaaaaaaaaabaaaaaaa'
mySet = ["a", "b", "aa", "aaa", "aaaa", "aaaaa"]
# solve(s, mySet)


# A slighly different apporach with a memo, 
# and using indices so to not pass substrings into the callstack.


def wordbreak(s):
    # returns true and false
    if not s:
        return True
    for i in range(0, len(s) + 1):
        if s[:i] in wordDict:
            return wordbreak(s[i:])
    return False


def wordbreak2(s):
    res = []
    if s in wordDict:
        return [s]
    for i in range(0, len(s) + 1):
        if s[:i] in wordDict:
            for w in wordbreak2(s[i:]):
                res.append(s[:i] + " " + w)
    return res


def wordbreak2_memo(s):
    memo = {}

    def helper(s):
        if s not in memo:
            res = []
            if s in wordDict:
                return [s]
            for i in range(0, len(s) + 1):
                if s[:i] in wordDict:
                    for w in helper(s[i:]):
                        res.append(s[:i] + " " + w)
            memo[s] = res
        return memo[s]

    return helper(s)


# the fastest given memo use and no passing of srings so no 
# extra ram and no additional O(len(substring)) for substring creation
def wordbreak2_index(string):
    memo = {}

    def helper(st):
        if st not in memo:
            res = []
            if string[st:] in wordDict:
                return [string[st:]]
            for en in range(st, len(string) + 1):
                if string[st:en] in wordDict:
                    for w in helper(en):
                        res.append(string[st:en] + " " + w)
            memo[st] = res
        return memo[st]

    return helper(0)


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
exp = ["cats and dog", "cat sand dog"]

print(wordbreak(s))
print(wordbreak2(s))
print(wordbreak2_memo(s))
print(wordbreak2_index(s))
print()

s = "catsanddogs"
wordDict = ["cat", "cats", "and", "sand", "dog"]
exp = ["cats and dog", "cat sand dog"]

print(wordbreak(s))
print(wordbreak2(s))
