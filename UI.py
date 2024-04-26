# Imports pygame and Button class
import pygame, sys
from button import Button

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

# Function for displaying buttons when in game
def in_game():
    while True:
        IG_MOUSE_POS = pygame.mouse.get_pos() # Tracks mouse only when in game

        og_button = pygame.image.load("assets/button_shape.png") # Loads original button

        SCREEN.fill("white") # Sets the background as white

        scaled_button = pygame.transform.scale(og_button,(100, 50)) # Scales button images down so they don't take up too much space

        IG_RESTART = Button(image=scaled_button, pos=(300,560),
                            text_input="Restart", font=get_font(30), base_color=(0,0,0), hovering_color="Orange") # Button for restarting
        IG_EXIT = Button(image=scaled_button, pos=(500,560),
                            text_input="Exit", font=get_font(30), base_color=(0,0,0), hovering_color="Red") # Button for exiting program
        IG_RESET = Button(image=scaled_button, pos=(100, 560),
                         text_input="Reset", font=get_font(30), base_color=(0, 0, 0), hovering_color="Green") # Button for resetting sudoku board

        for button in [IG_RESTART, IG_EXIT, IG_RESET]:
            button.changeColor(IG_MOUSE_POS) # Makes the buttons' text change color when hovered over by mouse
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # Checks if button is pressed
                if IG_RESTART.checkInput(IG_MOUSE_POS): # If restart button is pressed, user is taken back to main menu
                    main_menu()
                if IG_EXIT.checkInput(IG_MOUSE_POS): # If exit button is pressed, the program is closed
                    pygame.quit()
                    sys.exit()
                if IG_RESET.checkInput(IG_MOUSE_POS): # If reset button is pressed, the sudoku board is reset to its initial state
                    pass

        pygame.display.update() # Refreshes display


if __name__ == "__main__":
    main_menu()
