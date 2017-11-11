from game.board import Board
from game.move import Move


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

    @staticmethod
    def is_valid_score(m):
        """

        Args:
            m:

        Returns:

        """
        return m

    def start_game(self):
        """Game loop

        Args:
        """
        self.board.tiles.inject_random()

        while True:
            self.board.tiles.inject_random()
            self.board.print()

            if self.board.is_over:
                break

            move = input('\n')
            self.handle_move(move)

        print('Game Over!')

    def handle_move(self, move):
        """

        Args:
            move:

        Returns:

        """
        move_type = self.parse_move(move)
        self.board.shift(move_type)

    def parse_move(self, move):
        """

        Args:
            move:

        Returns:

        """
        if move == 'h':
            return  Move.LEFT
        elif move == 'j':
            return Move.DOWN
        elif move == 'k':
            return Move.UP
        elif move == 'l':
            return Move.RIGHT
        else:
            return self.parse_move(input('Try Again\n'))


if __name__ == '__main__':
    shape = (5, 5)
    n = 2048
    board = Board(n, shape)
    engine = Engine(board, n)
    engine.start_game()
