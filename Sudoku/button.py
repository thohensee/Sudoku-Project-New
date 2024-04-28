# Credits to baraltech on YouTube/GitHub for the tutorial of this Button class
class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image # Variable for the image to be displayed as button
        self.x_pos = pos[0] # Determines x position
        self.y_pos = pos[1] # Determines y position
        self.font = font # Determines font
        self.base_color, self.hovering_color = base_color, hovering_color # Determines the base color
        self.text_input = text_input # Allows for text to be displayed within button
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None: # If no image is chosen, the text by itself will function as a button
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos)) # Determines position of button
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos)) # Determines position of text with respect to button

    def update(self, screen): # Puts button on the screen with respect to the rect, which determines the position
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkInput(self, position): # Checks if the button has been clicked with respect to position of mouse
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position): # Changes color of text when button is hovered over by mouse
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)