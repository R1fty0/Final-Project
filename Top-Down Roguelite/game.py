import pygame
from colors import Color
from window import Window, Scene
from text import Text


""" Program Constants """
FPS = 60
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 480
SCALE_X = 48
SCALE_Y = 48
GAME_NAME = "Medieval Manor"

""" Game Window """
game_window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_NAME, FPS)

""" Scenes """
menu = Scene("menu", game_window)
game = Scene("game", game_window)

""" Colors and Text """
menu_color = Color(240, 248, 255)
game_color = Color(255, 160, 122)
white = Color(255, 255, 255)
menu_text = Text("Century Gothic", 20, "This is the menu!", white, menu_color)
game_text = Text("Century Gothic", 20, "This is the game!", white, game_color)

key_pressed = pygame.key.get_pressed()


def initialize():
    # initialize menu functions
    menu.add_function_call("add_color", menu_color)
    menu.add_function_call("add_text", menu_text, 250, 200)
    menu.add_function_call("load_scene_on_key_press", key_pressed, pygame.K_q, game)

    # initialize game functions
    game.add_function_call("add_color", game_color)
    game.add_function_call("add_text", game_text, 250, 200)

    # sets the menu as the starting scene
    game_window.set_current_scene(menu)

    # run the game
    main()


def main():
    game_window.run()


if __name__ == "__main__":
    initialize()
