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


#### a related question:
# return the number of un match brackets


# the string can only consist of 
# combinations of '(' and ')'

# using a stack
# Ot(n) 
# Os(n) if all '(' or all ')'
def bracket_match(string):
    stack = []
    for i in range(0,len(string)):
        if string[i] == '(':
            stack.append('(')
        elif len(stack) > 0:
            if stack[-1] == '(':
                stack.pop()
            else: 
                stack.append(')')
        else: 
            stack.append(')')
    return len(stack)

def tests():
    string = ')))()('
    print(bracket_match(string) == 4)
    string = ')'
    print(bracket_match(string) == 1)
    string = '('
    print(bracket_match(string) == 1)
    string = '(())'
    print(bracket_match(string) == 0)
    string = '(()'
    print(bracket_match(string) == 1)
    string = '())('
    print(bracket_match(string) == 2)
    string = '))))'
    print(bracket_match(string) == 4)
    string = ')('
    print(bracket_match(string) == 2)
    string = '()()()()()'
    print(bracket_match(string) == 0)

print('mismatch count:')
tests()

# using only Os(1)
def bracket_match(string):
    counterO = 0
    counterC = 0 
    for i in range(0,len(string)):
        if string[i] == '(':
            counterO +=1
        elif counterO > 0: 
            counterO -= 1
        else:
            counterC += 1
    return counterO+counterC

print('Os(1)')
tests()






