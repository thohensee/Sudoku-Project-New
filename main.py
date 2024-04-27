from pygame.locals import *
from SudokuGenerator import *  # Import shuffle function from t_SudokuGenerator
from Board import Board

class Main:
    @staticmethod
    def game(board):
        # Sudoku generating code
        running = True
        base = 3
        side = 9

        # Colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        # Window size
        WINDOW_SIZE = (400, 400)

        # Cell size
        CELL_SIZE = WINDOW_SIZE[0] // side

        # Pygame initialization
        pygame.init()




        #medium is squares * 1//2, easy is squares * 1//2.7, hard is squares * 2//3.2 .
        squares = side*side
        empties = squares * 1//2
        #empties = 2
        #add difficulties
        for p in sample(range(squares), empties):
            board.set_board(p//side, p % side, 0)

        # Separate changeable cells from non-changeable cells
        nonChange = board.nonChange()

        # Initialize the screen
        screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Sudoku")

        selected_row = None
        selected_col = None

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    selected_row = mouse_pos[1] // CELL_SIZE
                    selected_col = mouse_pos[0] // CELL_SIZE
                elif event.type == KEYDOWN:
                    if nonChange[selected_row][selected_col] == 0:
                        if event.key == K_1 or event.key == K_KP1:
                            if selected_row is not None and selected_col is not None:
                                board.get_board()[selected_row][selected_col] = 1
                        elif event.key == K_2 or event.key == K_KP2:
                            if selected_row is not None and selected_col is not None:
                                board.get_board()[selected_row][selected_col] = 2
                        elif event.key == K_3 or event.key == K_KP3:
                            if selected_row is not None and selected_col is not None:
                                board.get_board()[selected_row][selected_col] = 3
                        elif event.key == K_4 or event.key == K_KP4:
                            if selected_row is not None and selected_col is not None:
                                board.get_board()[selected_row][selected_col] = 4
                        elif event.key == K_5 or event.key == K_KP5:
                            if selected_row is not None and selected_col is not None:
                                board.get_board()[selected_row][selected_col] = 5
                        elif event.key == K_6 or event.key == K_KP6:
                            if selected_row is not None and selected_col is not None:
                                board.get_board()[selected_row][selected_col] = 6
                        elif event.key == K_7 or event.key == K_KP7:
                            if selected_row is not None and selected_col is not None:
                                board.get_board()[selected_row][selected_col] = 7
                        elif event.key == K_8 or event.key == K_KP8:
                            if selected_row is not None and selected_col is not None:
                                board.get_board()[selected_row][selected_col] = 8
                        elif event.key == K_9 or event.key == K_KP9:
                            if selected_row is not None and selected_col is not None:
                                board.get_board()[selected_row][selected_col] = 9
            draw_board(screen, board, nonChange)
            pygame.display.flip()

            if board.isFull():
                if board.isCorrect():
                    print('you win')
                    running = False
                    board = Board(3, 9)
                    Main.game(board)
                else:
                    print("YOU SUCK")



if __name__ == '__main__':
    board = Board(3, 9)
    Main.game(board)