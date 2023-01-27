'''
Distribute Candies

Alice has n candies, where the ith candy is of type candyType[i].
Alice noticed that she started to gain weight, so she visited a doctor.

The doctor advised Alice to only eat n / 2 of the candies she has
(n is always even).
Alice likes her candies very much, and she wants to eat the maximum number
of different types of candies while still following the doctor's advice.

Given the integer array candyType of length n, return the maximum number of
different types of candies she can eat if she only eats n / 2 of them.

Example 1:
Input: candyType = [1,1,2,2,3,3]
Output: 3
Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.

Example 2:
Input: candyType = [1,1,2,3]
Output: 2
Explanation: Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2], [1,3], or [2,3], she still can only eat 2 different types.

Example 3:
Input: candyType = [6,6,6,6]
Output: 1
Explanation: Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.
'''


# Ot(n) Os(k) where n is length of the arr and k
# is the number of different candys
def distribute_candy(arr):
    # Ot(n) Os(k)
    kind_count = len(set(arr))
    max_candy = len(arr) / 2
    if max_candy > kind_count:
        return kind_count
    else:
        return max_candy


def tests():
    candyType = [1,1,2,2,3,3]
    exp = 3
    print(distribute_candy(candyType) == exp)

    candyType = [1,1,2,3]
    exp = 2
    print(distribute_candy(candyType) == exp)

    candyType = [6,6,6,6]
    exp = 1
    print(distribute_candy(candyType) == exp)

    candyType = [6,6]
    exp = 1
    print(distribute_candy(candyType) == exp)

    candyType = [1,2,2,2,3,3,4,4]
    exp = 4
    print(distribute_candy(candyType) == exp)

tests()
