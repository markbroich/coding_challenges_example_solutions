'''
Count Number of Ways to Place Houses

There is a street with n * 2 plots, where there are n plots on each side of
the street. The plots on each side are numbered from 1 to n. On each plot,
a house can be placed.

Return the number of ways houses can be placed such that no two houses are
adjacent to each other on the same side of the street. Since the answer may
be very large, return it modulo 109 + 7.

Note that if a house is placed on the ith plot on one side of the street,
a house can also be placed on the ith plot on the other side of the street.

Example 1:
Input: n = 1
Output: 4

Explanation:
Possible arrangements:
1. All plots are empty.
2. A house is placed on one side of the street.
3. A house is placed on the other side of the street.
4. Two houses are placed, one on each side of the street.

Example 2:
Input: n = 2
Output: 9

Explanation: The 9 possible arrangements are shown in the diagram above.

Constraints:
1 <= n <= 104
'''

'''
Lots on eihter side of the street are independent from each other. So, can
can be modeled seperately.
And final result is permutation_count_of_one * permutation_count_of_the_other.

Solution: Dynamic programming (so bottom up).
One side of the street can either have an empty space or a house
as the last lot.
For n == 1, the last and the first lot are the same and
there is 1 way for last_empty and 1 way to last_w_house.

last_empty = 1
last_w_house = 1

A house can only be added after an empty lot. So,
last_w_house = last_empty (we do not add options)

But an empty lot can be added after either an empty lot or after a house. So,
last_empty = last_w_house + last_empty.

So, for n = 2:
First lot:
last_empty = 1
last_w_house = 1
Second lot:
last_w_house = last_empty # 1
last_empty = last_w_house + last_empty # 2
Then I add both trails:
permutations_one_side_of_street = last_w_house + last_empty
Result: 3
permutations_one_side_of_street * permutations_one_side_of_street
Result for both sides of the street: 9

For n = 3
First lot:
last_empty = 1
last_w_house = 1
Second lot:
last_w_house = last_empty  # 1
last_empty = last_w_house + last_empty # 2
Third lot:
last_w_house = last_empty # 2
last_empty = last_w_house + last_empty # 3
Then I add both trails:
permutations_one_side_of_street = last_w_house + last_empty
Result: 5
permutations_one_side_of_street * permutations_one_side_of_street
Result for both sides of the street: 25
'''


# Ot(2**n) Os(1)
class Solution:
    def __init__(self, n):
        self.n = n

    def countHousePlacements(self) -> int:
        last_empty = last_w_house = 1
        for i in range(1, self.n):
            # house can only be added after an empty lot
            # and there is no increase in options
            new_last_w_house = last_empty
            # an empty lot can be added after either
            new_last_empty = last_w_house + last_empty
            last_w_house = new_last_w_house
            last_empty = new_last_empty
        permustions_one_side_of_street = last_w_house + last_empty
        return permustions_one_side_of_street * permustions_one_side_of_street


def tests():
    n = 1
    exp = 4
    S1 = Solution(n)
    print(S1.countHousePlacements() == exp)

    n = 2
    exp = 9
    S1 = Solution(n)
    print(S1.countHousePlacements() == exp)

    n = 3
    exp = 25
    S1 = Solution(n)
    print(S1.countHousePlacements() == exp)


tests()
