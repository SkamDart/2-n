import numpy as np

from game.move import Move
from game.ndtile import NDTile
from game.tile import Tile


class Board(object):

    def __init__(self, goal=2048, shape=(4, 4)):
        """Constructor

        Args:
            goal:
            shape:
        """
        self._goal = goal
        self._tiles = np.zeros(shape, dtype=np.int)

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

    @tiles.setter
    def tiles(self, tiles):
        self._tiles = tiles

    @property
    def is_full(self):
        """
        Determines whether all squares are filled on the board
        :return:
        """
        tiles = self.tiles
        return np.count_nonzero(tiles) == (tiles.shape[0] * tiles.shape[1])

    def print(self):
        """ Removes none score components from board
        Returns:
        """
        print(self.tiles)

    def is_open(self, pt):
        """

        Args:
            pt:

        Returns:

        """
        return self.tiles[pt] == 0

    def inject_random(self):
        """
        Returns:

        """
        """
        Adds random tile with uniform sample
        :return:
        """
        tiles = self.tiles
        x = 0
        y = 0
        dx = tiles.shape[0]
        dy = tiles.shape[1]

        while True:
            tx = np.random.randint(x, dx, 1)[0]
            ty = np.random.randint(y, dy, 1)[0]
            pt = (tx, ty)
            if self.is_open(pt):
                self.set_tile(pt, 2)
                break

    def set_tile(self, pt, val):
        """
        Args:
            pt:
            val:

        Returns:

        """
        self.tiles[pt] = val

    def move_zeros(self, axis=0):
        """
        FIXME (REFACTOR)
        Returns:

        """
        tiles = self.tiles
        #m = tiles.shape[0]
        n = tiles.shape[1]
        # n = tiles.shape[0] if axis == 0 else tiles.shape[1]

        for i, row in enumerate(tiles):
            if np.count_nonzero(row) != n:
                row = np.array(list(filter(None, row)))
                if axis == 1:
                    tiles[i] = np.append(np.zeros(n - len(row)), row)
                else:
                    tiles[i] = np.append(row, np.zeros(n - len(row)))

    def vertical(self, axis=0):
        """
        FIXME (REFACTOR)
        Args:
            axis:

        Returns:

        """
        tiles = self.tiles.T

        n = tiles.shape[1]

        for i, row in enumerate(tiles):
            if np.count_nonzero(row) != n:
                row = np.array(list(filter(None, row)))
                if axis == 1:
                    tiles[i] = np.append(np.zeros(n - len(row)), row)
                else:
                    tiles[i] = np.append(row, np.zeros(n - len(row)))
        tiles = tiles.T

    def merge(self, axis=0):
        """
        Args:
            axis:

        Returns:

        """
        for row in self.tiles:
            self.merge_row(row, axis)

    def merge_row(self, row, axis=0):
        """
        TODO (REFACTOR, HACK)
        Args:
            row:
            axis:

        Returns:

        """
        b = len(row) - 1
        can_merge = True
        for i in range(b):
            if row[i] == row[i + 1] and can_merge:
                if axis == 0:
                    row[i + 1] = 0
                    row[i] *= 2
                elif axis == 1:
                    row[i] = 0
                    row[i + 1] *= 2
                can_merge = False
                continue
            can_merge = True

    def merge_vertical(self, axis=0):
        """

        Returns:

        """
        self.tiles = self.tiles.T

        for row in self.tiles:
            self.merge_row(row, axis)

        self.tiles = self.tiles.T

    def shift(self, direction):
        """

        Args:
            direction:
        """
        if direction == Move.UP:
            self.vertical()
            self.merge_vertical()
            self.vertical()
        elif direction == Move.DOWN:
            self.vertical(1)
            self.merge_vertical(1)
            self.vertical(1)
        elif direction == Move.LEFT:
            self.move_zeros()
            self.merge()
            self.move_zeros()
        elif direction == Move.RIGHT:
            self.move_zeros(1)
            self.merge(1)
            self.move_zeros(1)
        else:
            raise ValueError('Invalid Tile Move')
