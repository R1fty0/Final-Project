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
prompt = Utils.Text("Roboto", int(WIDTH / 20), "Press any key to begin", WHITE)

""" Play Button """
play_button_text = Utils.Text("Roboto", int(WIDTH / 20), "Play", WHITE)
play_button_rect = Utils.Rect(200, 200, play_button_text.get_text().get_width() + int(WIDTH / 80),
                              play_button_text.get_text().get_height() + int(HEIGHT / 60))
play_button = Utils.Button(play_button_text, play_button_rect, 4, WHITE)

""" Scenes """
menu = Utils.Scene("menu", game_manager)
game = Utils.Scene("game", game_manager)

""" Image """
menu_background = Utils.Image("darkPurple.png", "Background")


def populate_menu():
    # scale background image
    menu_background.scale_image(WIDTH, HEIGHT)
    # add background image to menu
    menu.add_function('image', menu_background, 0, 0)
    # add text to menu
    menu.add_function('text', header, WIDTH / 2 - header.get_text().get_width() / 2,
                      HEIGHT / 4 - header.get_text().get_height() / 2)
    menu.add_function('text', subheading, WIDTH / 2 - subheading.get_text().get_width() / 2,
                      HEIGHT / 3 - subheading.get_text().get_height() / 2)
    menu.add_function('text', prompt, WIDTH / 2 - prompt.get_text().get_width() / 2,
                      HEIGHT / 1.2 - prompt.get_text().get_height() / 2)
    # add button to menu
    menu.add_function('button', play_button, game.name)


def populate_game():
    game.add_function('image', menu_background, 0, 0)


def main():
    populate_menu()
    populate_game()
    game_manager.set_active_scene(menu)
    game_manager.run_game()


if __name__ == '__main__':
    main()
