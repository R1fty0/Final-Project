import sys
import pygame
import window_utillty
import image_and_colors
import gameobjects

""" Program Constants """
FPS = 60
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
WINDOW_NAME = "Game 2"
WINDOW = window_utillty.create_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_NAME)  # creates a game window


def main():
    game_clock = pygame.time.Clock()   # creates the game's clock
    is_running = True   # bool that controls whether the game is running or not
    while is_running:
        game_clock.tick(FPS)
        for event in pygame.event.get():  # closes the window
            if event.type == pygame.QUIT:
                sys.exit()

def main_menu():
    pass


if __name__ == "__main__":
    main()
