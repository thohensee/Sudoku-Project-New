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
        SCREEN.blit(BG, (0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("WELCOME TO SUDOKU!", True, (0, 0, 0))
        MENU_GAME_MODE = get_font(35).render("Select Game Mode:", True, (0, 0, 0))

        MENU_TEXT_RECT = MENU_TEXT.get_rect(center=(300, 75))
        MENU_GAME_MODE_RECT = MENU_GAME_MODE.get_rect(center=(300, 320))

        EASY_BUTTON = Button(image=pygame.image.load("assets/button_shape.png"), pos=(100,400),
                             text_input="EASY", font=get_font(35), base_color=(0,0,0), hovering_color="Green")
        MEDIUM_BUTTON = Button(image=pygame.image.load("assets/button_shape.png"), pos=(300,400),
                               text_input="MEDIUM", font=get_font(35), base_color=(0,0,0), hovering_color="Orange")
        HARD_BUTTON = Button(image=pygame.image.load("assets/button_shape.png"), pos=(500, 400),
                             text_input="HARD", font=get_font(35), base_color=(0,0,0), hovering_color="Red")

        for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON]:
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
                    pass
                if HARD_BUTTON.checkInput(MENU_MOUSE_POS):
                    lose()

        pygame.display.update()

def win():
    while True:
        WIN_MOUSE_POS =  pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(BG, (0,0))

        WIN_TEXT = get_font(50).render("Game Won!", True, (0,0,0))
        WIN_RECT = WIN_TEXT.get_rect(center=(300,250))

        WIN_EXIT = Button(image=pygame.image.load("assets/button_shape.png"), pos=(300,450),
                          text_input="EXIT", font=get_font(35), base_color=(0,0,0), hovering_color="Red")

        for button in [WIN_EXIT]:
            button.changeColor(WIN_MOUSE_POS)
            button.update(SCREEN)

        SCREEN.blit(WIN_TEXT, WIN_RECT)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIN_EXIT.checkInput(WIN_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

def lose():
    while True:
        LOSE_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(BG, (0,0))

        LOSE_TEXT = get_font(50).render("Game over :(", True, (0,0,0))
        LOSE_RECT = LOSE_TEXT.get_rect(center=(300,250))

        LOSE_RESTART = Button(image=pygame.image.load("assets/button_shape.png"), pos=(300,450),
                              text_input="RESTART", font=get_font(35), base_color=(0,0,0), hovering_color="Green")

        for button in [LOSE_RESTART]:
            button.changeColor(LOSE_MOUSE_POS)
            button.update(SCREEN)

        SCREEN.blit(LOSE_TEXT, LOSE_RECT)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LOSE_RESTART.checkInput(LOSE_MOUSE_POS):
                    main_menu()

if __name__ == "__main__":
    main_menu()
