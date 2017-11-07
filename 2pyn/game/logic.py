
class Game():

    def __init__(self, b):
        """
        :param b:
        """
        self.board = b

    def isOver(self):
        """
        Determines whether a game is over or not
        :return:
        """
        return self.board.isFull()