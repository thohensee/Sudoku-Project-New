import pygame, sys
from
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        pass

    def draw(self):
        CELL_SIZE = self.screen.get_width()//9
        cell_rect = pygame.Rect(self.col*CELL_SIZE, self.row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self.screen,(255, 0, 0) if self.selected else (0, 0, 0), cell_rect, 3)
        if self.value != 0:
