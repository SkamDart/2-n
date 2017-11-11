import numpy as np

from game.move import Move
from game.ndtile import NDTile
from game.tile import Tile


class Board(object):

    def __init__(self, goal=2048, dims=(4, 4)):
        """
        Constructor
        :param dims: (Int, Int)
        """
        self._goal = goal
        self._score = 0
        self._tiles = NDTile.zeros(dims)

    def __str__(self):
        """
        String representation for board
        :return:
        """
        return np.array_str(self.tiles)

    @property
    def tiles(self):
        """

        Returns:

        """
        return self._tiles

    @property
    def is_over(self):
        """

        Returns:

        """
        return self.is_full or self.has_reached_score

    @property
    def score(self):
        """

        Returns:

        """
        return self._score

    @property
    def goal(self):
        """

        Returns:

        """
        return self._goal

    @property
    def has_reached_score(self):
        return self.score >= self.goal

    @property
    def is_full(self):
        """
        Determines whether all squares are filled on the board
        :return:
        """
        m, n = self.tiles.shape
        for i in range(m):
            for j in range(n):
                if Tile.blank_tile[0] == self.tiles[i, j][0]:
                    return False
        return True

    def print(self):
        """ Removes none score components from board
        Returns:
        """
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                print(self._tiles[i, j][0], end=' ')
            print('\n')

    def shift(self, direction):
        """

        Args:
            direction:
        """
        if direction == Move.UP:
            self.tiles.shift_up()
        elif direction == Move.DOWN:
            self.tiles.shift_down()
        elif direction == Move.LEFT:
            self.tiles.shift_left()
        elif direction == Move.RIGHT:
            self.tiles.shift_right()
        else:
            raise ValueError('Invalid Tile Move')
