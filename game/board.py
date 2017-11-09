import numpy as np
from game.ndtile import NDTile


class Board(object):

    def __init__(self, dims=(4, 4)):
        """
        Constructor
        :param dims: (Int, Int)
        """
        self._tiles = NDTile.zeros(dims)
        self._dims = dims

    def __str__(self):
        """
        String representation for board
        :return:
        """
        return np.array_str(self.tiles)

    @property
    def tiles(self):
        return self._tiles

    @property
    def dims(self):
        return self._dims

    def is_full(self):
        """
        Determines whether all squares are filled on the board
        :return:
        """
        pass

    def base_tile(self):
        """

        Returns:

        """
        return (2, 0, 0)

    def set_tile(self, loc, val):
        self.tiles[loc] = val


    def is_open(self, loc):
        """
        :param loc:
        :return:
        """
        score = self.get_tile_score(loc)
        print ('tile score ', score)
        return True

    def inject_random(self):
        """
        Adds random tile with uniform sample
        :return:
        """
        x = 0
        y = 0
        dx = self.dims[0]
        dy = self.dims[1]
        pt = (x, y)
        while True:
            tx = np.random.randint(x, dx, 1)[0]
            ty = np.random.randint(y, dy, 1)[0]
            pt = (tx, ty)
            print ('pt ', pt)
            if self.is_open(pt):
                break


    def shift(self, move):
        """ Shifts a board one of the directions
        :see move.py
        :param move:
        :return:
        """
        pass

    def get_tile_score(self, loc):
        """Given

        Args:
            loc:

        Returns:

        """
        return self.tiles[loc][0]