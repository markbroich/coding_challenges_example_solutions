# Write a function to determine if a word (or phrase) is a palindrome.

# A palindrome is a word, number, phrase, or other sequence of characters which reads the 
# same backward as forward, such as madam, racecar. 

# Qs what if single digit or character?  
# also sentences? is it ok to ignore ignore capitalization, punctuation, and word boundaries? 

# rephrasing: if I can reverse a list without changing its meaning.
# reverse list. 
# then check if identical...  
# this is the brute force... O(n+n) so O(n)

def rev_list(arr):
    length = len(arr)
    arr_ret = [""]*length
    for i in range(0, length):
        arr_ret[i] = arr[length- i -1]
    return arr_ret

def compare(arr, rev_arr): 
    for i in range(0, len(arr)):
        if arr[i] != rev_arr[i]:
            return False
    return True

### testing ...
# two known examples
# odd length
arr = "madam" 
print(arr)
rev_arr = rev_list(arr)
print(compare(arr, rev_arr))
# odd length
arr = "racecar"
print(arr)
rev_arr = rev_list(arr)
print(compare(arr, rev_arr))
# even length 
arr = "abba"
print(arr)
rev_arr = rev_list(arr)
print(compare(arr, rev_arr))

# double letter
arr = "aa"
print(arr)
rev_arr = rev_list(arr)
print(compare(arr, rev_arr))
arr = "ab"
print(arr)
rev_arr = rev_list(arr)
print(compare(arr, rev_arr))
# single letter
arr = "a"
print(arr)
rev_arr = rev_list(arr)
print(compare(arr, rev_arr))

# not a palindrome
arr = "acestar"
print(arr)
rev_arr = rev_list(arr)
print(compare(arr, rev_arr))
print("")

# a better algo: 
# find half
# int(len(arr)/2)
# compare index i == length-1-i (in 1st half vs 2nd half for half the array)
# O(n/2) so O(n) for single words or numbers. More if sentences where spaces, punctation and caps need to be removed  

def find_pdrome(arr):
    if arr == None:
        retrun -1
    # drop spaces, punctations and caps (when dealing with sentences)
    arr = drop_space(arr)
    arr = drop_punct(arr)
    arr = decap(arr)
    length = len(arr)
    for i in range(0, int(length/2)):
        if arr[i] != arr[length-1-i]:
            return False
    return True

def drop_space(arr):
    # O(n)
    arr_ret = []
    for i in arr:
        if i != " ":
            arr_ret.append(i)
    return arr_ret

# could combine with drop_space to reduce total O() 
def drop_punct(arr):
    myset = {'.',',','?','!'}
    arr_ret = [""]*len(arr)
    i = 0
    j = 0
    while i < len(arr):
        if arr[i] not in myset:
            arr_ret[j] = arr[i]
            j += 1
        i += 1
    return arr_ret[0:j]

def decap(arr):
    arr_ret = [""]*len(arr)
    for i in range(0,len(arr)):
        if isinstance(arr[i], str):
            arr_ret[i] = arr[i].lower()
        else:
            arr_ret[i] = arr[i]
    return arr_ret


print("a better algo: ")
### testing ...
# two known examples
# odd length
arr = "madam" 
print(arr)
print(find_pdrome(arr))
# odd length
arr = "racecar"
print(arr)
print(find_pdrome(arr))
# even length 
arr = "abba"
print(arr)
print(find_pdrome(arr))

# double letter
arr = "aa"
print(arr)
print(find_pdrome(arr))
arr = "ab"
print(arr)
print(find_pdrome(arr))
# single letter
arr = "a"
print(arr)
print(find_pdrome(arr))

# not a palindrome
arr = "acestar"
print(arr)
print(find_pdrome(arr))

# other examples
arr = "redivider"
print(arr)
print(find_pdrome(arr))
arr = "deified"
print(arr)
print(find_pdrome(arr))
arr = "civic"
print(arr)
print(find_pdrome(arr))
arr = "radar"
print(arr)
print(find_pdrome(arr))
arr = "level"
print(arr)
print(find_pdrome(arr))
arr = "rotor"
print(arr)
print(find_pdrome(arr))
arr = "kayak"
print(arr)
print(find_pdrome(arr))
arr = "reviver"
print(arr)
print(find_pdrome(arr))

# sentences I found online
arr = "Mr. Owl ate my metal worm"
print(arr)
print(find_pdrome(arr))
arr = "Do geese see God?"
print(arr)
print(find_pdrome(arr))
arr = "Was it a car or a cat I saw?"
print(arr)
print(find_pdrome(arr))
arr = "Was it a cat or a car I saw?"
print(arr)
print(find_pdrome(arr))


# Then write a second function to receive a word (or phrase) list and determine which word is the longest palindrome.


word_list = ["madam", "racecar", "abba", "aa", "ab", "a", "acestar", "redivider", "deified", "civic", "radar", "level", "rotor", "kayak", "reviver", "Was it a car or a cat I saw?", "Mr. Owl ate my metal worm", "Do geese see God?", "Was it a cat or a car I saw?"]
len_max_pdrom = 0
max_pdrom = ""
for arr in word_list:
    if find_pdrome(arr) and len(arr) > len_max_pdrom:
            len_max_pdrom = len(arr)
            max_pdrom = arr

print(max_pdrom)