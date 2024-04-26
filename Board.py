from SudokuGenerator import *
from SudokuGenerator import shuffle
import pygame
class Board:

    testBoard = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                 [6, 7, 2, 1, 9, 5, 3, 4, 8],
                 [1, 9, 8, 3, 4, 2, 5, 6, 7],
                 [8, 5, 9, 7, 6, 1, 4, 2, 3],
                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
                 [9, 6, 1, 5, 3, 7, 2, 8, 4],
                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
                 [3, 4, 5, 2, 8, 6, 1, 7, 0]]
    def __init__(self, base, side):
        self.nonChange = []

        rBase = range(base)
        rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
        cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
        nums = shuffle(range(1, base * base + 1))

        self._board = [[nums[pattern(r, c)] for c in cols] for r in rows]
        #self._board = Board.testBoard

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

    def set_board(self, i, j, val):
        self._board[i][j] = val
