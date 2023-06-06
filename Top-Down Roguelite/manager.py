import pygame

def create_window(width, height, name) -> pygame.Surface:
    """ Creates a new game window. """
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption(name)
    return window