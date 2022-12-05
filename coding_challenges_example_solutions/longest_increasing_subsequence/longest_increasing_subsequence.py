'''Given an integer array nums, return the length of the longest strictly
increasing subsequence.


Example 1:

nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101],
therefore the length is 4.
Example 2:

nums = [0,1,0,3,2,3]
Output: 4
Example 3:

nums = [7,7,7,7,7,7,7]
Output: 1
'''


# def longest_increasing_subsequence(arr: list) -> int:
#     # arr = sorted(arr, key = lambda()
#     # print(arr)
#     arr_index = []
#     for i, num in enumerate(arr):
#         arr_index.append((num, i))
#     arr_index.sort(key=lambda a: (a[0], a[1]))
#     print(arr_index)

#     # current = float('-inf')
#     # count = 0
#     # for num in arr:
#     #     if num > current:
#     #         current = num
#     #         count += 1
#     #     else:
#     #         break
#     # return count


# Ot(2**n) Os(1) but extra space will be used for stack memory
def longest_increasing_subsequence(arr: list) -> int:
    n = len(arr)

    def recure(i: int, last: int) -> int:
        if i == n - 1:
            if arr[i] > last:
                return 1
            else:
                return 0

        result = -1
        longest_taken = 0
        if arr[i] > last:
            # each time an intem can be taken or skipped
            # hence, 2 choices n times = Ot(2**n)
            longest_taken = recure(i + 1, arr[i]) + 1
        for j in range(i, n - 1):
            longest_skipped = recure(j + 1, last)
            result = max(result, longest_taken, longest_skipped)
        return result

    return recure(0, float('-inf'))


# another recursion
def longest_increasing_subsequence_anohter(arr: list) -> int:
    n = len(arr)

    def recure(i: int, last: int, longest: int) -> int:
        if i == n:
            return longest
        result = -1
        longest_taken = -1
        if arr[i] > last:
            longest_taken = recure(i + 1, arr[i],  longest + 1)
        for j in range(i, n):
            longest_skipped = recure(j + 1, last, longest)
            result = max(result, longest_taken, longest_skipped)
        return result

    return recure(0, float('-inf'), 0)


# Ot(n**2) Os(n) using memorization
# + extra space will be used for stack memory proportional to n
def longest_increasing_subsequence_memo(arr):
    memo = {}

    def recure(j):
        if j in memo:
            return memo[j]
        longest = 1
        for k in range(0, j):
            if arr[k] < arr[j] and recure(k) + 1 > longest:
                longest = recure(k) + 1
        memo[j] = longest
        return memo[j]

    max_length = 0
    for i in range(len(arr)):
        cur_length = recure(i)
        if max_length < cur_length:
            max_length = cur_length
    return max_length



def tests():
    nums = [1, 2, 1, 3]
    exp = 3
    print(longest_increasing_subsequence(nums) == exp)
    print(longest_increasing_subsequence_anohter(nums) == exp)
    print(longest_increasing_subsequence_memo(nums) == exp)

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    exp = 4
    print(longest_increasing_subsequence(nums) == exp)
    print(longest_increasing_subsequence_anohter(nums) == exp)
    print(longest_increasing_subsequence_memo(nums) == exp)

    nums = [1, 3, 2, 4]
    exp = 3
    print(longest_increasing_subsequence(nums) == exp)
    print(longest_increasing_subsequence_anohter(nums) == exp)
    print(longest_increasing_subsequence_memo(nums) == exp)

    nums = [7, 7, 7, 7, 7, 7, 7]
    exp = 1
    print(longest_increasing_subsequence(nums) == exp)
    print(longest_increasing_subsequence_anohter(nums) == exp)
    print(longest_increasing_subsequence_memo(nums) == exp)

    nums = [0, 1, 0, 3, 2, 3]
    exp = 4
    print(longest_increasing_subsequence(nums) == exp)
    print(longest_increasing_subsequence_anohter(nums) == exp)
    print(longest_increasing_subsequence_memo(nums) == exp)

    nums = [1, 5, 2, 3, 4, 7, 2]
    exp = 5
    print(longest_increasing_subsequence(nums) == exp)
    print(longest_increasing_subsequence_anohter(nums) == exp)
    print(longest_increasing_subsequence_memo(nums) == exp)


tests()
