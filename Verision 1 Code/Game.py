from Images_and_Animation import Image
from Button import Button
from Text import Text
from Window import Window
from Scene import Scene

""" Window """
WIDTH = 800
HEIGHT = 800
NAME = 'Computer Programming 12 Final Project'
FPS = 75
# GAME_ICON = Image("enemyBlue3.png", "Enemies")
# GAME_ICON.scale_image(GAME_ICON.image.get_width()/3, GAME_ICON.image.get_height()/2)
window = Window(WIDTH, HEIGHT, NAME, FPS)


def create_menu():
    # create the menu scene
    menu = Scene("menu", window)

    # load the menu's background
    menu_background = Image("darkPurple.png", "Background")
    menu_background.scale_image(WIDTH, HEIGHT)

    # load the menu's header text
    header_font = "Roboto"
    header_color = (255, 255, 255)
    header = Text(header_font, int(WIDTH / 10), "Main Menu", header_color)

    # load the menu's 'made by' text
    made_by_font = "Century Gothic"
    made_by_text = Text(made_by_font, int(WIDTH / 40), "Made by Mohit Sah", header_color)

    # load the menu's instructions to the user
    instruction_font = "Ariel"
    instruction_text = Text(instruction_font, int(WIDTH / 30), "Press any key to begin!", header_color)

    # adds the functions that will be run when the menu is running
    menu.add_draw_function("draw_image", menu_background, 0, 0)
    menu.add_draw_function("draw_text", header, WIDTH / 2 - header.text.get_width() / 2, HEIGHT / 4 - header.text.get_height() / 2)
    menu.add_draw_function("draw_text", made_by_text, WIDTH / 2 - made_by_text.text.get_width() / 2, HEIGHT / 3 - made_by_text.text.get_height() / 2)
    menu.add_draw_function("draw_text", instruction_text, WIDTH / 2 - instruction_text.text.get_width() / 2, HEIGHT / 1.2 - instruction_text.text.get_height() / 2)

    # add a button to the screen
    menu.add_draw_function("draw_button", Button(Text("Roboto", int(WIDTH / 40), "Hello there", (198, 221, 223)), 200, 500, 100, 30, 2))

    # returns the menu scene
    return menu


def main():
    """ Game Logic is executed in this function.  """
    menu = create_menu()
    window.set_current_scene(menu.name)
    window.run()


if __name__ == '__main__':
    main()
