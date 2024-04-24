class Cell:
    def __init__(self, value, row, col, screen):
        self._value = value
        self._row = row
        self._column = col
        self._screen = screen

    def set_cell_value(self, value):
        self._value = value


    def set_sketched_value(self, value):
        self.sketched_value = value


    def draw(self):
        pass

