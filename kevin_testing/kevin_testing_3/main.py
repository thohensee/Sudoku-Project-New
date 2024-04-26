import pygame
import sys
from button import Button
from board import Board
from sudoku_generator import generate_sudoku

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

        image = pygame.image.load("assets/sudoku_image.png")
        scaled_image = pygame.transform.scale(image, (200, 200))
        SCREEN.blit(scaled_image, (215, 105))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkInput(MENU_MOUSE_POS):
                    game_loop("EASY")
                if MEDIUM_BUTTON.checkInput(MENU_MOUSE_POS):
                    game_loop("MEDIUM")
                if HARD_BUTTON.checkInput(MENU_MOUSE_POS):
                    game_loop("HARD")
                if EXIT_BUTTON.checkInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def game_loop(difficulty):
    sudoku_board = Board(600, 600, SCREEN, difficulty)
    sudoku_gen = generate_sudoku()
    for row in range(9):
        for col in range(9):
            value = sudoku_gen[row][col]
            sudoku_board.cells[row][col].set_cell_value(value)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                cell_pos = sudoku_board.click(mouse_pos[0], mouse_pos[1])
                if cell_pos:
                    sudoku_board.select(cell_pos[0], cell_pos[1])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if sudoku_board.selected_cell:
                        sudoku_board.update_board()
                        if sudoku_board.is_full() and sudoku_board.check_board():
                            win()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    sudoku_board.clear()
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                    num = int(pygame.key.name(event.key))
                    sudoku_board.place_number(num)
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                    num = int(pygame.key.name(event.key))
                    sudoku_board.sketch(num)

        SCREEN.fill("white")
        sudoku_board.draw()
        pygame.display.update()

def win():
    while True:
        WIN_MOUSE_POS = pygame.mouse.get_pos()

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

if __name__ == "__main__":
    main_menu()
