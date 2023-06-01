import pygame


class Scene:
    def __init__(self, name):
        self.name = name
        self.clock = pygame.time.Clock()
        self.is_running = True
