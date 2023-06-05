from image_n_colors import Color
from image_n_colors import Image
from scene import Scene
from text import Text
import game_manager

""" Program Constants """
FPS = 60
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
WINDOW_NAME = "Medieval Manor"
WINDOW = game_manager.create_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_NAME)  # creates a game window

""" Main Menu Attributes """
menu = Scene("Menu", WINDOW)
BLUE = Color(0, 191, 225)
WHITE = Color(255, 255, 255)
title = Text("Ariel", 58, "Medieval Manor", WHITE, BLUE)
author = Text("Ariel", 32, "Made By Mohit Sah", WHITE, BLUE)

""" Testing Image """
arrow = Image("arrow.png").image


def main_menu():
    menu.add_function_call("add_color", BLUE)
    menu.add_function_call("draw_text", title, title.text.get_width() - 150, 250)
    menu.add_function_call("draw_text", author, author.text.get_width(), 300)
    # menu.add_function_call("draw_image", arrow, 10, 300)
    menu.run(FPS)


if __name__ == "__main__":
    main_menu()
