import pygame
from image_and_colors import Color


def create_window(width, height, name) -> pygame.Surface:
    """ Creates a new game window. """
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption(name)
    return window


def draw_image(window, image, x, y):
    """ Draws an image to the game window at the given x and y coordinates. """
    window.blit(image, (x, y))
    pygame.display.update()


def draw_text():
    """ Draws text to the screen. """
    pass


def add_color(window, color: Color):
    """ Fills the window with a solid color. """
    window.fill(color.values)
    pygame.display.update()

