import numpy as np
from unittest import TestCase
from game.ndtile import NDTile
from game.tile import Tile


class TestNDTile(TestCase):

    def test_NDTile(self):
        tiles = NDTile()
        self.assertTrue(tiles.shape == (4, 4))
        self.assertTrue(tiles.dtype == Tile.dt)
        self.assertTrue(type(tiles) == NDTile)

        shape = (5, 5)
        tiles = NDTile(shape)
        self.assertTrue(tiles.shape == shape)
        self.assertTrue(tiles.dtype == Tile.dt)
        self.assertTrue(type(tiles) == NDTile)

    def test_zeros(self):
        tiles = NDTile.zeros((4,4))
        m, n = tiles.shape

        for i in range(m):
            for j in range(n):
                tile = tiles[i, j]
                self.assertTrue(0 == tile[0])
                self.assertTrue(0 == tile[1])
                self.assertTrue(0 == tile[2])
                
    def test_invalid_move(self):
        tiles = NDTile()
        self.assertRaises(ValueError, tiles.move, None)

    def test_move_left(self):
        self.fail()

    def test_move_right(self):
        self.fail()

    def test_move_up(self):
        self.fail()

    def test_move_down(self):
        self.fail()

