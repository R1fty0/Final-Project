import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame GUI")

# Classes for GUI elements

class Image:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Color:
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 32)

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

class InputField:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.font = pygame.font.Font(None, 32)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect, 2)
        text_surface = self.font.render(self.text, True, BLACK)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

class Text:
    def __init__(self, x, y, text):
        self.text = text
        self.font = pygame.font.Font(None, 32)
        self.rect = pygame.Rect(x, y, 0, 0)

    def draw(self, screen):
        text_surface = self.font.render(self.text, True, BLACK)
        screen.blit(text_surface, self.rect)

# Scene class

class Scene:
    def __init__(self):
        self.gui_elements = []

    def add_element(self, element):
        self.gui_elements.append(element)

    def handle_events(self, event):
        for element in self.gui_elements:
            if isinstance(element, InputField):
                element.handle_event(event)

    def draw(self, screen):
        for element in self.gui_elements:
            element.draw(screen)

# Create a scene
scene = Scene()

# Add GUI elements to the scene


color = Color((255, 0, 0), 200, 200, 100, 100)
scene.add_element(color)

button = Button(300, 300, 100, 50, "Click Me!")
scene.add_element(button)

input_field = InputField(400, 400, 200, 30)
scene.add_element(input_field)

text = Text(500, 500, "Hello, Pygame!")
scene.add_element(text)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        else:
            scene.handle_events(event)

    # Draw the scene
    screen.fill(BLACK)
    scene.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

