'''
Element Swapping

https://leetcode.com/discuss/interview-question/848430/element-swapping-facebook-coding-practice-2020


Given a sequence of n integers arr, determine the lexicographically smallest
sequence which may be obtained from it after performing at most k element
swaps, each involving a pair of consecutive elements in the sequence.

Note: A list x is lexicographically smaller than a different equal-length
list y if and only if, for the earliest index at which the two lists differ,
x's element at that index is smaller than y's element at that index.

Signature
int[] findMinArray(int[] arr, int k)

Input
n is in the range [1, 1000].
Each element of arr is in the range [1, 1,000,000].
k is in the range [1, 1000].

Output
Return an array of n integers output, the lexicographically smallest sequence
achievable after at most k swaps.

Example 1
n = 3
k = 2
arr = [5, 3, 1]
output = [1, 5, 3]
We can swap the 2nd and 3rd elements, followed by the 1st and 2nd elements, 
to end up with the sequence [1, 5, 3]. This is the lexicographically smallest
sequence achievable after at most 2 swaps.

Example 2
n = 5
k = 3
arr = [8, 9, 11, 2, 1]
output = [2, 8, 9, 11, 1]
We can swap [11, 2], followed by [9, 2], then [8, 2].
'''


# Ot(n^2)
# Os(1)
def findMinArray(arr, k):
    cur = 0
    while k > 0 and cur < len(arr):
        minInWIx = get_min_in_w(arr, cur, k)
        # only swap if there is a gain
        if arr[cur] != arr[minInWIx]:
            swap(arr, cur, minInWIx)
        # cost of k
        cost = minInWIx - cur
        k -= cost
        cur += 1
    return arr


def get_min_in_w(arr, cur, k):
    # get the index of the min value in arr
    # between cur and k + 1
    ix = ''
    minVal = float('inf')
    for i in range(cur, cur + k + 1):
        if i < len(arr) and arr[i] < minVal:
            minVal = arr[i]
            ix = i
    return ix


def swap(arr, cur, minInWIx):
    # swaps adj until cur s reached
    while minInWIx > cur:
        arr[minInWIx - 1], arr[minInWIx] = arr[minInWIx], arr[minInWIx - 1]
        minInWIx -= 1


# Example 1
k = 2
arr = [5, 3, 1]
exp = [1, 5, 3]
print(findMinArray(arr, k) == exp)

# Example 2
k = 3
arr = [8, 9, 11, 2, 1]
exp = [2, 8, 9, 11, 1]
print(findMinArray(arr, k) == exp)

# Example 3
k = 4
arr = [8, 9, 11, 2, 1]
exp = [1, 8, 9, 11, 2]
print(findMinArray(arr, k) == exp)

# Example 4
k = 5
arr = [8, 9, 11, 2, 1]
exp = [1, 8, 9, 2, 11]
print(findMinArray(arr, k) == exp)

# Example 5
k = 6
arr = [8, 9, 11, 2, 1]
exp = [1, 8, 2, 9, 11]
print(findMinArray(arr, k) == exp)

# Example 6
k = 7
arr = [8, 9, 11, 2, 1]
exp = [1, 2, 8, 9, 11]
print(findMinArray(arr, k) == exp)

# Example 7
k = 2
arr = [8, 9, 11, 2, 1, 99]
exp = [8, 2, 9, 11, 1, 99]
print(findMinArray(arr, k) == exp)

# Example 8
k = 6
arr = [8, 9, 11, 2, 1, 99]
exp = [1, 8, 2, 9, 11, 99]
print(findMinArray(arr, k) == exp)

# Example 9
k = 3
arr = [9, 9, 9, 9, 1]
exp = [9, 1, 9, 9, 9]
print(findMinArray(arr, k) == exp)

# Example 10
k = 99
arr = [9, 9, 9, 9, 1]
exp = [1, 9, 9, 9, 9]
print(findMinArray(arr, k) == exp)

# Example 11
k = 99
arr = [999]
exp = [999]
print(findMinArray(arr, k) == exp)
