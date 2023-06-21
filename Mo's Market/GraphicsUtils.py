import pygame
import sys
import os


class GraphicsManager:
    def __init__(self, window, frame_rate):
        self.window = window
        self.active_scene = None
        self.scenes = list()
        self.frame_rate = frame_rate

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

    def get_window(self):
        return self.window.window

    def run(self):
        clock = pygame.time.Clock()
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.window.quit_game()
            for _function in self.active_scene.functions:
                _function()
            pygame.display.flip()
            clock.tick(self.frame_rate)



class Window:
    def __init__(self, width, height, name, icon=None):
        self.window = self.create_window(width, height, name, icon)

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
    def close_window():
        """ Quits the game and closes the game window."""
        pygame.quit()
        sys.exit()


class Scene:
    def __init__(self, name, graphics_manager: GraphicsManager):
        self.name = name
        self.functions = list()
        self.behavior = list()
        self.graphics_manager = graphics_manager
        graphics_manager.add_scene(self)

    def add_draw_function(self, _object):
        if isinstance(_object, Text) or isinstance(_object, Image) or isinstance(_object, Color) or isinstance(_object, Button):
            self.functions.append(_object.draw(self.graphics_manager))
        else:
            return


""" 
    Image
"""


class Image:
    def __init__(self, x, y, image_name, folder_name=None):
        """ Loads in a new image and provides other useful image related functions. """
        self.image = self.load_image(folder_name, image_name)
        self.coordinates = (x, y)

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

    def draw(self, graphics_manager):
        graphics_manager.get_window().blit(self.get_image(), self.coordinates)


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

    def get_effect_state(self, effect_name):
        """ Checks the state of a given text effect. """
        if self.effects.get(effect_name) is not None:
            if not self.effects[effect_name]:  # if the effect is set to false
                return False
            else:
                return True   # if the effect is set to true


class Text(TextEffects):
    def __init__(self, x, y, font_name, font_size, text, color, background_color=None):
        """ Creates a new text object. """
        TextEffects.__init__(self)
        self.font = self.load_font(font_name, font_size)
        self.label = self.create_label(self.font, color, text, background_color)
        self.coordinates = (x, y)

    def load_font(self, font_name, font_size):
        """ Creates a new font."""
        pygame.font.init()  # Initialize the font module
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

    def draw(self, graphics_manager):
        graphics_manager.get_window().blit(self.get_text(), self.coordinates)



"""
    Color
"""


class Color:
    def __init__(self, red_val, green_val, blue_val):
        self.color = (red_val, green_val, blue_val)

    def get_color(self):
        return self.color

    def draw(self, graphics_manager):
        graphics_manager.get_window().fill(self.get_color())


"""
    Button
"""


class Button:
    def __init__(self, text_obj, x, y, width, height, color_normal, color_pressed):
        self.text = text_obj
        self.rect = pygame.Rect(x, y, width, height)
        self.color_normal = color_normal
        self.color_pressed = color_pressed
        self.is_pressed = False

    def update(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        if self.rect.collidepoint(event.pos):
                            self.is_pressed = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:  # Left mouse button
                        self.is_pressed = False

    def draw(self, graphics_manager):
        if self.is_pressed:
            pygame.draw.rect(graphics_manager.get_window(), self.color_pressed, self.rect)
        else:
            pygame.draw.rect(graphics_manager.get_window(), self.color_normal, self.rect)
        text_rect = self.text.get_text().get_rect(center=self.rect.center)
        graphics_manager.get_window().blit(self.text.get_text(), text_rect)
