# Imports pygame and Button class
import pygame, sys
from button import Button
from SudokuGenerator import SudokuGenerator

# Initializes pygame modules
pygame.init()

# Sets display size to 600x600
SCREEN = pygame.display.set_mode((540, 600))
FPS = 30
clock = pygame.time.Clock()
selected = (0, 0)
pygame.display.set_caption("Sudoku") # Captions the window as "Sudoku"

# Loads menu background
BG = pygame.image.load("assets/sudoku_bg.png")

# Gets font from assets folder allowing it to be utilized when displaying text
def get_font(size):
    return pygame.font.Font("assets/palatinolinotype_italic.ttf", size)

# Function for the main menu
def main_menu():
    while True:
        og_button = pygame.image.load("assets/button_shape.png") # Initializes button to then be scaled down
        scaled_button = pygame.transform.scale(og_button, (100, 50))

        SCREEN.blit(BG, (0,0)) # Displays the background for the main menu

        MENU_MOUSE_POS = pygame.mouse.get_pos() # Tracks the mouse specifically on the main menu

        MENU_TEXT = get_font(45).render("WELCOME TO SUDOKU!", True, (0, 0, 0)) # Initializes and displays text welcoming user
        MENU_GAME_MODE = get_font(35).render("Select Game Mode:", True, (0, 0, 0)) # Initializes and displays text prompting for user to select difficulty

        MENU_TEXT_RECT = MENU_TEXT.get_rect(center=(270, 75)) # Positions above text where desired
        MENU_GAME_MODE_RECT = MENU_GAME_MODE.get_rect(center=(270, 345)) # Positions above text where desired

        EASY_BUTTON = Button(image=pygame.image.load("assets/button_shape.png"), pos=(90, 425),
                             text_input="EASY", font=get_font(35), base_color=(0,0,0), hovering_color="Green") # Button for selecting easy difficulty
        MEDIUM_BUTTON = Button(image=pygame.image.load("assets/button_shape.png"), pos=(270, 425),
                               text_input="MEDIUM", font=get_font(35), base_color=(0,0,0), hovering_color="Orange") # Button for selecting medium difficulty
        HARD_BUTTON = Button(image=pygame.image.load("assets/button_shape.png"), pos=(450, 425),
                             text_input="HARD", font=get_font(35), base_color=(0,0,0), hovering_color="Red") # Button for selecting hard difficulty
        EXIT_BUTTON = Button(image=scaled_button, pos=(270, 550),
                               text_input="EXIT", font=get_font(30), base_color=(0, 0, 0), hovering_color="Red") # Button for exiting the game

        for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON, EXIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS) # Makes the buttons' text change color when hovered over by mouse
            button.update(SCREEN)

        SCREEN.blit(MENU_TEXT, MENU_TEXT_RECT) # Displays m and centers enu text
        SCREEN.blit(MENU_GAME_MODE, MENU_GAME_MODE_RECT) # Centers and displays menu text

        image = pygame.image.load("assets/sudoku_image.png") # Displays sudoku icon in middle of screen
        scaled_image = pygame.transform.scale(image, (200, 200)) # Scales image down because original is too large
        SCREEN.blit(scaled_image, (195, 105)) # Places the scaled icon in the center

        pygame.display.flip() # Updates the window

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # Checks if button is pressed
                if EASY_BUTTON.checkInput(MENU_MOUSE_POS): # Takes user to easy difficulty when selected
                    in_game()
                if MEDIUM_BUTTON.checkInput(MENU_MOUSE_POS): # Takes user to medium difficulty when selected
                    in_game()
                if HARD_BUTTON.checkInput(MENU_MOUSE_POS): # Takes user to hard difficulty when selected
                    in_game()
                if EXIT_BUTTON.checkInput(MENU_MOUSE_POS): # Exits the program when selected
                    pygame.quit()
                    sys.exit()

        pygame.display.update() # Refreshes display in case anything changes

# Function for winning screen
def win():
    while True:
        WIN_MOUSE_POS =  pygame.mouse.get_pos() # Tracks mouse location only on the winning screen

        SCREEN.fill("black") # Fills the screen black, hiding the previous menu
        SCREEN.blit(BG, (0,0)) # Loads and displays the background present in the main menu screen

        WIN_TEXT = get_font(50).render("Game Won!", True, (0,0,0)) # Loads the winning message
        WIN_RECT = WIN_TEXT.get_rect(center=(270,100)) # Centers the winning message

        WIN_EXIT = Button(image=pygame.image.load("assets/button_shape.png"), pos=(135, 450),
                          text_input="EXIT", font=get_font(35), base_color=(0,0,0), hovering_color="Red") # Button for exiting when on the winning screen
        WIN_RESTART = Button(image=pygame.image.load("assets/button_shape.png"), pos=(405, 450),
                             text_input="RESTART", font=get_font(35), base_color=(0,0,0), hovering_color="Green") # Button for taking user to the main menu when on the winning screen

        for button in [WIN_EXIT, WIN_RESTART]:
            button.changeColor(WIN_MOUSE_POS) # Makes the buttons' text change color when hovered over by mouse
            button.update(SCREEN)

        SCREEN.blit(WIN_TEXT, WIN_RECT) # Displays and centers text on winning screen

        image = pygame.image.load("assets/win_emoji.png") # Loads emoji for winning
        scaled_image = pygame.transform.scale(image,(300,300)) # Scales emoji for winning properly
        SCREEN.blit(scaled_image, (127,120)) # Centers and displays the emoji

        pygame.display.flip() # Updates the window

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # Checks if button is pressed
                if WIN_EXIT.checkInput(WIN_MOUSE_POS): # If exit button is selected, the program is closed
                    pygame.quit()
                    sys.exit()
                if WIN_RESTART.checkInput(WIN_MOUSE_POS): # If restart button is selected, it takes user back to main menu
                    generate_new_board()
                    main_menu()

        pygame.display.update() # Refreshes display

# Function for losing screen
def lose():
    while True:
        LOSE_MOUSE_POS = pygame.mouse.get_pos() # Tracks mouse only on the losing screen

        SCREEN.fill("black") # Fills the screen black, hiding the previous menu
        SCREEN.blit(BG, (0,0)) # Displays background present on main menu

        LOSE_TEXT = get_font(50).render("Game over :(", True, (0,0,0)) # Loads the losing message
        LOSE_RECT = LOSE_TEXT.get_rect(center=(270,100)) # Centers the losing message

        LOSE_RESTART = Button(image=pygame.image.load("assets/button_shape.png"), pos=(135, 450),
                              text_input="RESTART", font=get_font(35), base_color=(0,0,0), hovering_color="Green") # Button for restarting
        LOSE_EXIT = Button(image=pygame.image.load("assets/button_shape.png"), pos=(405, 450),
                           text_input="EXIT", font=get_font(35), base_color=(0,0,0), hovering_color="Red") # Button for exiting program

        for button in [LOSE_RESTART, LOSE_EXIT]:
            button.changeColor(LOSE_MOUSE_POS) # Makes the buttons' text change color when hovered over by mouse
            button.update(SCREEN)

        SCREEN.blit(LOSE_TEXT, LOSE_RECT) # Displays and centers the losing message

        image = pygame.image.load("assets/lose_emoji.png") # Loads emoji for losing screen
        scaled_image = pygame.transform.scale(image, (300, 300)) # Scales down the emoji due to being too large
        SCREEN.blit(scaled_image, (127, 120)) # Centers emoji for losing screen

        pygame.display.flip() # Updates the window

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # Checks if button is pressed
                if LOSE_RESTART.checkInput(LOSE_MOUSE_POS): # If restart button is pressed, the user is taken back to the main menu
                    generate_new_board()
                    main_menu()
                if LOSE_EXIT.checkInput(LOSE_MOUSE_POS): # If exit button is pressed, the program is closed
                    pygame.quit()
                    sys.exit()

        pygame.display.update() # Refreshes display

sudoku = SudokuGenerator(row_length=9, removed_cells=1)
board = sudoku.get_board()
original_board = [row[:] for row in board]  # Create a copy of the board

def draw_board():
    SCREEN.fill("white")
    for i in range(10):
        thickness = 3 if i % 3 == 0 else 1
        pygame.draw.line(SCREEN, "black", (60 * i, 0), (60 * i, 540), thickness)
        pygame.draw.line(SCREEN, "black", (0, 60 * i), (540, 60 * i), thickness)

    for row in range(9):
        for col in range(9):
            value = board[row][col]
            color = "gray" if original_board[row][col] == 0 else "black"  # Gray for user-inputted numbers
            if value != 0:
                text = get_font(40).render(str(value), True, color)
                text_rect = text.get_rect(center=(30 + 60 * col, 30 + 60 * row))
                SCREEN.blit(text, text_rect)

    pygame.draw.rect(SCREEN, "red", pygame.Rect(selected[1] * 60, selected[0] * 60, 60, 60), 3)

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
            lose()
            return
    win()

def is_valid_row(row):
    return len(set(board[row])) == 9

def is_valid_col(col):
    col_vals = [board[row][col] for row in range(9)]
    return len(set(col_vals)) == 9

def is_valid_box(row_start, col_start):
    box_vals = [board[i][j] for i in range(row_start, row_start + 3) for j in range(col_start, col_start + 3)]
    return len(set(box_vals)) == 9

def generate_new_board():
    global board, original_board
    sudoku = SudokuGenerator(row_length=9, removed_cells=1)
    board = sudoku.get_board()
    original_board = [row[:] for row in board]  # Create a copy of the board

# Function for displaying buttons when in game
def in_game():
    global selected
    while True:
        IG_MOUSE_POS = pygame.mouse.get_pos() # Tracks mouse only when in game

        og_button = pygame.image.load("assets/button_shape.png") # Loads original button

        SCREEN.fill("white") # Sets the background as white

        scaled_button = pygame.transform.scale(og_button,(100, 50)) # Scales button images down so they don't take up too much space

        IG_RESTART = Button(image=scaled_button, pos=(270,570),
                            text_input="Restart", font=get_font(30), base_color=(0,0,0), hovering_color="Orange") # Button for restarting
        IG_EXIT = Button(image=scaled_button, pos=(405,570),
                            text_input="Exit", font=get_font(30), base_color=(0,0,0), hovering_color="Red") # Button for exiting program
        IG_RESET = Button(image=scaled_button, pos=(135, 570),
                         text_input="Reset", font=get_font(30), base_color=(0, 0, 0), hovering_color="Green") # Button for resetting sudoku board

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # Checks if button is pressed
                if IG_RESTART.checkInput(IG_MOUSE_POS): # If restart button is pressed, user is taken back to main menu
                    generate_new_board()
                    main_menu()
                if IG_EXIT.checkInput(IG_MOUSE_POS): # If exit button is pressed, the program is closed
                    pygame.quit()
                    sys.exit()
                if IG_RESET.checkInput(IG_MOUSE_POS): # If reset button is pressed, the sudoku board is reset to its initial state
                    clear_user_input()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    row = mouse_pos[1] // 60
                    col = mouse_pos[0] // 60
                    selected = (min(max(row, 0), 8), min(max(col, 0), 8))
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
        for button in [IG_RESTART, IG_EXIT, IG_RESET]:
            button.changeColor(IG_MOUSE_POS) # Makes the buttons' text change color when hovered over by mouse
            button.update(SCREEN)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main_menu()
