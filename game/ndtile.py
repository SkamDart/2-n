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
        obj.is_running = True
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

    def move(self, direction):
        """

        Args:
            direction:
        """
        if direction == Move.UP:
            self.move_up()
        elif direction == Move.DOWN:
            self.move_down()
        elif direction == Move.LEFT:
            self.move_left()
        elif direction == Move.RIGHT:
            self.move_right()
        else:
            raise ValueError('Invalid Tile Move')

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

    def move_left(self):
        """

        """
        pass

    def move_right(self):
        """

        """
        pass

    def move_down(self):
        """

        """
        pass

    def move_up(self):
        """

        """
        pass

