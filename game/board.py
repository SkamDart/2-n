import numpy as np

class Board(object):

    def __init__(self, dims=(4,4)):
        """
        Constructor
        :param dims: (Int, Int)
        """
        self._board = np.array(dims, dtype=Tile.dt)

    def __getitem__(self, pos):
        try:
            return self.board[pos]
        except (TypeError, IndexError) as e:
            pass

    @property
    def board(self):
        return self._board

    def __str__(self):
        """
        String representation for board
        :return:
        """
        return np.array_str(self._board)

    def isFull(self):
        """
        Determines whether all squares are filled on the board
        :return:
        """
        pass


    def isOpen(self, loc):
        """
        :param tile:
        :return:
        """
        pass

    def injectRandom(self):
        """
        Adds random tile with uniform  sample
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