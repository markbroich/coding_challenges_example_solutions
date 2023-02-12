'''Combination Sum

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen
numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique
combinations that sum up to target is less than 150 combinations
for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. 
Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Example 3:
Input: candidates = [2], target = 1
Output: []

Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
'''


# O(split ** tree_depth) where splits is equal to len of candidates. 
# tree depth will vary with a max of len of candidates.
def combination_sum(candidates: list, target: int):
    combinations = []
    seen = set()
    candidates.sort()

    def rec(cur: list, cur_sum: int):
        if cur_sum == target:
            cur.sort()
            cur_str = str(cur)
            if len(seen) == 0:
                combinations.append(cur)
                seen.add(cur_str)
            elif cur_str not in seen:
                seen.add(cur_str)
                combinations.append(cur)
            return
        elif cur_sum > target:
            return
        for c in candidates:
            rec(cur + [c], cur_sum + c)

    rec([], 0)
    return combinations


# O(t**t) where t is length candidates. So this is worth case
# where we use each element in candidates
def combination_sum(candidates: list, target: int):
    combinations = []
    candidates.sort()

    def rec(i: int, cur: list, cur_sum: int):
        if cur_sum == target:
            combinations.append(cur)
            return
        elif cur_sum > target:
            return
        for j in range(i, len(candidates)):
            rec(j, cur + [candidates[j]], cur_sum + candidates[j])

    rec(0, [], 0)
    return combinations


def tests():
    candidates = [2,3,6,7]
    target = 7
    expected = [[2,2,3], [7]]
    print(combination_sum(candidates, target) == expected)

    candidates = [2,3,5]
    target = 8
    expected = [[2,2,2,2], [2,3,3], [3,5]]
    print(combination_sum(candidates, target) == expected)

    candidates = [2]
    target = 1
    expected = []
    print(combination_sum(candidates, target) == expected)


tests()