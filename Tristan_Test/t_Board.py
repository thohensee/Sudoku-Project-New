from t_SudokuGenerator import *
from t_SudokuGenerator import shuffle
class Board:

    def __init__(self, base, side):
        self.nonChange = []

        rBase = range(base)
        rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
        cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
        nums = shuffle(range(1, base * base + 1))

        self._board = [[nums[pattern(r, c)] for c in cols] for r in rows]

        squares = side * side
        empties = squares * 3 // 4

        for i in range(9):
            row = []
            for i in range(9):
                row.append(0)
            self.nonChange.append(row)

        for i in range(9):
            for j in range(9):
                if self._board[i][j] != 0:
                    self.nonChange[i][j] = 1

    def get_nonChange(self):
        return self.nonChange

    def get_board(self):
        return self._board
