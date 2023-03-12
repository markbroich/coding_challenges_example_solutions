'''Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Constraints:
-2**31 <= x <= 2**31 - 1
'''

# O(n) where n is len of number
def reverse_integer(number: int) -> int:
    rev = ''
    postive = True
    number_str = str(number)
    for i in range(len(number_str) -1, -1, -1):
        if number_str[i] == '-':
            postive = False
            break
        rev += number_str[i]
    if is_out_of_range(rev, postive):
        return 0
    if not postive:
        return -int(rev)
    return int(rev)


# Ot(n) Os(1) where n is len of number
def is_out_of_range(rev, postive):
    if len(rev) > 10:
        return 0
    if len(rev) == 10:
        for i, c in enumerate(rev):
            if postive:
                max_num = str(2**31 - 1)
                if int(c) > int(max_num[i]):
                    return True
            else:
                min_num = str(2**31)
                if int(c) > int(min_num[i]):
                    return True
    return False


def tests():
    x = 123
    expected = 321
    print(reverse_integer(x) == expected)

    x = -123
    expected = -321
    print(reverse_integer(x) == expected)

    x = 120
    expected = 21
    print(reverse_integer(x) == expected)

    x = 7463847412
    expected = 2147483647
    print(reverse_integer(x) == expected)

    x = 8463847412
    expected = 0
    print(reverse_integer(x) == expected)

    x = -7463847412
    expected = -2147483647
    print(reverse_integer(x) == expected)

    x = -8463847412
    expected = -2147483648
    print(reverse_integer(x) == expected)

    x = -9463847412
    expected = 0
    print(reverse_integer(x) == expected)

    x = -8463847413
    expected = 0
    print(reverse_integer(x) == expected)

    x = -8463847422
    expected = 0
    print(reverse_integer(x) == expected)


tests()
