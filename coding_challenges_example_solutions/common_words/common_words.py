# Common words
# Given two sentences that each contains words in case insensitive way, you have to check the common case insensitive words appearing in both sentences.

# If there are duplicate words in the results, just choose one. The results should be sorted by words length.

# The sentences are presented as list of words. Example:
S = ['You', 'can', 'do', 'anything', 'but', 'not', 'everything', 'repeatedly']
# ##                 **                       **                   **
T = ['We', 'are', 'what', 'we', 'repeatedly', 'do', 'is', 'not', 'an', 'act']
# ##                                 **         **          **
# Result = ['do', 'not', 'repeatedly']


# I could 
# A) populate a dict while looping over S, then loop over T to find common, then sort, then look for dubs
# this would be O(s + t + m*log(m) + m) where s, t, m are length of S, length of t, length of matches respectivley. 
# or 
# B) do the sorting and de dublication by mapping all matches to a BST. this would be O(s + t + log(m) + d) 
# where m and d are length of matches and length of matches after de-duplication, respectivley. 
# B) would simplify to O(s + t) as log(m) and d are small
# space is O(d) as I store the duplicaties in bst.

# Concept: 
# 1) loop over S and pop dict
# 2) loop over T and query dict for matches. write to bst meanwhile
# 3) transverse bst in order... 
# during 1 and 2, set to lower case. 

# wrapper function
def print_sorted_matches(S,T):
    my_dict = populate_dict(S)
    bst_matches = find_matches(T, my_dict)
    print(bst_matches.inorder_trav())
 
def populate_dict(S):
    my_dict = {}
    for i in S:
        i = i.lower()
        my_dict[i] = i
    return my_dict

def find_matches(T, my_dict):
    # find matches and map to bst
    # which will sort and deduplicate them
    first_match = True
    # loop over T, and if match map to bst
    for j in T:
        j = j.lower()
        if j in my_dict:
            if first_match: 
                bst = Node(j)
                first_match = False
            else:
                bst.insert(j)
    return bst

class Node:
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

    def insert(self, value):
        if not self._value:
            self._value = value # insert here
        else:
            if value <  self._value:
                if self._left == None:
                    self._left = Node(value)
                else:
                    self._left.insert(value)
            if value >  self._value:
                if self._right == None:
                    self._right = Node(value)
                else:
                    self._right.insert(value)
    
    # Print the tree inorder (so left, root, 
    # right starting from leftmost)
    def inorder_trav(self):
        if self._value == None:
            print('empty tree')
        else:     
            if self._left:
                self._left.inorder_trav()
            print(self._value)
            if self._right:
                self._right.inorder_trav()
            return ""

# run the code    
print_sorted_matches(S,T)   


    
# algo question from: https://codechalleng.es