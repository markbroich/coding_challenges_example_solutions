# create a function that given a number plots back a square of numbers 
# with concentric rings as per examples below

# Input: A = 3.
# Output:

# 3 3 3 3 3 
# 3 2 2 2 3 
# 3 2 1 2 3 
# 3 2 2 2 3 
# 3 3 3 3 3 

# Input: A = 4.
# Output:

# 4 4 4 4 4 4 4 
# 4 3 3 3 3 3 4 
# 4 3 2 2 2 3 4 
# 4 3 2 1 2 3 4 
# 4 3 2 2 2 3 4 
# 4 3 3 3 3 3 4 
# 4 4 4 4 4 4 4 


class PrettyPrinter:
    # Input: A, an integer specifying the 
    #   value of the outer ring
    # Return: a list of list with concentric
    #   rings of numbers starting with A and 
    #   decreasing to 1 in the center
    def prettyPrint(A):
        x = 2 * A - 1
        # init the list of lists to A
        res = [[A for j in range(x)] for i in range(x)]
        # the 'out rim*' does not change
        for i in range(1, A):
            for j in range(1, A): 
                res[i][x-1-j] = res[x-1-i][j] = res[x-1-i][x-1-j] = res[i][j] = A-min(i,j)
        return res


P1 = PrettyPrinter
print(P1.prettyPrint(3))


# *out rim :  https://i.pinimg.com/1200x/c5/c2/4d/c5c24d582f90544851a617a8e419edd6.jpg