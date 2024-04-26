base = 3
side = base * base

def pattern(r, c): return (base * (r % base) + r // base + c) % side

from random import sample

def shuffle(s): return sample(s, len(s))

rBase = range(base)
rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
nums = shuffle(range(1, base * base + 1))

def generate_board(difficulty):
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]
    squares = side * side
    empties = difficulty
    for p in sample(range(squares), empties):
        board[p // side][p % side] = 0
    return board

import pygame
import sys
from pygame.locals import *

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Window size
WINDOW_SIZE = (400, 400)

# Cell size
CELL_SIZE = WINDOW_SIZE[0] // side

# Initialize the screen
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku")

def draw_board(board):
    screen.fill(WHITE)
    for i in range(side + 1):
        if i % base == 0:
            line_thickness = 11
        else:
            line_thickness = 5
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE[1]), line_thickness)
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WINDOW_SIZE[0], i * CELL_SIZE), line_thickness)

    font = pygame.font.Font(None, 36)
    for i in range(side):
        for j in range(side):
            if board[i][j] != 0:
                text_surface = font.render(str(board[i][j]), True, BLACK)
                text_rect = text_surface.get_rect(center=(j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text_surface, text_rect)

# Difficulty levels
EASY = 30
MEDIUM = 40
HARD = 50
board = generate_board(HARD)

running = True
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
            if event.key == K_1 or event.key == K_KP1:
                if selected_row is not None and selected_col is not None:
                    board[selected_row][selected_col] = 1
            elif event.key == K_2 or event.key == K_KP2:
                if selected_row is not None and selected_col is not None:
                    board[selected_row][selected_col] = 2
            elif event.key == K_3 or event.key == K_KP3:
                if selected_row is not None and selected_col is not None:
                    board[selected_row][selected_col] = 3
            elif event.key == K_4 or event.key == K_KP4:
                if selected_row is not None and selected_col is not None:
                    board[selected_row][selected_col] = 4
            elif event.key == K_5 or event.key == K_KP5:
                if selected_row is not None and selected_col is not None:
                    board[selected_row][selected_col] = 5
            elif event.key == K_6 or event.key == K_KP6:
                if selected_row is not None and selected_col is not None:
                    board[selected_row][selected_col] = 6
            elif event.key == K_7 or event.key == K_KP7:
                if selected_row is not None and selected_col is not None:
                    board[selected_row][selected_col] = 7
            elif event.key == K_8 or event.key == K_KP8:
                if selected_row is not None and selected_col is not None:
                    board[selected_row][selected_col] = 8
            elif event.key == K_9 or event.key == K_KP9:
                if selected_row is not None and selected_col is not None:
                    board[selected_row][selected_col] = 9
    draw_board(board)
    pygame.display.update()