# balanced_brackets

# write code to check if a line or piece of code (a string)
# has balanced brackets. 

# Examples: 
string = "[()]{}{[()()]()}" 
# Output: Balanced
string  = "[(])"
# Output: NotBalanced

def balanced_brackets(string):
    if not string:
        return -1
    stack = []
    for char in string:
        if char == "(" or char == "{" or char == "[":
            stack.append(char)
        elif not stack:
            return False
        else:
            popped = stack.pop()
            if char == ")" and popped != "(":
                return False
            if char == "}" and popped != "{":
                return False
            if char == "]" and popped != "[":
                return False
    # if there are still items in the stack
    if stack:
        return False
    else:
        return True

string = "[()]{}{[()()]()}" 
#Output: Balanced
print(balanced_brackets(string))

string  = "[(])"
#Output: NotBalanced
print(balanced_brackets(string))

string = "[()]{}{[()()]()}}" 
#Output: NotBalanced
print(balanced_brackets(string))

string = "[()]{}{[()()]()}{" 
#Output: NotBalanced
print(balanced_brackets(string))

string = None
#Output: -1 
print(balanced_brackets(string))