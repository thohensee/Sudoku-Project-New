import pygame
from SudokuGenerator import SudokuGenerator

# Initialize Pygame
pygame.init()

# Constants for the game window
WIDTH, HEIGHT = 540, 600
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Create a Sudoku board
sudoku = SudokuGenerator(row_length=9, removed_cells=30)
board = sudoku.get_board()
original_board = [row[:] for row in board]  # Create a copy of the board

# Initialize Pygame window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")
clock = pygame.time.Clock()

# Font for numbers
font = pygame.font.Font(None, 40)

selected = (0, 0)  # Start with the top-left cell selected

def draw_board():
    window.fill(WHITE)
    for i in range(10):
        thickness = 3 if i % 3 == 0 else 1
        pygame.draw.line(window, BLACK, (60 * i, 0), (60 * i, 540), thickness)
        pygame.draw.line(window, BLACK, (0, 60 * i), (540, 60 * i), thickness)

    for row in range(9):
        for col in range(9):
            value = board[row][col]
            color = GRAY if original_board[row][col] == 0 else BLACK  # Gray for user-inputted numbers
            if value != 0:
                text = font.render(str(value), True, color)
                text_rect = text.get_rect(center=(30 + 60 * col, 30 + 60 * row))
                window.blit(text, text_rect)

    pygame.draw.rect(window, RED, pygame.Rect(selected[1] * 60, selected[0] * 60, 60, 60), 3)

def update_cell(row, col, num):
    # Check if the cell indices are within bounds
    if 0 <= row < 9 and 0 <= col < 9:
        if original_board[row][col] == 0:  # Check if cell is user-inputted
            board[row][col] = num
            if is_board_complete():
                check_board_validity()

def clear_user_input():
    for row in range(9):
        for col in range(9):
            if original_board[row][col] == 0:
                board[row][col] = 0

def is_board_complete():
    for row in board:
        if 0 in row:
            return False
    return True

def check_board_validity():
    # Check rows, columns, and boxes for validity
    for i in range(9):
        if not is_valid_row(i) or not is_valid_col(i) or not is_valid_box(i // 3 * 3, i % 3 * 3):
            print("Board filled incorrectly!")
            return
    print("Board filled correctly!")

def is_valid_row(row):
    return len(set(board[row])) == 9

def is_valid_col(col):
    col_vals = [board[row][col] for row in range(9)]
    return len(set(col_vals)) == 9

def is_valid_box(row_start, col_start):
    box_vals = [board[i][j] for i in range(row_start, row_start + 3) for j in range(col_start, col_start + 3)]
    return len(set(box_vals)) == 9

def main():
    global selected
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                row = mouse_pos[1] // 60
                col = mouse_pos[0] // 60
                selected = (min(max(row, 0), 8), min(max(col, 0), 8))  # Ensure selected coordinates are within bounds
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (max(selected[0] - 1, 0), selected[1])
                elif event.key == pygame.K_DOWN:
                    selected = (min(selected[0] + 1, 8), selected[1])
                elif event.key == pygame.K_LEFT:
                    selected = (selected[0], max(selected[1] - 1, 0))
                elif event.key == pygame.K_RIGHT:
                    selected = (selected[0], min(selected[1] + 1, 8))
                elif event.key == pygame.K_r:
                    clear_user_input()
                elif event.type == pygame.KEYDOWN:
                    if selected:
                        key = event.unicode
                        if key.isdigit():
                            update_cell(selected[0], selected[1], int(key))
                        elif key == '\x08':  # Backspace key
                            update_cell(selected[0], selected[1], 0)

        draw_board()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
