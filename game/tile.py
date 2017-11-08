import numpy as np
from game.color import Color

class Tile(object):

    dt = np.dtype([
        ('val', np.uint16),
        ('isVisible', np.bool),
        ('color', np.uint64)
    ])

    def __init__(self):
        self.value = 1
        self.isVisible = False
        self.color = Color.RED

    def __str__(self):
        return self.value

    def increment(self):
        self.value *= 2

    def decrement(self):
        self.value /= 2

    def changeColor(self, color):
        self.color = color



