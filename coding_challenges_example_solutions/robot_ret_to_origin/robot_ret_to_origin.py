# Toy example of a toy robot :)

# write code to work out if a robot returns to 
# its origin after a sequence of steps. 

# The robot can step up, down, left and right 
# the instructions are given in the form of a string:
# e.g. 
# string = 'RRLUD'
# expected = False

# or     
# string = 'URDL'
# expected = True

# leetcode 657


def ret_to_origin(string):
    x = y = 0
    for i in string:
        if i == 'U':
            y += 1 
        if i == 'D':
            y -= 1
        if i == 'R':
            x += 1 
        if i == 'L':
            x -= 1
    return x == 0 and y == 0

def testing():
    string = 'RRLUD'
    expected = False
    print(ret_to_origin(string) == expected)
    
    string = 'URDL'
    expected = True
    print(ret_to_origin(string) == expected)

testing()