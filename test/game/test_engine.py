from unittest import TestCase

from src.game.board import Board
from src.game.engine import Engine

from src.game.move import Move


class TestEngine(TestCase):

    def setUp(self):
        self.default = Board()
        self.engine = Engine(self.default, 2048)

    def test_is_over(self):
        self.assertFalse(self.engine.is_over())
        for i in range(16):
            self.engine.board.inject_random()
        self.assertTrue(self.engine.is_over())

    def test_is_valid_score(self):
        self.assertTrue(self.engine.is_valid_score(2048))
        self.assertFalse(self.engine.is_valid_score(200))

    def test_start_game(self):
        pass

    def test_parse_valid_move(self):
        self.assertTrue(Move.LEFT == Engine.parse_move('h'))
        self.assertTrue(Move.RIGHT == Engine.parse_move('l'))
        self.assertTrue(Move.UP == Engine.parse_move('k'))
        self.assertTrue(Move.DOWN == Engine.parse_move('j'))

    def test_parse_invalid_move(self):
        self.assertTrue(Engine.parse_move('a') is None)
