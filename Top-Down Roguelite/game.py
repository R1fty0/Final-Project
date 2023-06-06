from visuals import Color
from visuals import Image
from scene import Scene
from text import Text
import manager

""" Program Constants """
FPS = 60
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
WINDOW_NAME = "Medieval Manor"
WINDOW = manager.create_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_NAME)

""" Main Menu Attributes """
menu = Scene("Menu", WINDOW)
BLUE = Color(0, 191, 225)



def main_menu():
    menu.add_function_call("add_color", BLUE)
    menu.run(FPS)


if __name__ == "__main__":
    main_menu()
