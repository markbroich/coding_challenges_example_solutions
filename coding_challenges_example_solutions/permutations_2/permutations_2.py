'''
Permutations II

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''


# Worth case:
# O(g**d) where g is uniwue vlaues in nums and
# d is depth of the tree (which is len of nums)
#
# Tigher: O(n * n! / (n-k)!) where k iterares from 1, to 2, 3 ... to g.
# Which is the number of nodes in the tree (after dropping
# all overlaps)
def permutations(nums: list) -> list:
    res = []
    occurance_cnt = {}
    for i in nums:
        if i in occurance_cnt:
            occurance_cnt[i] += 1
        else:
            occurance_cnt[i] = 1

    def rec(cur: list, occurance_cnt: dict) -> list:
        if len(cur) == len(nums):
            res.append(cur)
            return
        for k in occurance_cnt:
            if occurance_cnt[k] > 0:
                occurance_cnt[k] -= 1
                rec(cur + [k], occurance_cnt)
                occurance_cnt[k] += 1

    rec([], occurance_cnt)
    return res


nums = [1,1,2]
expected = [[1,1,2], [1,2,1], [2,1,1]]
print(permutations(nums) == expected)

nums = [1,2,3]
expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(permutations(nums) == expected)