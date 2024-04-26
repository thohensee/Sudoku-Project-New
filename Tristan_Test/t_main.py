import pygame
import sys
from pygame.locals import *
from t_SudokuGenerator import *  # Import shuffle function from t_SudokuGenerator
from t_Board import Board

# Pygame initialization
pygame.init()

# Initialize the screen
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku")

running = True
selected_row = None
selected_col = None

# Sudoku generating code
base = 3
side = 9

board = Board(base, side)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            selected_row = mouse_pos[1] // CELL_SIZE
            selected_col = mouse_pos[0] // CELL_SIZE
        elif event.type == KEYDOWN:
            nonChange = board.get_nonChange()
            if board.get_board()[selected_row][selected_col] == 0:
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

    draw_board(screen, board)