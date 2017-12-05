import numpy as np
import copy
from src.game.move import Move


class Player:
    EASY = 'easy'
    USER = 'user'
    HARD = 'hard'


moves = [Move.LEFT, Move.RIGHT, Move.DOWN, Move.UP]


class AI(object):

    @classmethod
    def random_uniform(cls):
        p = np.random.uniform(0, 1)
        if p <= .25:
            return 'h'
        elif p <= .50:
            return 'j'
        elif p <= .75:
            return 'k'
        else:
            return 'l'

    @classmethod
    def random_normal(cls):
        p = np.random.randn()
        if p <= .25:
            return 'h'
        elif p <= .50:
            return 'j'
        elif p <= .75:
            return 'k'
        else:
            return 'l'

    @staticmethod
    def next_move(board, recursion_depth=3):
        """
        Wrapper for smart ai next move
        Args:
            board:
            recursion_depth:

        Returns:

        """
        return AI.next_move_helper(board, recursion_depth, recursion_depth)[0]

    @staticmethod
    def next_move_helper(board, depth, max_depth, base=0.9):
        """

        Args:
            board:
            depth:
            max_depth:
            base:

        Returns:

        """
        best_score = -1.
        best_move = 0

        for m in moves:
            new_board = copy.deepcopy(board)
            new_board.shift(m)
            score, critical = AI.evaluate_best_move(new_board)
            new_board.setCell(critical[0], critical[1], 2)

            if depth != 0:
                my_m, my_s = AI.next_move_helper(new_board, depth - 1, max_depth)
                score += my_s * pow(base, max_depth - depth + 1)

            if score > best_score:
                best_move = m
                best_score = score

        return best_move, best_score

    @staticmethod
    def eval_linear_weight(board, common_ratio):
        linear_weighted_val = 0
        weight = 1.
        critical_tile = (-1, -1)
        invert = False
        n = board.tiles.shape[0]
        tiles = board.tiles

        for y in range(n):
            for x in range(n):
                b_x = x
                b_y = y

                if invert:
                    b_x = n - 1 - x

                curr_val = tiles[(b_x, b_y)]

                if curr_val == 0 and critical_tile == (-1, -1):
                    critical_tile = (b_x, b_y)

                linear_weighted_val += curr_val * weight
                weight *= common_ratio

            invert = not invert

        return linear_weighted_val, critical_tile

    @staticmethod
    def evaluate_best_move(board, common_ratio=0.25):
        """
        calculates best move for a board
        Args:
            board:
            common_ratio:

        Returns:

        """
        linear_weighted_values = np.zeros(8)
        critical_tiles = []

        for i in range(8):
            weight_val, tile = AI.eval_linear_weight(board, common_ratio)
            linear_weighted_values[i] = weight_val
            critical_tiles.append(tile)

        critical_tiles = np.array(critical_tiles)
        max_arg = np.argmax(linear_weighted_values)
        return linear_weighted_values[max_arg], critical_tiles[max_arg]
