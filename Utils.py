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


class GameUtils:
    def __init__(self, window):
        self.window = window

    def draw(self, _object, arg_1=None, arg_2=None):
        """ Draws a given object (args): color (values), text (x, y), image (x, y) or button (color, rect). """
        # object is text
        if isinstance(_object, Text):
            self.window.blit(_object.get_text(), (arg_1, arg_2))
        # object is an image
        elif isinstance(_object, Image):
            self.window.blit(_object.get_image(), (arg_1, arg_2))
        # object is a color
        elif isinstance(_object, tuple()):
            self.window.fill(_object)


class SceneManager:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.active_scene = None
        self.scenes = list()

    def set_active_scene(self, scene):
        """ Sets the active scene of the game. """
        for _scene in self.scenes:
            if _scene.name == scene.name:
                self.active_scene = _scene

    def add_scene(self, scene):
        """ Adds a scene to the game manager. """
        if not isinstance(scene, Scene):
            print(f"The following scene: {scene} is not an instance of the scene class. ")
        self.scenes.append(scene)

    def run_scene_functions(self):
        """ Run functions in active scene. """
        try:
            # call functions
            for event in self.active_scene.functions:
                event()
                print(f"Scene: {self.active_scene.name} is active")
                # update screen
            pygame.display.update()
        except AttributeError:
            print("-> Error: No active scene assigned!")
            self.game_manager.quit_game()


class GameManager(GameUtils, SceneManager):

    def __init__(self, window_width, window_height, window_name, window_icon):
        """ Handles game visuals and game events. """
        self.window = self.create_window(window_width, window_height, window_name, window_icon)
        GameUtils.__init__(self, self.window)
        SceneManager.__init__(self, self)

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

    @staticmethod
    def quit_game():
        """ Quits the game and closes the game window."""
        pygame.quit()
        sys.exit()

    def run_game(self):
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
            self.run_scene_functions()


class Scene:
    def __init__(self, name, game_manager: GameManager):
        self.name = name
        self.functions = list()
        self.behavior = list()
        self.game_manager = game_manager
        game_manager.add_scene(self)

    def add_function(self, _type, _object, arg_1=None, arg_2=None):
        if _type.upper() == 'IMAGE' or 'TEXT':
            self.functions.append(lambda: self.game_manager.draw(_object, arg_1, arg_2))
        elif _type.upper == 'COLOR':
            self.functions.append(lambda: self.game_manager.draw(_object))


class Rect:
    def __init__(self, x, y, width, height):
        self.rect = self.create_rect(x, y, width, height)

    @staticmethod
    def create_rect(x, y, width, height):
        """ Creates a new rect. """
        rect = pygame.Rect(x, y, width, height)
        return rect

    def is_colliding(self, rect: pygame.Rect):
        """ Returns true if the rect is colliding with another rect. """
        if self.rect.colliderect(rect):
            return True
        else:
            return False

    def get_rect(self):
        return self.rect


class Button:
    def __init__(self, text, rect: Rect, outline_thickness, outline_color=None):
        """ Creates a button that can be drawn to the screen. """
        self.rect = rect
        if outline_color is None:
            self.outline_color = (255, 255, 255)
        else:
            self.outline_color = outline_color
        self.text = text
        self.outline_thickness = outline_thickness

    def is_clicked(self, event) -> bool:
        """ Returns true if player clicked button. """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.get_rect().collidepoint(event.pos):
                print("clicked")
                return True
            else:
                print("No click")
                return False

