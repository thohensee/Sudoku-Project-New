import random

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]
        self.fill_values()
        self.remove_cells()

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(row)

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        return num not in [row[col] for row in self.board]

    def valid_in_box(self, row_start, col_start, num):
        box = [self.board[i][j] for i in range(row_start, row_start + 3) for j in range(col_start, col_start + 3)]
        return num not in box

    def is_valid(self, row, col, num):
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row - row % 3, col - col % 3, num)

    def fill_box(self, row_start, col_start):
        nums = [n for n in range(1, 10)]
        random.shuffle(nums)
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                self.board[i][j] = nums.pop()

    def fill_diagonal(self):
        for i in range(0, self.row_length, 3):
            self.fill_box(i, i)

    def fill_remaining(self, row, col):
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

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, 3)

    def remove_cells(self):
        cells_to_remove = self.removed_cells
        while cells_to_remove > 0:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                cells_to_remove -= 1

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    return sudoku.get_board()

# Example usage:
if __name__ == "__main__":
    sudoku_board = generate_sudoku(9, 40)  # Generate a 9x9 Sudoku with 40 cells removed
    print("Generated Sudoku Board:")
    for row in sudoku_board:
        print(row)
