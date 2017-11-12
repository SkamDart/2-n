import numpy as np

from game.move import Move
from game.ndtile import NDTile
from game.tile import Tile


class Board(object):

    def __init__(self, goal=2048, shape=(4, 4)):
        """
        Constructor
        :param shape: (Int, Int)
        """
        self._goal = goal
        #self._tiles = NDTile.zeros(dims)
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
        print (self.tiles)

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
        pt = None

        while True:
            tx = np.random.randint(x, dx, 1)[0]
            ty = np.random.randint(y, dy, 1)[0]
            pt = (tx, ty)
            if self.is_open(pt):
                break

        self.set_tile(pt, 2)

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

        Returns:

        """
        tiles = self.tiles
        m = tiles.shape[0]
        n = tiles.shape[1]
        # n = tiles.shape[0] if axis == 0 else tiles.shape[1]

        for i, row in enumerate(tiles):
            if np.count_nonzero(row) != n:
                row = np.array(list(filter(None, row)))
                if axis == 1:
                    tiles[i] = np.append(np.zeros(n - len(row)), row)
                else:
                    tiles[i] = np.append(row, np.zeros(n - len(row)))

    def shift_right(self):
        """

        """
        pass

    def shift_down(self):
        """

        """
        pass

    def shift_up(self):
        """

        """
        pass

    def shift_left(self):
        """
        Returns:

        """
        tiles = self.tiles
        # for i, row in enumerate(tiles):

        pass

    def shift(self, direction):
        """

        Args:
            direction:
        """
        if direction == Move.UP:
            self.shift_up()
        elif direction == Move.DOWN:
            self.shift_down()
        elif direction == Move.LEFT:
            self.move_zeros()
            self.shift_left()
        elif direction == Move.RIGHT:
            self.move_zeros(1)
            self.shift_right()
        else:
            raise ValueError('Invalid Tile Move')
