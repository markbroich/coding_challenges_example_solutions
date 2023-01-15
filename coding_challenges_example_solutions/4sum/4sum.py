'''
Given an array nums of n integers, return an array of all the unique
quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[1, 0, -1, 0], [1, -1, -2, 2], [0, 0, -2, 2]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''

# Ot(n**4 * 4log(4))
# Os(n)
def four_sum_brute_forth(nums: list, target: int) -> list:
    if not nums:
        return []
    res = []
    seen = set()
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                for m in range(k + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] + nums[m] == target:
                        sorted_tuple = get_sorted_tuple(nums, i, j, k, m)
                        # print(sorted_tuple)
                        # print(type(sorted_tuple))
                        if sorted_tuple not in seen:
                            seen.add(sorted_tuple)
                            res.append([nums[i], nums[j], nums[k], nums[m]])
    return res


def get_sorted_tuple(nums, i, j, k, m):
    return tuple(sorted([nums[i], nums[j], nums[k], nums[m]]))


# O(splits ** n) so O(2**n)
def four_sum_rec(nums: list, target: int) -> list:
    res = []

    def rec(idx: int, indices: list, total: int):
        if len(indices) == 4 and total == target:
            res.append([nums[i] for i in indices])
            return
        elif len(indices) >= 4:
            return
        if idx == len(nums):
            return
        rec(idx + 1,  indices + [idx], total + nums[idx])
        rec(idx + 1,  indices, total)

    rec(0, [], 0)
    return de_duplicate(res)


#############
def quadrupe_list(nums, target):
    res = []
    def hasQuadruplet(nums, n, target, count, indices):
        # if the desired sum is reached with 4 elements, return true
        if target == 0 and count == 4:
            res.append([nums[i] for i in indices])
            return
        # return false if the sum is not possible with the current
        # configuration
        if count > 4 or n == 0:
            return
        # Recur with
        # 1. Including the current element
        # 2. Excluding the current element
        hasQuadruplet(nums, n - 1, target - nums[n - 1], count + 1, indices + [n - 1])
        hasQuadruplet(nums, n - 1, target, count, indices)

    hasQuadruplet(nums, len(nums), target, 0, [])    
    return de_duplicate(res)


# Ot(n) where n is len of res. Os(k + k) where k is
# length of unique results
def de_duplicate(res: list) -> list:
    res_deduplicated = []
    seen = set()
    for r in res:
        if tuple(r) not in seen:
            res_deduplicated.append(r)
            seen.add(tuple(r))
    return res_deduplicated


# Ot(n**2 * (4 + 4log(4)) + k) Os(n**2 * 4 + 4)
# where k is number of items in res set
def quadrupe_using_dict(nums: list, target: int) -> list:
    res = set()
    memo = {}
    # Ot(n**2)
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            current_sum = nums[i] + nums[j]
            if current_sum in memo:
                for combination in memo[current_sum]:
                    if (i != combination[0] and j != combination[1])\
                       and (i != combination[1] and j != combination[0]):
                        # Ot(4 + 4log(4)) Os(4 + 4)
                        res.add(tuple(sorted([nums[i], nums[j],
                                nums[combination[0]], nums[combination[1]]])))
            if target - current_sum in memo:
                found = False
                for combination in memo[target - current_sum]:
                    if (combination[0] == nums[i]
                       and combination[1] == nums[j]
                       or combination[1] == nums[i]
                       and combination[0] == nums[j]):
                        found = True
                if not found:
                    memo[target - current_sum].add(tuple([i, j]))
            else:
                memo[target - current_sum] = set([tuple([i, j])])
    # Ots(k) where k is number of items in res set
    return [list(r) for r in res]


def testing():
    nums = [1,0,-1,0,-2,2]
    target = 0
    exp = [[1, 0, -1, 0], [1, -1, -2, 2], [0, 0, -2, 2]]
    print(four_sum_brute_forth(nums, target) == exp)
    print(quadrupe_list(nums, target))
    print(quadrupe_list(nums, target) == exp)
    print(four_sum_rec(nums, target) == exp)
    print('d', quadrupe_using_dict(nums, target))

    nums = [2,2,2,2,2]
    target = 8
    exp = [[2,2,2,2]]
    print(four_sum_brute_forth(nums, target) == exp)
    print(quadrupe_list(nums, target) == exp)
    print(four_sum_rec(nums, target) == exp)
    print('d', quadrupe_using_dict(nums, target))
   


testing()
