'''
https://leetcode.com/problems/encode-and-decode-strings 

Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded
back to the original list
of strings.

Machine 1 (sender) has the function:
string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:
string encoded_string = encode(strs);

and Machine 2 does:
vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods
(such as eval).

Example 1:
Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);

Example 2:
Input: dummy_input = [""]
Output: [""]

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] contains any possible characters out of 256 valid ASCII characters.
'''


# Solution 1
# when strs[i] contains any possible characters out of 256
# valid ASCII characters:
# Using a none ASCII character as a seperator
SEPERATOR = 'Â'  # a none ascii character


# Ot(m) where m is total chars
# Os(m + k) where k is wordcount
def encoder(list_of_words: str) -> str:
    encodered = ''
    for w in list_of_words:
        encodered += w
        encodered += (SEPERATOR)
    return encodered


# Ot(m + k) where k is wordcount
# Os(m) where m is total chars
def decoder(encodered: str) -> list:
    return encodered.split(SEPERATOR)[:-1]


def tests():
    list_of_words = ["Hello","World"]
    encodered = encoder(list_of_words)
    print(decoder(encodered) == list_of_words)

    list_of_words = [""]
    encodered = encoder(list_of_words)
    print(decoder(encodered) == list_of_words)


tests()


# Solution 2
# When strs[i] contains any possible characters:
# encode to bianry and encode word length at the beginning of
# each word
def char_to_int(character: str) -> int:
    return ord(character)


def int_to_binary(integer: int, depth=8) -> str:
    return bin(integer)[2:].zfill(depth)


def int_to_char(integer: int) -> str:
    return chr(int(integer))


def binanry_to_int(binary: str) -> int:
    return int(binary, 2)


def encoder_to_binary(list_of_words: str, depth=8) -> str:
    encodered = ''
    for w in list_of_words:
        # encode the wordlength to binary at the beginnig of each word
        character_count = len(w)
        binnary = int_to_binary(character_count, depth)
        encodered += binnary
        for c in w:
            integer = char_to_int(c)
            binnary = int_to_binary(integer, depth)
            encodered += binnary
    return encodered


def decoder_from_binary(encodered: str, depth=8) -> list:
    decoded = []
    start = 0
    end = depth

    while end < len(encodered):
        # get the wordlength as the first 'depth'-long
        # bin word
        word_len_bin = encodered[start: end]
        word_len_int = binanry_to_int(word_len_bin)

        start = end
        end = end + depth
        word = ''
        for i in range(word_len_int):
            binnary = encodered[start: end]
            char_as_int = binanry_to_int(binnary)
            word += int_to_char(char_as_int)
            start = end
            end = end + depth
        decoded.append(word)
    if not decoded:
        return ['']
    return decoded


def tests():
    print('')
    list_of_words = ["Hello","World"]
    encodered = encoder_to_binary(list_of_words, depth=8)
    print(decoder_from_binary(encodered, depth=8) == list_of_words)

    list_of_words = ["Hello","World"]
    encodered = encoder_to_binary(list_of_words, depth=16)
    print(decoder_from_binary(encodered, depth=16) == list_of_words)

    list_of_words = [""]
    encodered = encoder_to_binary(list_of_words, depth=8)
    print(decoder_from_binary(encodered, depth=8) == list_of_words)

    list_of_words = [""]
    encodered = encoder_to_binary(list_of_words, depth=16)
    print(decoder_from_binary(encodered, depth=16) == list_of_words)


tests()
