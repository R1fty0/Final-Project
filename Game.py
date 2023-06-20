import pygame
import Utils
pygame.init()

WIDTH = 800
HEIGHT = 600
NAME = "CP12 Final Project"
GAME_ICON = Utils.Image("enemyBlack1.png", "Enemies")
game_manager = Utils.GameManager(WIDTH, HEIGHT, NAME, GAME_ICON)


""" Colors """
WHITE = (255, 255, 255)

""" Text """
header = Utils.Text("Roboto", int(WIDTH / 10), "Main Menu", WHITE)
subheading = Utils.Text("Century Gothic", int(WIDTH / 40), "Made by Mohit Sah", WHITE)
prompt = Utils.Text("Roboto", int(WIDTH/20), "Press any key to begin", WHITE)

""" Scenes """
menu = Utils.Scene("menu", game_manager)

""" Image """
menu_background = Utils.Image("darkPurple.png", "Background")


def populate_menu():
    # scale background image
    menu_background.scale_image(WIDTH, HEIGHT)
    # add background image to menu
    menu.draw_object(menu_background, 0, 0)
    # add text to menu
    menu.draw_object(header, WIDTH / 2 - header.get_text().get_width() / 2,
                     HEIGHT / 4 - header.get_text().get_height() / 2)
    menu.draw_object(subheading, WIDTH / 2 - subheading.get_text().get_width() / 2,
                     HEIGHT / 3 - subheading.get_text().get_height() / 2)
    menu.draw_object(prompt, WIDTH / 2 - prompt.get_text().get_width() / 2,
                     HEIGHT / 1.2 - prompt.get_text().get_height() / 2)


# Game loop
def main():
    # populate menu scene with visuals
    populate_menu()
    # set active scene
    game_manager.set_active_scene(menu.name)
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_manager.quit_game()
        game_manager.run_scene_functions()


if __name__ == '__main__':
    main()
