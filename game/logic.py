from game.board import Board

class Logic():

    def __init__(self, b):
        """

        Args:
            b:
        """
        self._board = b

    def is_over(self):
        """

        Returns:

        """
        return self._board.is_full()

    def start_game(self, n):
        """

        Args:
            n:
        """
        pass

    def game_loop(self):
        """

        """
        pass