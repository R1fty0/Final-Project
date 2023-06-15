import pygame

# Initialize Pygame
pygame.init()

# Set the width and height of the screen (adjust according to your needs)
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Button Example")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# Define the button class
class Button:
    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, WHITE)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)


# Create a button object
button = Button(300, 250, 200, 100, GREEN, "Click Me")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check if the button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.rect.collidepoint(event.pos):
                print("Button Clicked!")

    # Clear the screen
    screen.fill(BLACK)

    # Draw the button
    button.draw()

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
