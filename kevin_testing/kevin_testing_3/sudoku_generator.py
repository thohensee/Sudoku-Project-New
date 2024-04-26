import random

class SudokuGenerator:
    def __init__(self, row_length=9, removed_cells=40):
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]
        self.removed_cells = removed_cells

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(row)

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        return num not in [self.board[row][col] for row in range(len(self.board))]

    def valid_in_box(self, row_start, col_start, num):
        box_values = [self.board[row][col] for row in range(row_start, row_start + 3) for col in range(col_start, col_start + 3)]
        return num not in box_values

    def is_valid(self, row, col, num):
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row - row % 3, col - col % 3, num)

    def fill_box(self, row_start, col_start):
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                self.board[row][col] = numbers.pop()

    def fill_diagonal(self):
        for i in range(0, 9, 3):
            self.fill_box(i, i)

    def fill_remaining(self, row, col):
        if col >= 9 and row < 8:
            row += 1
            col = 0
        if row >= 9 and col >= 9:
            return True
        if row < 3:
            if col < 3:
                col = 3
        elif row < 6:
            if col == int(row / 3) * 3:
                col += 3
        else:
            if col == 6:
                row += 1
                col = 0
            if row == 9:
                return True
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, 3)

    def remove_cells(self):
        cells_removed = 0
        while cells_removed < self.removed_cells:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                cells_removed += 1

def generate_sudoku(size=9, removed=40):
    sudoku_gen = SudokuGenerator(size, removed)
    sudoku_gen.fill_values()
    sudoku_gen.remove_cells()
    return sudoku_gen.get_board()
