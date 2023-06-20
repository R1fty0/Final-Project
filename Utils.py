import pygame
import os
import sys

"""
    Image 
"""


class Image:
    def __init__(self, image_name, folder_name=None):
        """ Loads in a new image and provides other useful image related functions. """
        self.image = self.load_image(folder_name, image_name)

    @staticmethod
    def load_image(folder_name, image_name):
        """ Loads a new image into the game. """
        # load image when not in folder
        if folder_name is None:
            image = pygame.image.load(image_name)
        # load image from folder
        else:
            image = pygame.image.load(os.path.join(folder_name, image_name))
        return image

    def scale_image(self, width, height):
        """ Scales the class's image. """
        self.image = pygame.transform.scale(self.image, (width, height))

    def get_image(self):
        return self.image


""" 
    Text 
"""


class TextEffects:
    def __init__(self):
        self.effects = {"italic": False, "bold": False, "antialiasing": False}

    def enable_effect(self, name):
        """ Allows for the addition or removal of the following text effects: 1. antialiasing; 2. bold; 3. italic """
        match name:
            # enable effect
            case key if key in self.effects and not self.effects[key]:
                self.effects[key] = True
                print(f"Enabled text effect: {key}.")
            # tell user that text effect is enabled
            case key if key in self.effects and self.effects[key]:
                print("Text effect already enabled.")
            case _:
                print(f"Invalid text effect: {name}.")

    def get_effect_state(self, effect_name) -> bool:
        """ Checks the state of a given text effect. """
        if self.effects.get(effect_name) is not None:
            if not self.effects[effect_name]:  # if the effect is set to false
                return False
            else:
                return True   # if the effect is set to true


class Text(TextEffects):
    def __init__(self, font_name, font_size, text, color, background_color=None):
        """ Creates a new text object. """
        TextEffects.__init__(self)
        self.font = self.load_font(font_name, font_size)
        self.label = self.create_label(self.font, color, text, background_color)

    def load_font(self, font_name, font_size) -> pygame.font:
        """ Creates a new font."""
        # check if text is bold or italic
        is_bold = self.get_effect_state("is_bold")
        is_italic = self.get_effect_state("is_italic")
        # load font
        font = pygame.font.SysFont(font_name, font_size, is_bold, is_italic)
        return font

    def create_label(self, font, color, text, background_color):
        """ Creates a new label given a font. """
        # check if text has antialiasing effect
        is_aa = self.get_effect_state("is_antialiasing")
        # load font with transparent background
        if background_color is None:
            label = font.render(text, is_aa, color)
        # load font with given background
        else:
            label = font.render(text, is_aa, color, background_color)
        return label

    def get_text(self):
        return self.label


class GameManager:

    def __init__(self, window_width, window_height, window_name, window_icon):
        """ Handles game visuals and game events. """
        self.active_scene = None
        self.scenes = list()
        self.window = self.create_window(window_width, window_height, window_name, window_icon)

    @staticmethod
    def create_window(width, height, name, icon):
        """ Creates a new game window. """
        window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)
        if icon is None:
            return window
        else:
            pygame.display.set_icon(icon.image)
            return window

    def set_active_scene(self, scene_name):
        """ Sets the active scene of the game. """
        for scene in self.scenes:
            if scene.name == scene_name:
                self.active_scene = scene

    def add_scene(self, scene):
        """ Adds a scene to the game manager. """
        if not isinstance(scene, Scene):
            print(f"The following scene: {scene} is not an instance of the scene class. ")
        self.scenes.append(scene)

    def draw(self, _object, x=None, y=None):
        """ Draws a given object that is either a color, text, or image. """
        # object is text
        if isinstance(_object, Text):
            self.window.blit(_object.get_text(), (x, y))
        # object is an image
        elif isinstance(_object, Image):
            self.window.blit(_object.get_image(), (x, y))
        # object is a color
        elif isinstance(_object, tuple()):
            self.window.fill(_object)

    def run_scene_functions(self):
        """ Run functions in active scene. """
        try:
            # call functions
            for event in self.active_scene.functions:
                event()
            # update screen
            pygame.display.update()
        except AttributeError:
            print("-> Error: No active scene assigned!")
            self.quit_game()

    @staticmethod
    def quit_game():
        """ Quits the game and closes the game window."""
        pygame.quit()
        sys.exit()


class Scene:
    def __init__(self, name, game_manager: GameManager):
        self.name = name
        self.functions = list()
        self.game_manager = game_manager
        game_manager.add_scene(self)

    # double check method name
    def draw_object(self, _object, x=None, y=None):
        """ Adds a function that will draw an image, text or color to the screen when the scene is run. """
        self.functions.append(lambda: self.game_manager.draw(_object, x, y))
