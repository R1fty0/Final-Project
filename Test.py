import pygame
from pygame.math import Vector2
import math

pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Define a class for the object
class GameObject(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=position)
        self.position = Vector2(position)
        self.angle = 0

    def update(self, target_position):
        direction = Vector2(target_position) - self.position
        self.angle = math.degrees(math.atan2(-direction.y, direction.x))
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

# Create two instances of the GameObject class
object1 = GameObject((200, 300))
object2 = GameObject((600, 300))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the objects
    object1.update(object2.position)

    # Draw the objects
    screen.fill((255, 255, 255))
    screen.blit(object1.image, object1.rect)
    screen.blit(object2.image, object2.rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()