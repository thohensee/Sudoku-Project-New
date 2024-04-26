import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sudoku")

BG = pygame.image.load("assets/sudoku_bg.png")

def get_font(size):
    return pygame.font.Font("assets/palatinolinotype_italic.ttf", size)

def main_menu():
    while True:
        og_button = pygame.image.load("assets/button_shape.png")
        scaled_button = pygame.transform.scale(og_button, (100, 50))

        SCREEN.blit(BG, (0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("WELCOME TO SUDOKU!", True, (0, 0, 0))
        MENU_GAME_MODE = get_font(35).render("Select Game Mode:", True, (0, 0, 0))

        MENU_TEXT_RECT = MENU_TEXT.get_rect(center=(300, 75))
        MENU_GAME_MODE_RECT = MENU_GAME_MODE.get_rect(center=(300, 345))

        EASY_BUTTON = Button(image=pygame.image.load("assets/button_shape.png"), pos=(100,425),
                             text_input="EASY", font=get_font(35), base_color=(0,0,0), hovering_color="Green")
        MEDIUM_BUTTON = Button(image=pygame.image.load("assets/button_shape.png"), pos=(300,425),
                               text_input="MEDIUM", font=get_font(35), base_color=(0,0,0), hovering_color="Orange")
        HARD_BUTTON = Button(image=pygame.image.load("assets/button_shape.png"), pos=(500, 425),
                             text_input="HARD", font=get_font(35), base_color=(0,0,0), hovering_color="Red")
        EXIT_BUTTON = Button(image=scaled_button, pos=(300, 550),
                               text_input="EXIT", font=get_font(30), base_color=(0, 0, 0), hovering_color="Red")

        for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON, EXIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        SCREEN.blit(MENU_TEXT, MENU_TEXT_RECT)
        SCREEN.blit(MENU_GAME_MODE, MENU_GAME_MODE_RECT)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkInput(MENU_MOUSE_POS):
                    win()
                if MEDIUM_BUTTON.checkInput(MENU_MOUSE_POS):
                    in_game()
                if HARD_BUTTON.checkInput(MENU_MOUSE_POS):
                    lose()
                if EXIT_BUTTON.checkInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def in_game():
    while True:
        IG_MOUSE_POS = pygame.mouse.get_pos()

        og_button = pygame.image.load("assets/button_shape.png")

        SCREEN.fill("white")

        scaled_button = pygame.transform.scale(og_button,(100, 50))

        IG_RESTART = Button(image=scaled_button, pos=(300,560),
                            text_input="Restart", font=get_font(30), base_color=(0,0,0), hovering_color="Orange")
        IG_EXIT = Button(image=scaled_button, pos=(500,560),
                            text_input="Exit", font=get_font(30), base_color=(0,0,0), hovering_color="Red")
        IG_RESET = Button(image=scaled_button, pos=(100, 560),
                         text_input="Reset", font=get_font(30), base_color=(0, 0, 0), hovering_color="Green")

        for button in [IG_RESTART, IG_EXIT, IG_RESET]:
            button.changeColor(IG_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if IG_RESTART.checkInput(IG_MOUSE_POS):
                    main_menu()
                if IG_EXIT.checkInput(IG_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if IG_RESET.checkInput(IG_MOUSE_POS):
                    pass

        pygame.display.update()

def win():
    while True:
        WIN_MOUSE_POS =  pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(BG, (0,0))

        WIN_TEXT = get_font(50).render("Game Won!", True, (0,0,0))
        WIN_RECT = WIN_TEXT.get_rect(center=(300,100))

        WIN_EXIT = Button(image=pygame.image.load("assets/button_shape.png"), pos=(180,450),
                          text_input="EXIT", font=get_font(35), base_color=(0,0,0), hovering_color="Red")
        WIN_RESTART = Button(image=pygame.image.load("assets/button_shape.png"), pos=(420,450),
                          text_input="RESTART", font=get_font(35), base_color=(0,0,0), hovering_color="Green")

        for button in [WIN_EXIT, WIN_RESTART]:
            button.changeColor(WIN_MOUSE_POS)
            button.update(SCREEN)

        SCREEN.blit(WIN_TEXT, WIN_RECT)

        image = pygame.image.load("assets/win_emoji.png")
        scaled_image = pygame.transform.scale(image,(300,300))
        SCREEN.blit(scaled_image, (157,120))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIN_EXIT.checkInput(WIN_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if WIN_RESTART.checkInput(WIN_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def lose():
    while True:
        LOSE_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(BG, (0,0))

        LOSE_TEXT = get_font(50).render("Game over :(", True, (0,0,0))
        LOSE_RECT = LOSE_TEXT.get_rect(center=(300,100))

        LOSE_RESTART = Button(image=pygame.image.load("assets/button_shape.png"), pos=(180,450),
                              text_input="RESTART", font=get_font(35), base_color=(0,0,0), hovering_color="Green")
        LOSE_EXIT = Button(image=pygame.image.load("assets/button_shape.png"), pos=(420,450),
                           text_input="EXIT", font=get_font(35), base_color=(0,0,0), hovering_color="Red")

        for button in [LOSE_RESTART, LOSE_EXIT]:
            button.changeColor(LOSE_MOUSE_POS)
            button.update(SCREEN)

        SCREEN.blit(LOSE_TEXT, LOSE_RECT)

        image = pygame.image.load("assets/lose_emoji.png")
        scaled_image = pygame.transform.scale(image, (300, 300))
        SCREEN.blit(scaled_image, (157, 120))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LOSE_RESTART.checkInput(LOSE_MOUSE_POS):
                    main_menu()
                if LOSE_EXIT.checkInput(LOSE_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main_menu()
