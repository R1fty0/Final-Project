from Characters import Collider
import pygame


class Button(Collider):
    def __init__(self, text, x, y, width, height, outline_width, color=None):
        """ Creates a button that can be drawn to the screen. """
        Collider.__init__(self, x, y, width, height)
        self.x = x
        self.y = y
        if color is None:
            self.color = (255, 255, 255)
        else:
            self.color = color
        self.text_object = text
        self.outline_width = outline_width

    def on_clicked(self) -> bool:
        """ Returns true if player clicked button. """
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.collider.collidepoint(event.pos):
                    return True
            else:
                return False
