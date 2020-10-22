# workbreak2 

# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

# Note:
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:

# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]

########
# Below are two solutions to the problem. Both have O(a*b) time complexity 
# but the meaning of b is different!

# 1) 
# O(n*d) where n is the length of the string and d the 
# word count in the dictionary

# vs

# 2) 
# O(n*l) where n is the length of the string and l the 
# length of the longest dictionary word

#################
# Solutions: 

# 1) 
# O(n*d) where n is the length of the string and d the 
# word count in the dictionary
def wordBreak(string, mySet, memoDict={}):
    # if previously split
    if string in memoDict: 
        return memoDict[string]

    sentencesList = []
    for word in mySet:
        if string[:len(word)] == word:
            if len(word) == len(string): 
                sentencesList.append(word)
            else:
                sentences = wordBreak(string[len(word):], mySet, memoDict)
                # if it can not be solved along a recursive path, 
                # sentences is empty and hence sentencesList stays empty
                for nextword in sentences:
                    sentencesList.append(word + " " + nextword)
    # save split
    memoDict[string] = sentencesList
    #print(memoDict)
    return sentencesList

# test cases
string1 = 'iloveyou'
mySet1 = {'i', 'love', 'you'}

string2 = 'cockiesandcream'
mySet2 = {'cockie', 'cockies', 'and', 'sand', 'cream'}

string3 = 'ilikeicecreamandmango'
mySet3 = {'i', 'like', 'ice', 'and', 'cream', 'icecream', 'man', 'go', 'mango'}

# the stress test!
string4 = 'aaaaaaaaaaaaaaaabaaaaaaa'
mySet4 = {"a", "b", "aa", "aaa", "aaaa", "aaaaa"}

# run test cases
print(wordBreak(string1, mySet1))
print(wordBreak(string2, mySet2))
print(wordBreak(string3, mySet3))
sentences = wordBreak(string4, mySet4)
# only print if ready to wait :-)
#print(sentences)



# 2) 
# O(n*l) where n is the length of the string and l the 
# length of the longest dictionary word

def wordBreak(s, mySet):
    maxL = getMaxLen(mySet)
    return findSentences(s, mySet, maxL)

def getMaxLen(mySet):
    maxLen = 0
    for word in mySet:
        if len(word) > maxLen:
            maxLen = len(word)
    return maxLen

def findSentences(s, mySet, maxL, memoDict={}):
    # if previously split
    if s in memoDict.keys():
        return memoDict[s]
    
    sentencesList = []
    lenS = len(s)
    if lenS <= 0:
        return sentencesList
    
    for i in range(1, lenS + 1):
        if i <=  maxL:   
            prefix = s[0:i]
            if prefix in mySet:
                if i == lenS:
                    sentencesList.append(prefix)
                else:                              
                    temp = findSentences(s[i:lenS], mySet, maxL, memoDict)
                    tmp = ''
                    for tmp in temp:
                        tmp = prefix + " " + tmp
                        sentencesList.append(tmp)
    # save split
    memoDict[s] = sentencesList
    #print(memoDict)
    return sentencesList


# test cases
string1 = 'iloveyou'
mySet1 = {'i', 'love', 'you'}

string2 = 'cockiesandcream'
mySet2 = {'cockie', 'cockies', 'and', 'sand', 'cream'}

string3 = 'ilikeicecreamandmango'
mySet3 = {'i', 'like', 'ice', 'and', 'cream', 'icecream', 'man', 'go', 'mango'}

# the stress test!
string4 = 'aaaaaaaaaaaaaaaabaaaaaaa'
mySet4 = {"a", "b", "aa", "aaa", "aaaa", "aaaaa"}

# run test cases
print(wordBreak(string1, mySet1))
print(wordBreak(string2, mySet2))
print(wordBreak(string3, mySet3))
sentences = wordBreak(string4, mySet4)
# only print if ready to wait :-)
#print(sentences)