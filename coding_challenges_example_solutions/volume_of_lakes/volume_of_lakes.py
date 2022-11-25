'''
Imagine an island that is in the shape of a bar graph. When it rains, certain
areas of the island 
fill up with rainwater to form lakes. Any excess rainwater the island cannot
hold in lakes will run off the island to the west or east and drain
into the ocean.

Given an array of positive integers representing 2-D bar heights, design an
lgorithm (or write a function)
that can compute the total volume (capacity) of water that could be held in
all lakes on such an island given an array of the heights of the bars.
Assume an elevation map where the width of each bar is 1.

Example: Given [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2], return 15
(3 bodies of water with volumes of
1, 7, 7 yields total volume of 15)

input = [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2]
exp = 15
'''

# edge caees: flat, no depressions, lenght == < 3

from typing import Tuple

# Ot(n), Os(1)
def get_lake_volume(input: list) -> int:
    volume = 0
    if not input or len(input) < 3: 
        return volume

    left, right = get_left_right_start(input)
    high_left = input[left]
    high_right = input[right]
    high_max = max(input[left],  input[right])

    while left < right - 1:
        if input[right] < high_max:
            right -= 1
            volume += max(high_right - input[right], 0)
        elif input[left] < high_max:
            left += 1
            volume += max(high_left - input[left], 0)
        elif left + 1 < right - 1:
            # if both pointers can be moved
            right -= 1
            left += 1
            volume += max(high_right - input[right], 0)
            volume += max(high_left - input[left], 0)
        else:
            # move only one pointers
            right -= 1
            volume += max(high_right - input[right], 0)            
        high_left = max(high_left, input[left])
        high_right = max(high_right, input[right])
        high_max = max(high_max, input[left],  input[right])
    return volume


def get_left_right_start(input: list) -> Tuple:
    '''if one step in from the start on the left or
    right is a decend, then use start as bounds on
    that side, else, climb up the slope until at
    the top and use it as the bound'''
    left = 0        
    right = len(input) - 1
    bround = 0
    while bround < 2 and left < right:
        if input[left] <= input[left + 1]:
            if input[left] < input[left + 1]:
                bround += 1
            left += 1
        else:
            bround += 1

        if input[right - 1] >= input[right]:
            if input[right - 1] > input[right]:
                bround += 1
            right -= 1
        else:
            bround += 1
    return left, right



input = [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2]
exp = 15
print(get_lake_volume(input) == exp)


# single ridge, or flat
input = [1, 2, 1]
exp = 0
print(get_lake_volume(input) == exp)

input = [1, 2, 2, 1]
exp = 0
print(get_lake_volume(input) == exp)

input = [2, 2, 2, 2, 2]
exp = 0
print(get_lake_volume(input) == exp)

input = [2, 3, 2, 2, 2]
exp = 0
print(get_lake_volume(input) == exp)

input = [5]
exp = 0
print(get_lake_volume(input) == exp)

input = [5, 6]
exp = 0
print(get_lake_volume(input) == exp)


# on valley with bounds at the end

input = [2, 1, 2]
exp = 1
print(get_lake_volume(input) == exp)

input = [1, 0, 1]
exp = 1
print(get_lake_volume(input) == exp)

input = [0, -1, 0]
exp = 1
print(get_lake_volume(input) == exp)

input = [2, 1, 1, 2]
exp = 2
print(get_lake_volume(input) == exp)

input = [1, 0, 0, 1]
exp = 2
print(get_lake_volume(input) == exp)

# on valley with bounds one step in
input = [1, 2, 1, 1, 2, 1]
exp = 2
print(get_lake_volume(input) == exp)


