from visuals import Color
from visuals import Image
from scene import Scene
from text import Text
import manager

""" Program Constants """
FPS = 60
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 480
X_SCALE = 48
Y_SCALE = 48
WINDOW_NAME = "Medieval Manor"
WINDOW = manager.create_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_NAME)
game = Scene(WINDOW, FPS)

""" Colors """
PINK = Color(255, 192, 203)


""" Player testing image """
player = Image("player_gun_idle1.png", "Images")
player.scale_image(X_SCALE, Y_SCALE)


def initialize_scene_functions():
    """ Adds the required function calls to the scene. """
    game.add_function_call("add_color", PINK)
    game.add_function_call("draw_image", player, 200, 200)
    # runs the game
    main()


def main():
    """ Where all game logic is run. """
    game.run()


if __name__ == "__main__":
    initialize_scene_functions()
