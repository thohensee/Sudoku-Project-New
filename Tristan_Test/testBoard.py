from testSudokuGenerator import *
from testSudokuGenerator import shuffle
import pygame
class Board:

    testBoard = [[0, 3, 4, 6, 7, 8, 9, 1, 2],
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

        #self._board = [[nums[pattern(r, c)] for c in cols] for r in rows]
        self._board = Board.testBoard

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

    #Check if puzzle is solved
    def isCorrect(self):
        #Checks each horizontal row's validity

        board = self.get_board()

        for i in range(9):
            intList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in range(9):
                if board[i][j] == 0:
                    return False
                elif board[i][j] in intList:
                    loc = intList.index(board[i][j])
                    intList = intList[:loc] + intList[loc + 1:]
            if len(intList) != 0:
                return False

        #Checks each vertical row's validity
        for j in range(9):
            intList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for i in range(9):
                if board[i][j] == 0:
                    return False
                elif board[i][j] in intList:
                    loc = intList.index(board[i][j])
                    intList = intList[:loc] + intList[loc + 1:]
            if len(intList) != 0:
                return False

        #Checks each 3x3 box's validity
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                intList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for ii in range(i, i + 3):
                    for jj in range(j, j + 3):
                        if board[ii][jj] in intList:
                            loc = intList.index(board[ii][jj])
                            intList = intList[:loc] + intList[loc + 1:]
                if len(intList) != 0:
                    return False

        return True

    def isFull(self):
        board = self.get_board()

        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return False
        return True