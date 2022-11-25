'''
In this exercise, you're going to decompress a compressed string.
Your input is a compressed string of the format number[string] and the
decompressed output form should be the string written number times.

For example:

The input
3[abc]4[ab]c

Would be output as
abcabcabcababababc

Other rules

Number can have more than one digit. For example,
10[a]
is allowed, and just means
aaaaaaaaaa

One repetition can occur inside another. For example, 
2[3[a]b] 
decompresses into 
aaabaaab

Characters allowed as input include digits, small English letters and
brackets [ ].
Digits are only to represent amount of repetitions.
Letters are just letters.
Brackets are only part of syntax of writing repeated substring.
Input is always valid, so no need to check its validity.
'''


# Ot(n) Os(n) where n is sum(substring * factor) instances
# n is also the len of the result
def decode(input: str) -> str:
    num_stack = []
    char_stack = []
    result = ''
    idx = 0
    while idx <= len(input) - 1:
        if input[idx].isnumeric():
            number = ''
            while input[idx].isnumeric():
                number += input[idx]
                idx += 1
            num_stack.append(int(number))
        elif input[idx] != ']':
            char_stack.append(input[idx])
            idx += 1
        else:
            # found ], so unwinde to get substring
            substring = get_substring_from_char_stack(char_stack)
            substring = reverse_string(substring)
            # mulitply substring with last factor from num_stack
            # and add to char_stack
            if num_stack:
                factor = num_stack.pop()
            else:
                factor = 1
            char_stack = char_stack + list(factor * substring)
            idx += 1
    while len(char_stack) > 0:
        char = char_stack.pop()
        if char != '[':
            result += char
    return reverse_string(result)
    # return result[::-1]


# Ot(n) Os(n) where n is number of chars until next '['
def get_substring_from_char_stack(char_stack: str) -> str:
    char = char_stack.pop()
    substring = ''
    while char != '[':
        substring += char
        char = char_stack.pop()
    return substring


# Ot(n) Os(n) where n is length of input
def reverse_string(input: str) -> str:
    result = ''
    for i in range(len(input) - 1, -1, -1):
        result += input[i]
    return result


def tests():
    input = '3[abc]4[ab]c'
    exp = 'abcabcabcababababc'
    print(decode(input) == exp)

    input = '10[a]'
    exp = 'aaaaaaaaaa'
    print(decode(input) == exp)

    input = '2[3[a]b]'
    exp = 'aaabaaab'
    print(decode(input) == exp)

    input = 'a[]b'
    exp = 'ab'
    print(decode(input) == exp)

    input = '0[abc]'
    exp = ''
    print(decode(input) == exp)

    # this case requires a lot of data to be copied around for the
    # above code version.
    input = '1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[xx]]]]]]]]]]]]]]]]]]]]'
    exp = 'xx'
    print(decode(input) == exp)


tests()
