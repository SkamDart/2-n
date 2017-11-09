import sys
import tty
import termios
from game.board import Board
import numpy as np


class Engine:

    def __init__(self, b, _n):
        """

        Args:
            b:
        """
        self._board = b
        self._end_score = _n
        self._tiles = b.tiles

    @property
    def board(self):
        """

        Returns:

        """
        return self._board

    @property
    def tiles(self):
        """

        Returns:

        """
        return self._tiles

    @property
    def end_score(self):
        """

        Returns:

        """
        return self._end_score

    def is_over(self):
        """Determines if game is over

        Returns:

        """
        return self._board.is_full()

    @staticmethod
    def is_valid_score(m):
        """

        Args:
            m:

        Returns:

        """
        return m

    def print_board(self):
        """ Removes none score components from board
        Returns:
        """
        for i in range(len(self._tiles)):
            for j in range(len(self._tiles[0])):
                print(self._tiles[i, j][0], end=' ')
            print('\n')

    def get_move(self):
        """

        Returns:

        """

    def start_game(self):
        """Game loop

        Args:
            n:
        """
        self.board.inject_random()
        self.board.inject_random()
        while self.is_over() is not True:
            self.print_board()
            move = input('Enter Move')



if __name__ == '__main__':
    shape = (4, 4)
    n = 2048
    board = Board(shape)
    engine = Engine(board, n)
    engine.start_game()
