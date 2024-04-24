
 # Lab 5B - Connect Four

def initialize_board(num_rows, num_cols):
    board = []

    for i in range(0, num_rows):
        row = []
        for j in range(0, num_cols):
            row.append("-")
        board.append(row)

    return board

def print_board(board):
    for i in range(0, len(board)):
        print(" ".join(board[i]))

def check_if_winner(board, row, col, chip_type):
    for i in range(0, row):
        hCount = 0

        for j in range(0, col):
            if board[i][j] == chip_type:
                hCount = hCount + 1
                response = "True"
            else:
                response = "False"

        if hCount == 4:
            return True

    for j in range(0, col):
        vCount = 0

        for i in range(0, row):
            if board[i][j] == chip_type:
                vCount = vCount + 1
                response = "True"
            else:
                response = "False"
            #print(f"{i}{j}{response}{vCount}")
        if vCount == 4:
            return True
    return False


def insert_chip(board, col, chip_type):
    for i in range(len(board) - 1, -1, -1):
        if board[i][col] == "-":
            board[i][col] = chip_type
            break

    return board


def main():
    height = int(input("What would you like the height of the board to be? "))
    length = int(input("What would you like the length of the board to be? "))
    maxMoves = height*length

    board = initialize_board(height, length)
    print_board(board)
    moveCount = 0

    print("\nPlayer 1: x")
    print("Player 2: o")

    player = 2

    while True:
        match player:
            case 1:
                player = 2
                piece = "o"
            case 2:
                player = 1
                piece = "x"

        match player:
            case 1:
                col = int(input("Player 1: Which column would you like to choose? "))
            case 2:
                col = int(input("Player 2: Which column would you like to choose? "))

        board = insert_chip(board, col, piece)
        print_board(board)
        moveCount = moveCount + 1

        if check_if_winner(board, height, length, piece):
            match piece:
                case "x":
                    print("Player 1 won the game!")
                case "0":
                    print("Player 2 won the game!")
            exit()

        if moveCount == maxMoves:
            print("Draw. Nobody wins.")
            exit()

if __name__ == "__main__":
     main()