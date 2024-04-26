import pygame
from button import Button
from cell import Cell
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell(0, row, col, self.screen) for col in range(9)] for row in range(9)]
        self.selected_cell = None

    def draw(self):
        CELL_SIZE = self.width // 9
        for row in range(9):
            for col in range(9):
                self.cells[row][col].draw(CELL_SIZE)

    def select(self, row, col):
        if self.selected_cell:
            self.selected_cell.selected = False
        self.selected_cell = self.cells[row][col]
        self.selected_cell.selected = True

    def click(self, x, y):
        cell_size = self.width // 9
        if x < self.width and y < self.height:
            row = y // cell_size
            col = x // cell_size
            return row, col
        else:
            return None

    def clear(self):
        if self.selected_cell:
            self.selected_cell.clear()

    def sketch(self, value):
        if self.selected_cell:
            self.selected_cell.set_sketched_value(value)

    def place_number(self, value):
        if self.selected_cell:
            self.selected_cell.set_cell_value(value)

    def reset_to_original(self):
        for row in self.cells:
            for cell in row:
                cell.reset()

    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True

    def update_board(self):
        for row in self.cells:
            for cell in row:
                cell.update_board()

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return row, col
        return None

    def check_board(self):
        for row in range(9):
            for col in range(9):
                if not self.is_valid(row, col, self.cells[row][col].value):
                    return False
        return True
