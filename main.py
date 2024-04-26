

# Current issues:
# no win screen
# overwriting generated squares is possible (it shouldn't be) (DONE)
# A lot of this stuff will have to be sorted into classes, but we can do that at the end
# Required sorting: SudokuGenerator, innit, get_board, print_board, valid_in_row, valid_in_col, valid_in_box, is_valid, fill_box, fill_diagonal, fill_remaining(self, row, col), fill_values, remove_cells,
# This one is outside the SudokuGenerator class- generate_sudoku(size, removed)
# Make different difficulties: easy= 30 empty cells, medium = 40 empty cells, hard = 50 empty cells
# Might need a function to solve the board (DONE)



import pygame
import sys
from pygame.locals import *

# Sudoku generating code
base  = 3
side  = base*base


def pattern(r,c): return (base*(r%base)+r//base+c)%side
#this is where the different difficulties might come in

from random import sample

def shuffle(s): return sample(s,len(s))

rBase = range(base)
rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ]
cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
nums  = shuffle(range(1,base*base+1))

board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

squares = side*side
empties = squares * 3//4
#add difficulties
for p in sample(range(squares),empties):
    board[p//side][p%side] = 0

# Pygame initialization
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Window size
WINDOW_SIZE = (400, 400)

# Cell size
CELL_SIZE = WINDOW_SIZE[0] // side

# Initialize the screen
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku")
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

running = True
selected_row = None
selected_col = None

nonChange = []
for i in range(9):
    row = []
    for i in range(9):
        row.append(0)
    nonChange.append(row)

for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            nonChange[i][j] = 1

#Check if puzzle is solved
def isCorrect(board):
    #Checks each horizontal row's validity
    for i in range(9):
        intList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            if board[i][j] == 0:
                return False
            elif board[i][j] in intList:
                loc = intList.index(board[i][j])
                intList = intList[:loc] + intList[loc + 1:]
        if len(intList) != 0:
            return False

    #Checks each vertical row's validity
    for j in range(9):
        intList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(9):
            if board[i][j] == 0:
                return False
            elif board[i][j] in intList:
                loc = intList.index(board[i][j])
                intList = intList[:loc] + intList[loc + 1:]
        if len(intList) != 0:
            return False

    #Checks each 3x3 box's validity
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            intList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for ii in range(i, i + 3):
                for jj in range(j, j + 3):
                    if board[ii][jj] in intList:
                        loc = intList.index(board[ii][jj])
                        intList = intList[:loc] + intList[loc + 1:]
            if len(intList) != 0:
                return False

    return True

testBoard = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
             [6, 7, 2, 1, 9, 5, 3, 4, 8],
             [1, 9, 8, 3, 4, 2, 5, 6, 7],
             [8, 5, 9, 7, 6, 1, 4, 2, 3],
             [4, 2, 6, 8, 5, 3, 7, 9, 1],
             [7, 1, 3, 9, 2, 4, 8, 5, 6],
             [9, 6, 1, 5, 3, 7, 2, 8, 4],
             [2, 8, 7, 4, 1, 9, 6, 3, 5],
             [3, 4, 5, 2, 8, 6, 1, 7, 9]]

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

    draw_board()
    pygame.display.update()

pygame.quit()
sys.exit()





