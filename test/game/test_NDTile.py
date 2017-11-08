from unittest import TestCase
from game.ndtile import NDTile

class TestNDTile(TestCase):

    def test_NDTile(self):
        tiles = NDTile((4, 4))
        print (tiles[3, 3])
        self.fail()
