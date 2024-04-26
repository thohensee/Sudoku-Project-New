import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.sketched_value = None

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        if 1 <= value <= 9:
            self.sketched_value = value

    def draw(self, cell_size):
        cell_rect = pygame.Rect(self.col * cell_size, self.row * cell_size, cell_size, cell_size)
        pygame.draw.rect(self.screen, (255, 0, 0) if self.selected else (0, 0, 0), cell_rect, 3)
        if self.value != 0:
            font = pygame.font.Font(None, 30)
            text_surface = font.render(str(self.value), True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=cell_rect.center)
            self.screen.blit(text_surface, text_rect)
        elif self.sketched_value is not None:
            font = pygame.font.Font(None, 30)
            text_surface = font.render(str(self.sketched_value), True, (128, 128, 128))
            text_rect = text_surface.get_rect(topleft=(cell_rect.left + 5, cell_rect.top + 5))
            self.screen.blit(text_surface, text_rect)

    def clear(self):
        self.value = 0
        self.sketched_value = None

    def reset(self):
        self.value = 0
        self.sketched_value = None

    def update_board(self):
        pass
