import numpy as np
from game.tile import Tile

class Board(object):

    def __init__(self, dims=(4,4)):
        """
        Constructor
        :param dims: (Int, Int)
        """
        self._board = np.empty(dims, dtype=Tile.dt)
        self._dims = dims

    def __str__(self):
        """
        String representation for board
        :return:
        """
        return np.array_str(self._board)

    @property
    def board(self):
        return self._board

    @property
    def dims(self):
        return self._dims

    def is_full(self):
        """
        Determines whether all squares are filled on the board
        :return:
        """
        pass

    def is_open(self, loc):
        """
        :param loc:
        :return:
        """
        pass

    def inject_random(self):
        """
        Adds random tile with uniform sample
        :return:
        """
        pass

    def shift(self, move):
        """
        Shifts a board one of the directions
        :see move.py
        :param direction:
        :return:
        """
        pass