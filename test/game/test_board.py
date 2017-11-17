from unittest import TestCase
from game.board import Board


class TestBoard(TestCase, object):
    def setUp(self):
        self.default = Board()
        self.custom = Board((5, 5))

    def test_board(self):
        self.assertTrue(self.default.tiles is not None)
        self.assertTrue(self.default.tiles.shape == (4, 4))

        self.assertTrue(self.custom.tiles is not None)
        self.assertTrue(self.custom.tiles.shape == (5, 5))

    def test_set_tile(self):
        pt = (0, 0)
        small = Board((2, 2))
        small.set_tile(pt, 4)
        self.assertTrue(small.tiles[pt] == 4)

    def test_is_full(self):
        self.assertFalse(self.default.is_full)
        small = Board((2, 2))
        for i in range(2):
            for j in range(2):
                small.set_tile((i, j), 2)
        self.assertTrue(small.is_full)

    def test_is_open(self):
        self.assertTrue(self.default.is_open((0, 0)))
        self.custom.set_tile((0, 0), 2)
        self.assertFalse(self.custom.is_open((0, 0)))

    def test_inject_random(self):
        blank = Board()
        blank.inject_random()
        blank.inject_random()
        self.assertTrue(blank.tiles.nonzero() != 0)

    def test_shift(self):
        pass

    def test_merge(self):
        pass
