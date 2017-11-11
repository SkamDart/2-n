import numpy as np
from game.tile import Tile
from game.move import Move


class NDTile(np.ndarray):
    """
    Subclass of ndarray. Allows us to create and use typical np ndarray
    functionality with a custom data type.
    Create the ndarray instance of our type Tile, given the usual
    ndarray input arguments.  This will call the standard
    ndarray constructor, but return a ndtile instance.
    It also triggers a call to NDTile.__array_finalize__
    """

    def __new__(subtype, shape=(4,4), buffer=None, offset=0,
                strides=None, order=None, info=None):
        """

        Args:
            shape:
            buffer:
            offset:
            strides:
            order:
            info:

        Returns:

        """
        dtype = Tile.dt
        obj = np.ndarray.__new__(subtype, shape, dtype, buffer, offset, strides,
                                 order)
        return obj

    def __array_finalize__(self, obj):
        """
        ``self`` is a new object resulting from
        ndarray.__new__(NDTile, ...), therefore it only has
        attributes that the ndarray.__new__ constructor gave it -
        i.e. those of a standard ndarray.

       We could have got to the ndarray.__new__ call in 3 ways:
       From an explicit constructor - e.g. NDTile():
       obj is None
       (we're in the middle of the NDTile.__new__
       constructor, and self.is_running will be set when we return to
       NDTile.__new__)

        Args:
            obj:

        Returns:

        """
        if obj is None:
            return

        self.is_running = getattr(obj, 'is_running', True)

    @staticmethod
    def zeros(shape):
        """Zeros out all elements in the ndtile tuple

        Args:
            shape: dimensions of matrix

        Returns:
            zero'd out matrix with provided shape
        """
        # return map(lambda x: (0, ) * len(x), np.nditer(NDTile(shape), flags=['refs_ok']))

        m, n = shape
        tiles = NDTile(shape)
        for i in range(n):
            for j in range(m):
                tiles[i, j] = (0,) * len(tiles[i, j])
        return tiles

    def get_score(self, pos):
        """

        Args:
            pos:

        Returns:

        """
        try:
            self.item(pos)[0]
        except IndexError as err:
            print (err.args)
            raise ValueError('Invalid Index')

    def get_color(self, pos):
        """

        Args:
            pos:

        Returns:

        """
        try:
            self.item(pos)[1]
        except IndexError as err:
            print (err.args)
            raise ValueError('Invalid Index')

    def is_open(self, pt):
        """
        Args:
            pt:

        Returns:

        """
        return self.item(pt)[0] == Tile.blank_tile[0]

    def shift_left(self):
        """

        Returns:

        """
        m = self.shape[0]
        n = self.shape[1]

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

    def set_tile(self, pt, val):
        """
        Args:
            pt:
            val:

        Returns:

        """
        self.itemset(pt, val)

    def inject_random(self):
        """
        Adds random tile with uniform sample
        :return:
        """
        x = 0
        y = 0
        dx = self.shape[0]
        dy = self.shape[1]
        pt = None

        while True:
            tx = np.random.randint(x, dx, 1)[0]
            ty = np.random.randint(y, dy, 1)[0]
            pt = (tx, ty)
            if self.is_open(pt):
                break

        self.set_tile(pt, Tile.base_tile)