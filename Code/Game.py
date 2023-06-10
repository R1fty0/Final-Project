import pygame
import sys
from Graphics import Window, Text, Color, Scene

""" Window Setup """
WIDTH = 400
HEIGHT = 400
NAME = 'Computer Programming 12 Final Project'
FPS = 75
window = Window(WIDTH, HEIGHT, NAME, FPS)

""" Colors """
WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)
BLUE = Color(30, 144, 255)
RED = Color(255, 0, 0)

""" Text """
menu_title = Text("Times New Roman", int(WIDTH/10), "CP12 Final Project", BLACK, WHITE)
menu_author = Text("Times New Roman", int(WIDTH/20), "Made by Mohit Sah", BLACK, WHITE)

""" Scenes """
menu = Scene("menu", window)

def set_up_menu():
    """ Sets Up the Functions Used in the Menu Scene. """
    menu.add_function("add_color", WHITE)
    menu.add_function("add_text", menu_title, WIDTH/2 - menu_title.text.get_width()/2, HEIGHT/2 - menu_title.text.get_height() * 2)
    menu.add_function("add_text", menu_author, WIDTH/2 - menu_author.text.get_width()/2, HEIGHT/2 - menu_author.text.get_height() * 1.5)

def main():
    """ Game Logic is executed in this function.  """
    set_up_menu()
    window.set_current_scene(menu.name)
    while True:
        window.clock.tick(window.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        for function in window.current_scene.functions:
            function()
        pygame.display.update()


if __name__ == '__main__':
    main()