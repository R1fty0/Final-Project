import pygame
import Utils
pygame.init()

WIDTH = 800
HEIGHT = 600
NAME = "CP12 Final Project"
GAME_ICON = Utils.Image("enemyBlack1.png", "Enemies")
game_manager = Utils.GameManager(WIDTH, HEIGHT, NAME, GAME_ICON)
WINDOW = game_manager.window


""" Colors """
WHITE = (255, 255, 255)

""" Text """
menu_header = Utils.Text("Roboto", int(WIDTH / 10), "Main Menu", WHITE)

""" Scenes """
menu = Utils.Scene("menu", game_manager)


# Game loop
def main():
    game_manager.set_active_scene(menu.name)
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_manager.quit_game()
        game_manager.run_scene_functions()


if __name__ == '__main__':
    main()
