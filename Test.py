import pygame

pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Define button properties
button_rect = pygame.Rect(200, 200, 100, 50)
button_color = (255, 0, 0)  # Red color
button_pressed_color = (0, 255, 0)  # Green color
button_pressed = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if button_rect.collidepoint(event.pos):
                    button_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                button_pressed = False

    # Clear the screen
    screen.fill((255, 255, 255))  # White color

    # Draw the button
    if button_pressed:
        pygame.draw.rect(screen, button_pressed_color, button_rect)
    else:
        pygame.draw.rect(screen, button_color, button_rect)

    # Update the display
    pygame.display.flip()
    clock.tick(60)
