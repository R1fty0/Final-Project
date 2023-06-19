import pygame
import sys
import Utils
pygame.init()


WIDTH = 800
HEIGHT = 600
NAME = "CP12 Final Project"

""" Colors """
WHITE = (255, 255, 255)

""" Text """
menu_header = Utils.Text("Roboto", int(WIDTH / 10), "Main Menu", WHITE)

""" Images """
GAME_ICON = Utils.Image("enemyBlack1.png", "Enemies")


def set_up_window(width, height, name, icon=None):
    """ Creates a new game window. """
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption(name)
    if icon is None:
        return window
    else:
        pygame.display.set_icon(icon.image)
        return window


WINDOW = set_up_window(WIDTH, HEIGHT, NAME, GAME_ICON)


def draw(_object, x=None, y=None):
    object_name = ''
    match _object:
        # object is text
        case isinstance(_object, Utils.Text):
            object_name = 'text'
        # object is an image
        case isinstance(_object, Utils.Image):
            object_name = 'image'
        # object is a color
        case isinstance(_object, tuple()):
            object_name = 'color'
    # object is none of the above
    if object_name is None:
        return
    else:
        # draw image or text
        if object_name == 'string' or 'text':
            WINDOW.blit(_object, (x, y))
        # fill window with color 
        else:
            WINDOW.fill(_object)


# Game loop
def main():
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    main()
