import pygame

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

""" Menu Text """
menu_font = "Comic Sans MS"
menu_title = Text(menu_font, int(WIDTH/10), "CP12 Final Project", BLACK, WHITE)
menu_author = Text(menu_font, int(WIDTH/20), "Made by Mohit Sah", BLACK, WHITE)
menu_title.enable_effect("antialiasing")


""" Scenes """
menu = Scene("menu", window)
game = Scene("game", window)

def set_up_menu():
    """ Sets Up the Functions Used in the Menu Scene. """
    menu.add_function("add_color", WHITE)
    menu.add_function("add_text", menu_title, WIDTH/2 - menu_title.text.get_width()/2, HEIGHT/2 - menu_title.text.get_height() * 2)
    menu.add_function("add_text", menu_author, WIDTH/2 - menu_author.text.get_width()/2, HEIGHT/2 - menu_author.text.get_height() * 1.5)
    menu.add_function("switch_scene_on_key_press", pygame.K_1, game)

def set_up_game():
    game.add_function("add_color", WHITE)
    game.add_function("switch_scene_on_key_press", pygame.K_2, menu)


def main():
    """ Game Logic is executed in this function.  """
    set_up_menu()
    set_up_game()
    window.set_current_scene(menu.name)
    window.run()



if __name__ == '__main__':
    main()