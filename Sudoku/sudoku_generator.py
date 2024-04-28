import random

class SudokuGenerator: # Constructor
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]
        self.fill_values()
        self.remove_cells()

    def get_board(self):
        return self.board

    def print_board(self): # Displays the board to console
        for row in self.board:
            print(row)

    def valid_in_row(self, row, num): # Determines if num is contained in given row
        return num not in self.board[row]

    def valid_in_col(self, col, num): # Determines if num is contained in given column
        return num not in [row[col] for row in self.board]

    def valid_in_box(self, row_start, col_start, num): # Determines if num is within 3x3 box
        box = [self.board[i][j] for i in range(row_start, row_start + 3) for j in range(col_start, col_start + 3)]
        return num not in box

    def is_valid(self, row, col, num): # Determines validity of desired num placement
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row - row % 3, col - col % 3, num)

    def fill_box(self, row_start, col_start): # Randomly fills 3x3 box while ensuring no repeating numbers
        nums = [n for n in range(1, 10)]
        random.shuffle(nums)
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                self.board[i][j] = nums.pop()

    def fill_diagonal(self): # Fills the three diagonal boxes
        for i in range(0, self.row_length, 3):
            self.fill_box(i, i)

    def fill_remaining(self, row, col): # Returns solution
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < 3:
            if col < 3:
                col = 3
        elif row < self.row_length - 3:
            if col == (row // 3) * 3:
                col += 3
        else:
            if col == self.row_length - 3:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self): # Constructs solution via calling fill diagonal and fill remaining
        self.fill_diagonal()
        self.fill_remaining(0, 3)

    def remove_cells(self): # Removes desired number of cells from board
        cells_to_remove = self.removed_cells
        while cells_to_remove > 0:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                cells_to_remove -= 1

def generate_sudoku(size, removed): # Generates sudoku with given size and number of removed cells
    sudoku = SudokuGenerator(size, removed)
    return sudoku.get_board()
