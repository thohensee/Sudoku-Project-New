import pygame, sys
from kevin_testing import get_font

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
        if 1 <= value <=9:
            self.sketched_value = value

    def draw(self):
        CELL_SIZE = self.screen.get_width() // 9
        cell_rect = pygame.Rect(self.col * CELL_SIZE, self.row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self.screen, (255, 0, 0) if self.selected else (0, 0, 0), cell_rect, 3)
        if self.value != 0:
            font = get_font(30)
            text_surface = font.render(str(self.value), True, (0,0,0))
            text_rect = text_surface.get_rect(center=cell_rect.center)
            self.screen.blit(text_surface, text_rect)
        elif self.sketched_value is not None:
            font = get_font(30)
            text_surface = font.render(str(self.sketched_value), True, (128, 128, 128))
            text_rect = text_surface.get_rect(center=cell_rect.center)
            self.screen.blit(text_surface, text_rect)