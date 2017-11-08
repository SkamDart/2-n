import numpy as np
from game.tile import Tile

"""
Subclasses of ndarray
"""


class NDTile(np.ndarray):
    """
    Create the ndarray instance of our type, given the usual
    ndarray input arguments.  This will call the standard
    ndarray constructor, but return an object of our type.
    It also triggers a call to NDTile.__array_finalize__
    """

    def __new__(subtype, shape, buffer=None, offset=0,
                strides=None, order=None, info=None):
        dtype = Tile.dt
        obj = np.ndarray.__new__(subtype, shape, dtype, buffer, offset, strides,
                                 order)
        obj.is_running = True
        return obj

    def __array_finalize__(self, obj):
        # ``self`` is a new object resulting from
        # ndarray.__new__(NDTile, ...), therefore it only has
        # attributes that the ndarray.__new__ constructor gave it -
        # i.e. those of a standard ndarray.
        #
        # We could have got to the ndarray.__new__ call in 3 ways:
        # From an explicit constructor - e.g. NDTile():
        #    obj is None
        #    (we're in the middle of the NDTile.__new__
        #    constructor, and self.is_running will be set when we return to
        #    NDTile.__new__)
        if obj is None:
            return
        # From view casting - e.g arr.view(NDTile):
        #    obj is arr
        #    (type(obj) can be NDTile)
        # From new-from-template - e.g ndtile[:3]
        #    type(obj) is NDTile
        #
        # Note that it is here, rather than in the __new__ method,
        # that we set the default value for 'is_running', because this
        # method sees all creation of default objects - with the
        # NDTile.__new__ constructor, but also with
        # arr.view(NDTile).
        self.is_running = getattr(obj, 'is_running', True)
        # We do not need to return anything
