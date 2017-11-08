from game.board import Board

class Logic():

    def __init__(self, b):
        """
        :param b:
        """
        self._board = b

    def is_over(self):
        """
        Determines whether a game is over or not
        :return:
        """
        return self._board.is_full()

    def start_game(self, n):
        """
        :param n:
        :return:
        """
        pass

    def game_loop(self):
        """
        :return:
        """
        pass