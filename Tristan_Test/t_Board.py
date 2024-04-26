class Board:

    def __init__(self, board):
        self.nonChange = []
        for i in range(9):
            row = []
            for i in range(9):
                row.append(0)
            self.nonChange.append(row)

        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    self.nonChange[i][j] = 1

    def get_nonChange(self):
        return self.nonChange