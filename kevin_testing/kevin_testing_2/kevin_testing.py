import pygame, sys
from constants_k import *
import button

pygame.init()

# Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

# Variables
game_paused = False

# Load Buttons
resume_img = pygame.image.load("images/resume_button.png").convert_alpha()

# Display Buttons
resume_button = button.Button(275, 275, resume_img, 1)

# Fonts
font = pygame.font.SysFont("gabriola",40)

def display_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

# Game Loop
run = True
while run:

    screen.fill((200, 255, 200))

    # Checks if Game is Paused
    if game_paused == True:
        if resume_button.draw(screen):
            game_paused = False
    else:
        display_text("Welcome to Sudoku!", font, BLACK, (WIDTH//3.175), 275)

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()