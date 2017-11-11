import numpy as np
from game.color import Color


class Tile(object):

    dt = np.dtype({'names': ['val', 'color'],
                   'formats': [np.uint16, np.uint64],
                   'titles': ['Tile Value', 'Tile Color']
                   })

    base_tile = (2, 0)
    blank_tile = (0, 0)

    def __init__(self):
        """

        """
        self._val = 1
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
    def color(self):
        """

        Returns:

        """
        return self._color
