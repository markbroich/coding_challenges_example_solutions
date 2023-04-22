'''
Nearest neighbor in rgb color space
'''

import math
from typing import Dict


# Ot(n+k) Os(1) were n is the number of colors to try match against.
def nearest_color(incolor: tuple, matchcolors: Dict[str, tuple]) -> str:
    '''returns the name of color in matchcolors
    that incolor is nearest to.
    colors it a tuple in RGB (0-255 space)
    matchcolors is a dict with color names as keys
    and tuple in RGB (0-255 space) as values.
    '''
    nearest_color = ''
    min_dist = float('inf')
    # Ot(n) Os(1) were n is the number of colors to try match against.
    for key, value in matchcolors.items():
        # Ot(k) Os(1) were k is the number of input dimensions
        distance = euclidean_distance(incolor, value)
        if distance < min_dist:
            min_dist = distance
            nearest_color = key
    if nearest_color:
        return nearest_color
    return -1


# Ot(k) Os(1) were k is the number of input dimensions, which
# for an rgb color is three, so constant
def euclidean_distance(loc1: tuple, loc2: tuple) -> float:
    if len(loc1) != len(loc2):
        # input lenght differs
        return float('inf')
    mysum = 0
    for i in range(len(loc1)):
        mysum += (loc1[i] - loc2[i])**2
    return math.sqrt(mysum)


def tests():
    # matchcolors are incomplete so
    # matches will be to closest in matchcolor
    matchcolors = {
        'red': (255, 0, 0),
        'cyan': (0, 255, 255),
        'cerulean': (153, 181, 210),
        'pink': (255, 192, 20)
    }

    incolor = (255, 0, 0)  # red
    expected = 'red'
    print(nearest_color(incolor, matchcolors) == expected)

    incolor = (50, 0, 0)  # very dark red
    expected = 'red'
    print(nearest_color(incolor, matchcolors) == expected)

    incolor = (0, 139, 139)  # dark cyan
    expected = 'cyan'
    print(nearest_color(incolor, matchcolors) == expected)

    incolor = (0, 250, 0)  # dark green
    expected = 'cyan'
    print(nearest_color(incolor, matchcolors) == expected)

    incolor = (0, 0, 255)  # blue
    expected = 'cerulean'
    print(nearest_color(incolor, matchcolors) == expected)

    incolor = (255, 255, 0)  # yellow
    expected = 'pink'
    print(nearest_color(incolor, matchcolors) == expected)

    incolor = (128, 0, 128)  # purple
    expected = 'red'
    print(nearest_color(incolor, matchcolors) == expected)

    incolor = (128, 0)  # bad input
    expected = -1
    print(nearest_color(incolor, matchcolors) == expected)


tests()
