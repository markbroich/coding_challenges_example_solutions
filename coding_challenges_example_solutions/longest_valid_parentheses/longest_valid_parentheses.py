# Longest valid Parentheses
# Given a string A containing just the characters ’(‘ and ’)’.

# Find the length of the longest valid (well-formed) parentheses substring.


# Input Format:
# The only argument given is string A.

# Output Format:
# Return the length of the longest valid (well-formed) parentheses substring.

# For Example
# Input 1:
#     A = "(()"
# Output 1:
#     2
#     Explanation 1:
#         The longest valid parentheses substring is "()", which has length = 2.

# Input 2:
#     A = ")()())"
# Output 2:
#     4
#     Explanation 2:
#         The longest valid parentheses substring is "()()", which has length = 4.


# test stings and expected answers
testDict={}
# format: ('string',expectedCount)
testDict['A1'] = (")())", 2)
testDict['A2'] = (")(())", 4)
testDict['A3'] = ("())()())", 4)
testDict['A4'] = ("((()(())", 6)
testDict['A5'] = ("((()(()(", 2)
testDict['A6'] = ("((()(()(())((()))", 12)
testDict['A7'] = ("((()(()((()(()))", 8)




####################
# Hint: 
# If you know the longest parenthesis ending at index i, can you use that to compute answer?
####################


## Conceptual aporoach using a stack: 
# 1) Create an empty stack and push -1 to it. 
#    The first element of the stack is used 
#    to provide a base for the next valid string. 
#    (so that if this string '()xxxx' at index 1, 
#     triggers step 2), 
#     the 'difference between the current 
#     index and top of the stack is: 1-(-1)=2
#
# 2) Initialize result as 0.
#
# 3) If the character is '(' i.e. str[i] == '('), 
#    push index'i' to the stack. 
#   
# 4) Else (if the character is ')')
#    a) Pop an item from the stack 
#    b) If the stack is not empty, then find the
#       length of current valid substring by taking 
#       the difference between the current index and
#       top of the stack (the index before the bracket we 
#       just closed...).
#        If current length is more 
#       than the result, then update the result.
#    c) If the stack is empty, push the current index
#       as a base for the next valid substring.
# 5) Return result.

def find_max_len_stack(arr): 
    n = len(arr) 
    # Create a stack and push -1 
    # as initial index to it. 
    stk = [] 
    stk.append(-1) 
    # Initialize result 
    result = 0
    # Traverse all characters of given arr 
    for i in range(n): 
        # If opening bracket, push index of it 
        if arr[i] == '(': 
            stk.append(i) 
        # If closing bracket, i.e., str[i] = ')' 
        else:    
            # If the stack is not empty,
            # pop the previous opening bracket's index 
            if len(stk) != 0: 
               stk.pop() 
            # then find length of current valid substring by 
            # taking the difference between the current index 
            # and top of the stack. (The index before the 
            # bracket we just closed...).
            # If current length is more than the result, 
            # then update the result.
            # 
            # Check if this length formed with base of 
            # current valid substring is more than max 
            # so far 
            if len(stk) != 0: 
                result = max(result, i - stk[len(stk)-1]) 
            # If stack is empty. push current index as 
            # base for next valid substring (if any) 
            else: 
                stk.append(i) 
    return result 


# test cases 1-7
print('find_max_len_stack')
for i in testDict:
    print(i, " ", find_max_len_stack(testDict[i][0]) == testDict[i][1])
print('--------')


# dynamic programming approach were I store the max valid length at index i
# and use that information later when another bracket is closed 
# and where appropriate (when sequence of currently closed bracket 
# and previously closed brackets are in sequence)
def find_max_len_dp1(arr): 
    if (len(arr) <= 1): 
        return 0
    # Initialize result to zero 
    result = 0
    store = [0]*(len(arr)) 
    # Iterate over the arr starting 
    # from second index 
    for i in range(1, len(arr)): 
        if ((arr[i] == ')' and i-store[i-1]-1 >= 0 
             and arr[i-store[i-1]-1] == '(')): 
            store[i] = store[i-1]+2
            #
            if (i-store[i-1]-2 >= 0): 
                store[i] += (store[i-store[i-1]-2]) 
            else: 
                store[i] += 0
            result = max(store[i], result) 
    return result 
  
# test cases 1-7
print('find_max_len_dp1')
for i in testDict:
    print(i, " ", find_max_len_dp1(testDict[i][0]) == testDict[i][1])
print('--------')


# similar to dp approach above:
def find_max_len_dp2(arr):
    store = [0]*len(arr)
    for i in range(0,len(arr)):
        if(arr[i] == '('):
            store[i] = 0
        elif(arr[i] == ')' and i!=0):
            if(arr[i-1] == '('): # did I just close a pair? 
                store[i] = store[i-2]+2 # if the one before the one I just closed 
                #                 is zero, then I get 2, else I add what
                #                 was closed before the one I just closed
            elif(arr[i-1] == ')' and arr[i-1-store[i-1]] == '(' and i-1-store[i-1] >= 0):
                store[i] = store[i-1]+2+store[i-store[i-1]-2]
            else:
                pass
    return max(store)

# test cases 1-7
print('find_max_len_dp2')
for i in testDict:
    print(i, " ", find_max_len_dp2(testDict[i][0]) == testDict[i][1])
print('--------')



# but if I add some noise, the stack solution bails so would need more work 
print('find_max_len_dp1', find_max_len_dp1("(, ))") == 0)
print('find_max_len_dp2', find_max_len_dp2("(, ))") == 0)
# bails
print('find_max_len_stack', find_max_len_stack("(, ))") == 0)