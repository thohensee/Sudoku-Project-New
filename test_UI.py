# Imports pygame and Button class
import pygame, sys
from button import Button
from test_board import Board
from SudokuGenerator import *
from pygame.locals import *

# Initializes pygame modules
pygame.init()

# Sets display size to 600x600
SCREEN = pygame.display.set_mode((600, 600))
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

        MENU_TEXT = get_font(50).render("WELCOME TO SUDOKU!", True, (0, 0, 0)) # Initializes and displays text welcoming user
        MENU_GAME_MODE = get_font(35).render("Select Game Mode:", True, (0, 0, 0)) # Initializes and displays text prompting for user to select difficulty

        MENU_TEXT_RECT = MENU_TEXT.get_rect(center=(300, 75)) # Positions above text where desired
        MENU_GAME_MODE_RECT = MENU_GAME_MODE.get_rect(center=(300, 345)) # Positions above text where desired

        EASY_BUTTON = Button(image=pygame.image.load("assets/button_shape.png"), pos=(100, 425),
                             text_input="EASY", font=get_font(35), base_color=(0,0,0), hovering_color="Green") # Button for selecting easy difficulty
        MEDIUM_BUTTON = Button(image=pygame.image.load("assets/button_shape.png"), pos=(300, 425),
                               text_input="MEDIUM", font=get_font(35), base_color=(0,0,0), hovering_color="Orange") # Button for selecting medium difficulty
        HARD_BUTTON = Button(image=pygame.image.load("assets/button_shape.png"), pos=(500, 425),
                             text_input="HARD", font=get_font(35), base_color=(0,0,0), hovering_color="Red") # Button for selecting hard difficulty
        EXIT_BUTTON = Button(image=scaled_button, pos=(300, 550),
                               text_input="EXIT", font=get_font(30), base_color=(0, 0, 0), hovering_color="Red") # Button for exiting the game

        for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON, EXIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS) # Makes the buttons' text change color when hovered over by mouse
            button.update(SCREEN)

        SCREEN.blit(MENU_TEXT, MENU_TEXT_RECT) # Displays m and centers enu text
        SCREEN.blit(MENU_GAME_MODE, MENU_GAME_MODE_RECT) # Centers and displays menu text

        image = pygame.image.load("assets/sudoku_image.png") # Displays sudoku icon in middle of screen
        scaled_image = pygame.transform.scale(image, (200, 200)) # Scales image down because original is too large
        SCREEN.blit(scaled_image, (215, 105)) # Places the scaled icon in the center

        pygame.display.flip() # Updates the window

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # Checks if button is pressed
                if EASY_BUTTON.checkInput(MENU_MOUSE_POS): # Takes user to easy difficulty when selected
                    win()
                if MEDIUM_BUTTON.checkInput(MENU_MOUSE_POS): # Takes user to medium difficulty when selected
                    in_game()
                if HARD_BUTTON.checkInput(MENU_MOUSE_POS): # Takes user to hard difficulty when selected
                    lose()
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
        WIN_RECT = WIN_TEXT.get_rect(center=(300,100)) # Centers the winning message

        WIN_EXIT = Button(image=pygame.image.load("assets/button_shape.png"), pos=(180, 450),
                          text_input="EXIT", font=get_font(35), base_color=(0,0,0), hovering_color="Red") # Button for exiting when on the winning screen
        WIN_RESTART = Button(image=pygame.image.load("assets/button_shape.png"), pos=(420, 450),
                             text_input="RESTART", font=get_font(35), base_color=(0,0,0), hovering_color="Green") # Button for taking user to the main menu when on the winning screen

        for button in [WIN_EXIT, WIN_RESTART]:
            button.changeColor(WIN_MOUSE_POS) # Makes the buttons' text change color when hovered over by mouse
            button.update(SCREEN)

        SCREEN.blit(WIN_TEXT, WIN_RECT) # Displays and centers text on winning screen

        image = pygame.image.load("assets/win_emoji.png") # Loads emoji for winning
        scaled_image = pygame.transform.scale(image,(300,300)) # Scales emoji for winning properly
        SCREEN.blit(scaled_image, (157,120)) # Centers and displays the emoji

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
                    main_menu()

        pygame.display.update() # Refreshes display

# Function for losing screen
def lose():
    while True:
        LOSE_MOUSE_POS = pygame.mouse.get_pos() # Tracks mouse only on the losing screen

        SCREEN.fill("black") # Fills the screen black, hiding the previous menu
        SCREEN.blit(BG, (0,0)) # Displays background present on main menu

        LOSE_TEXT = get_font(50).render("Game over :(", True, (0,0,0)) # Loads the losing message
        LOSE_RECT = LOSE_TEXT.get_rect(center=(300,100)) # Centers the losing message

        LOSE_RESTART = Button(image=pygame.image.load("assets/button_shape.png"), pos=(180, 450),
                              text_input="RESTART", font=get_font(35), base_color=(0,0,0), hovering_color="Green") # Button for restarting
        LOSE_EXIT = Button(image=pygame.image.load("assets/button_shape.png"), pos=(420, 450),
                           text_input="EXIT", font=get_font(35), base_color=(0,0,0), hovering_color="Red") # Button for exiting program

        for button in [LOSE_RESTART, LOSE_EXIT]:
            button.changeColor(LOSE_MOUSE_POS) # Makes the buttons' text change color when hovered over by mouse
            button.update(SCREEN)

        SCREEN.blit(LOSE_TEXT, LOSE_RECT) # Displays and centers the losing message

        image = pygame.image.load("assets/lose_emoji.png") # Loads emoji for losing screen
        scaled_image = pygame.transform.scale(image, (300, 300)) # Scales down the emoji due to being too large
        SCREEN.blit(scaled_image, (157, 120)) # Centers emoji for losing screen

        pygame.display.flip() # Updates the window

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # Checks if button is pressed
                if LOSE_RESTART.checkInput(LOSE_MOUSE_POS): # If restart button is pressed, the user is taken back to the main menu
                    main_menu()
                if LOSE_EXIT.checkInput(LOSE_MOUSE_POS): # If exit button is pressed, the program is closed
                    pygame.quit()
                    sys.exit()

        pygame.display.update() # Refreshes display

base = 3
side = 9
CELL_SIZE = 10
board = Board(base, side)
selected_row = None
selected_col = None
# Function for displaying buttons when in game
def in_game():
    while True:
        global selected_row, selected_col
        IG_MOUSE_POS = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                selected_row = IG_MOUSE_POS[1]// CELL_SIZE
                selected_col = IG_MOUSE_POS[0]// CELL_SIZE
            elif event.type == KEYDOWN:
                nonChange = board.get_nonChange()
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
        draw_board(SCREEN, board)
        pygame.display.flip()

if __name__ == "__main__":
    main_menu()
