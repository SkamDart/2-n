from src.game.board import Board
from src.game.move import Move
from src.game.AI import AI, Player


class Engine:

    def __init__(self, b, _n, p):
        """

        Args:
            b:
        """
        self._board = b
        self._end_score = _n
        self._player = p

    @property
    def board(self):
        """

        Returns:

        """
        return self._board

    @property
    def player(self):
        return self._player

    @staticmethod
    def is_valid_score(m):
        """

        Args:
            m:

        Returns:

        """
        return m != 0 and (m & (m - 1) == 0)

    def is_over(self):
        """

        Returns:

        """
        return self.board.is_full

    def start_game(self):
        """Game loop

        Args:
        """
        self.board.inject_random()

        while True:
            self.board.inject_random()
            self.board.print()

            if self.is_over():
                break

            # move = input('\n')
            move = self.get_move()
            self.handle_move(move)

        print('Game Over!')

    def get_move(self):
        if self.player == Player.EASY:
            return AI.random_uniform()
        elif self.player == Player.HARD:
            return AI.next_move(self.board)
        elif self.player == Player.USER:
            return input('\n')

    def handle_move(self, move):
        """

        Args:
            move:

        Returns:

        """
        move_type = None
        while True:
            move_type = Engine.parse_move(move)
            if move_type is not None:
                break
            move = input('Invalid Input\n')
        self.board.shift(move_type)

    @classmethod
    def parse_move(cls, move):
        """

        Args:
            move:

        Returns:

        """
        if move == 'h':
            return Move.LEFT
        elif move == 'j':
            return Move.DOWN
        elif move == 'k':
            return Move.UP
        elif move == 'l':
            return Move.RIGHT
        elif move == Move.UP or Move.DOWN or Move.RIGHT or Move.LEFT:
            return move
        else:
            return None


if __name__ == '__main__':
    shape = (4, 4)
    n = 2048
    board = Board(shape)
    engine = Engine(board, n, Player.HARD)
    engine.start_game()
