'''
Integer to Roman

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.


Example 1:
Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.

Example 2:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 3:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:
1 <= num <= 3999
'''


lookup = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',
    10: 'X',
    20: 'XX',
    30: 'XXX',
    40: 'XL',
    50: 'L',
    60: 'LX',
    70: 'LXX',
    80: 'LXXX',
    90: 'XC',
    100: 'C',
    200: 'CC',
    300: 'CCC',
    400: 'CD',
    500: 'D',
    600: 'DC',
    700: 'DCC',
    800: 'DCCC',
    900: 'CM',
    1000: 'M'
}


def integer_to_roman(num: int) -> str:
    str_of_number = str(num)
    number_as_list_of_string = list(str_of_number)

    # attach leading zeros is needed
    diff = 4 - len(number_as_list_of_string)
    for i in range(diff):
        number_as_list_of_string = [0] + number_as_list_of_string

    res = ''
    for i in range(0, len(number_as_list_of_string)):
        num = int(number_as_list_of_string[i])
        if num == 0:
            continue
        else:
            if i == 0:
                num = int(str(num) + str(0) + str(0) + str(0))
            elif i == 1:
                num = int(str(num) + str(0) + str(0))
            elif i == 2:
                num = int(str(num) + str(0))
            res = res + lookup[num]
    return res


num = 3
expected = "III"
# Explanation: 3 is represented as 3 ones.
print(integer_to_roman(num) == expected)

num = 9
expected = "IX"
print(integer_to_roman(num) == expected)

num = 58
expected = "LVIII"
# Explanation: L = 50, V = 5, III = 3.
print(integer_to_roman(num) == expected)

num = 1994
expected = "MCMXCIV"
print(integer_to_roman(num) == expected)
