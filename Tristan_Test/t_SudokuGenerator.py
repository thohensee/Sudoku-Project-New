import sys
import pygame
from t_main import *
from random import sample

# Pygame initialization
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Window size
WINDOW_SIZE = (400, 400)

# Cell size
CELL_SIZE = WINDOW_SIZE[0] // side
# Function to draw the Sudoku board
def draw_board():
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

def pattern(r, c): return (base * (r % base) + r // base + c) % side
# this is where the different difficulties might come in

def shuffle(s): return sample(s,len(s))