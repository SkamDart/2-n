import numpy as np
from game.color import Color


class Tile(object):

    dt = np.dtype({'names': ['val', 'is_visible', 'color'],
                   'formats': [np.uint16, np.uint16, np.uint64],
                   'titles': ['Tile Value', 'Tile Visibility', 'Tile Color']
                   })

    def __init__(self):
        self._val = 1
        self._is_visible = False
        self._color = Color.RED

    def __str__(self):
        return self._val

    @property
    def val(self):
        """
        :return:
        """
        return self._val

    @property
    def is_visible(self):
        """
        :return:
        """
        return self._is_visible

    @property
    def color(self):
        """

        :return:
        """
        return self._color
