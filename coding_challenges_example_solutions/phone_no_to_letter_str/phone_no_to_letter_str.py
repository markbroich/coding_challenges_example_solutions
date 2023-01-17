'''
Given a phone number that contains digits 2-9, find all possible letter
permutations the phone number could translate to.

  1 	 2		3
		ABC    D#F
  4		 5		6
  GHI   JKL	   MNO

  7		 8		9
  PQRS  TUV     WXYZ


Input:
number = "56"

Output:
["jm","jn","jo","km","kn","ko","lm","ln","lo"]
'''


# Ot(k**n) where n is len of number and k is number of options
# more secifically Ot(ka**n * kb**n) where ka = 3 and kb = 4
# Os(n) given that I explore one branch of the tree at a time.
def phone_no_to_letter_str(number: str, lookup: dict) -> list:
    if not number:
        return []

    def rec(i: int, letters: str) -> list:
        if i == len(number):
            return [letters]
        res = []
        if number[i] == '1':
            i += 1
        options = lookup[number[i]]
        for opt in options:
            res = res + rec(i + 1, letters + opt)
        return res

    return rec(0, '')


# same compelxity
def phone_no_to_letter_str_concise(number: str, lookup: dict) -> list:
    if not number:
        return []
    res = []

    def rec(i: int, letters: str) -> None:
        if i == len(number):
            res.append(letters)
        else:
            if number[i] == '1':
                i += 1
            [rec(i + 1, letters + opt) for opt in lookup[number[i]]]

    rec(0, '')
    return res


lookup = {'2': 'ABC', '3': 'D#F', '4': 'GHI', '5': 'JKL', '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'}
number = "56"
exp = ["JM","JN","JO","KM","KN","KO","LM","LN","LO"]
print(phone_no_to_letter_str(number, lookup) == exp)
print(phone_no_to_letter_str_concise(number, lookup) == exp)
