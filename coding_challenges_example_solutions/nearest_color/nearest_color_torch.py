'''
Nearest neighbor in rgb color space.

For a large dict of reference_colors,
this class build around torch should
run faster than nearest_color.py
given that the dist cal against
each all reference_colors is done
in parallel.
'''

import torch
from typing import Dict, Tuple


class Nearest_Color:
    def __init__(self, reference_colors: Dict[str, tuple]):
        '''reference_colors is a dict with color names as keys
        and tuple in RGB (0-255 space) as values.'''
        self.row_to_color = {i: key
            for i, key in enumerate(reference_colors.keys())}
        self.match_colors = torch.tensor([row
            for row in reference_colors.values()])

    def get_nearest(self, in_color: Tuple[int, int, int]) -> str:
        '''returns the name of color in reference_colors
        that incolor is nearest to.
        colors it a tuple in RGB (0-255 space)'''
        diff = self.match_colors - torch.tensor(in_color)
        diff_squared = torch.square(diff)
        diff_squared_summed = torch.sum(diff_squared, 1)
        idx_min = int(torch.argmin(diff_squared_summed))
        color_min_dist = self.row_to_color[idx_min]
        return color_min_dist


def tests():
    # reference_colors are incomplete so
    # matches will be to closest in matchcolor
    reference_colors = {
        'red': (255, 0, 0),
        'cyan': (0, 255, 255),
        'cerulean': (153, 181, 210),
        'pink': (255, 192, 20)
        }

    nc = Nearest_Color(reference_colors)

    expected = 'red'
    incolor = (255, 0, 0)  # red
    print(nc.get_nearest(incolor) == expected)

    expected = 'red'
    incolor = (50, 0, 0)  # very dark red
    print(nc.get_nearest(incolor) == expected)

    expected = 'cyan'
    incolor = (0, 139, 139)  # dark cyan
    print(nc.get_nearest(incolor) == expected)

    expected = 'cyan'
    incolor = (0, 250, 0)  # dark green
    print(nc.get_nearest(incolor) == expected)

    expected = 'cerulean'
    incolor = (0, 0, 255)  # blue
    print(nc.get_nearest(incolor) == expected)

    expected = 'pink'
    incolor = (255, 255, 0)  # yellow
    print(nc.get_nearest(incolor) == expected)

    expected = 'red'
    incolor = (128, 0, 128)  # purple
    print(nc.get_nearest(incolor) == expected)


tests()
