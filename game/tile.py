import numpy as np
from game.color import Color


class Tile(object):

    dt = np.dtype({'names': ['val', 'is_visible', 'color'],
                   'formats': [np.uint16, np.uint16, np.uint64],
                   'titles': ['Tile Value', 'Tile Visibility', 'Tile Color']
                   })
    base_tile = (2, 0, 0)
    blank_tile = (0, 0, 0)

    def __init__(self):
        """

        """
        self._val = 1
        self._is_visible = False
        self._color = Color.RED

    def __str__(self):
        """

        Returns:

        """
        return self._val

    @property
    def val(self):
        """

        Returns:

        """
        return self._val

    @property
    def is_visible(self):
        """

        Returns:

        """
        return self._is_visible

    @property
    def color(self):
        """

        Returns:

        """
        return self._color
