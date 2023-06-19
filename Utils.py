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
        if folder_name is None:
            image = pygame.image.load(image_name)
        else:
            image = pygame.image.load(os.path.join(folder_name, image_name))
        return image

    def scale_image(self, width, height):
        """ Scales the class's image. """
        self.image = pygame.transform.scale(self.image, (width, height))


""" 
    Text 
"""


class TextEffects:
    def __init__(self):
        self.effects = {"italic": False, "bold": False, "antialiasing": False}

    def enable_effect(self, name):
        """ Allows for the addition or removal of the following text effects: 1. antialiasing; 2. bold; 3. italic """
        match name:
            case key if key in self.effects and not self.effects[key]:
                self.effects[key] = True
                print(f"Enabled text effect: {key}.")
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
        is_bold = self.get_effect_state("is_bold")
        is_italic = self.get_effect_state("is_italic")
        font = pygame.font.SysFont(font_name, font_size, is_bold, is_italic)
        return font

    def create_label(self, font, color, text, background_color):
        """ Creates a new label given a font. """
        is_aa = self.get_effect_state("is_antialiasing")
        if background_color is None:
            label = font.render(text, is_aa, color)  # creates text with a transparent background
        else:
            label = font.render(text, is_aa, color, background_color)  # creates text with a given colored background
        return label

    def get_text(self):
        return self.label





class GameManager:

    def __init__(self, window_width, window_height, window_name, window_icon):
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
        object_name = ''
        match _object:
            # object is text
            case isinstance(_object, Text()):
                object_name = 'text'
            # object is an image
            case isinstance(_object, Image()):
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
                self.window.blit(_object, (x, y))
            # fill window with color
            else:
                self.window.fill(_object)

    def run_scene_functions(self):
        """ Run functions in active scene. """
        try:
            for event in self.active_scene.functions:
                event()
            pygame.display.update()
        except AttributeError:
            print("-> Error: No active scene assigned!")
            self.quit_game()

    def quit_game(self):
        """ Quits the game and closes the game window."""
        pygame.quit()
        sys.exit()

class Scene:
    def __init__(self, name, game_manager: GameManager):
        self.name = name
        self.functions = list()
        game_manager.add_scene(self)

    def add_function(self):
        pass
