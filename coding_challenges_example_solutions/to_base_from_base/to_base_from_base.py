# solve a number conversion problem: given a positive number, and target base b, convert this number to that base.

# # Example: we can ignore the prefix part of each base: such as '0b' for base 2, '0o' for base 8, etc. 
# Just return the converted number.
# >>> dec_to_base(10, 2) -> 1010   -  as of "0b1010"
# >>> dec_to_base(24, 6) -> 40
# >>> dec_to_base(256, 8) -> 400   -  as of "0o400"

def numberToBase(n, b):
    if n == 0:
        return [0]
    
    digits = []
    while n:
        remaining = int(n % b)
        digits.append(str(remaining))
        n = int(n / b)

    #digits = digits.reverse()
    digits = digits[::-1]
    return ''.join(digits)
 

print(numberToBase(10, 2))
print(numberToBase(24, 6))
print(numberToBase(256, 8))
print(numberToBase(2, 2))
print(numberToBase(3, 2))
print(numberToBase(4, 2))
print(numberToBase(100, 2))
print("")

# the pythonic conversion of decimal_to_bin is very simple: bin(int(decimal))
def decimal_to_bin_pythonic(n):
    return bin(int(n))

print(decimal_to_bin_pythonic(10))
print("")

# for binary numbers here is the conversion back to a decimal number
def binarytodecimal(binary):
    if isinstance(binary, int):
        binary = str(binary)

    decimal = 0 
    for digit in binary: 
        decimal = decimal*2 + int(digit) 
    return decimal

print(binarytodecimal(1010))
print("")

# again the pythonic way is very simple: int(binary,base) 
def binarytodecimal_pythonic(binary, base):
    if isinstance(binary, int):
        binary = str(binary)

    decimal = int(binary,base)  
    return decimal

print(binarytodecimal_pythonic('1010',2))
print(binarytodecimal_pythonic(1010,2))
print(binarytodecimal_pythonic(400,8))
print("")



### step by step calc using the core equations: 

# TO BINARY
# digits = []
# while n:
#     remaining = int(n % b)
#     digits.append(str(remaining))
#     n = int(n / b)
# digits = digits[::-1]

# 12 to bin = 1110

#    1 1 0 0 
# 16,8,4,2,1

# so, 
# r = 0
# n 6
# r = 00
# n 3
# r = 001
# n 1
# r = 0011
# n = 0


# TO DECIMAL
# decimal = 0 
# for digit in binary: 
#     decimal = decimal*2 + int(digit) 

# bin 1110 to dec = 12

#    1 1 0 0 
# 16,8,4,2,1

# deci = 0
# deci = 0*2 + 1
# deci = 1*2 + 1
# deci = 3*2 + 0
# deci = 6*2 + 0
# so, deci = 12
