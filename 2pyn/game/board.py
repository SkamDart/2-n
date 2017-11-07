import numpy as np

class Board():

    def __init__(self, dims=(4,4)):
        """
        Constructor
        :param dim: (Int, Int)
        """
        self.board = np.zeros(dims)
        self.shape = dims

    def __str__(self):
        """
        String representation for board
        :return:
        """
        return np.array_str(self.board)

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

    def shift(self, direction):
        """
        Shifts a board one of the directions
        :see Move.py
        :param direction:
        :return:
        """
        pass