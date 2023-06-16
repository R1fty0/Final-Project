import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Box Example")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

def draw_box(x, y, width, height, outline_width):
    pygame.draw.rect(screen, GREEN, (x, y, width, height), outline_width)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill((0, 0, 0))
    draw_box(300, 250, 200, 100, 2)  # Adjust the outline width as needed
    pygame.display.update()

pygame.quit()

