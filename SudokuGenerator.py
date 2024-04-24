class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board =
        self.box_length = float(self.row_length) ** 0.5
    def get_board(self):


    def print_board(self):


    def valid_in_row(self, row, num):


    def valid_in_col(self, col, num):


    def valid_in_box(self,row_start, col_start, num):


    def is_valid(self, row, col, num):


    def fill_box(self, row_start, col_start):


    def fill_diagonal(self):


    def fill_remaining(self, row, col):


    def fill_values(self):


    def remove_cells(self):


def generate_sudoku(size, removed):
