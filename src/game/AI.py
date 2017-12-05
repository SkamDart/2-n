import numpy as np


class Player:
    EASY = 'easy'
    USER = 'user'
    HARD = 'hard'


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

class SmartAI(object):

    def __init__(self):
        self.range4 = np.arange(4)

    def rotateRight(self, grid):
        return [[grid[r][3 - c] for r in self.range4] for c in self.range4]

    def move_row(self, row):
        out = [x for x in row if x]
        ic = oc = 0
        while out[ic:]:
            if out[ic + 1:] and out[ic] == out[ic + 1]:
                out[oc] = 2 * out[ic]
                ic += 1
            else:
                out[oc] = out[ic]
            ic += 1
            oc += 1
        out[oc:] = [None] * (4 - oc)
        return out

    def move(self, grid, rot):
        for i in range(rot):
            grid = self.rotateRight(grid)
        out = map(self.move_row, grid)
        return out, out != grid

    def eval_monotone_L(self, grid):
        L = 0
        for x in self.range4:
            m = 0
            for y in range(3):
                A = grid[x][y] or 0
                B = grid[x][y + 1] or 0
                if A and A >= B:
                    m += 1
                    L += m ** 2 * 4
                else:
                    L -= abs(A - B) * 1.5
                    m = 0
        return L

    def eval_monotone_LR(self, grid):
        return np.max(self.eval_monotone_L(grid),
                      self.eval_monotone_L(self.rotateRight(self.rotateRight(grid))))

    def eval_smoothness(self, grid):
        return -np.sum(np.min(
            [1e8] + [abs((grid[x][y] or 2) - (grid[x + a][y + b] or 2)) for a, b in ((-1, 0), (0, -1), (1, 0), (0, 1))
                     if 0 <= x + a < 4 and 0 <= y + b < 4]) for x in range4 for y in range4)

    def count_free(grid):
        return sum(r.count(None) for r in grid)

    def EVAL(self, grid):
        return self.eval_monotone_LR(grid) \
               + self.eval_monotone_LR(rotateRight(grid)) \
               + self.val_smoothness(grid) \
               - (16 - self.count_free(grid)) ** 2

    def search_max(self, grid):
        return max([self.EVAL(self.move(grid, m)[0]) for m in self.range4 if self.move(grid, m)[1]] + [-1e8])

    def search_min(grid):
        scores = []
        for i in range4:
            row = grid[i]
            for j in range4:
                if not row[j]:
                    score = all_p = 0
                    for v, p in ((2, 9.), (4, 1)):
                        if count_free(grid) <= 4 or p > 1:  # XXX hardcode for level=2
                            row[j] = v
                            score += p * search_max(grid)
                            all_p += p
                    row[j] = None

                    scores.append(score / all_p)

        return sum(scores) / len(scores)

