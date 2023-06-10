import pygame
import os
pygame.font.init()


class Color:
    def __init__(self, red, green, blue):
        """ Creates a new color. """
        self.values = (red, green, blue)

    def get_values(self):
        """ Returns the values of the color. """
        return self.values

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

class Animation:
    def __init__(self, window, image_list: list, frame_duration):
        """ Creates an animation that can be played upon request. """
        self.image_list = image_list  # list of images that will be looped through when the animation plays
        self.frame_duration = frame_duration  # how long each image will appear on screen - measured in milliseconds
        self.window = window  #

    # this method without the class integration was made by AI
    def update(self, current_frame_time, current_frame_index):
        """ Updates the animation. """
        current_frame_time += self.window.clock.get_time()  # + 1 sec to the time the animation has been playing for
        if current_frame_time >= self.frame_duration:  # moves to the next frame if the frame duration of the last frame has elapsed
            current_frame_time = 0
            current_frame_index += 1
            if current_frame_index >= len(self.image_list):  # resets the animation if it has already played through
                current_frame_index = 0
        return current_frame_time, current_frame_index


    def play(self):  # may need some work
        """ Plays the animation and returns its current frame """
        time, frame = self.initialize()
        time, frame = self.update(time, frame)  # gets the current time and frame
        return self.image_list[frame]


    @staticmethod
    def initialize():
        """ Sets the starting values needed for the animation to run. """
        current_frame_time = 0
        current_frame_index = 0
        return current_frame_time, current_frame_index



class Window:
    def __init__(self, width, height, name, fps):
        """ Creates a new game window that can have images, colors, and text drawn onto it. """
        self.window = self.create_window(width, height, name)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.current_scene = None
        self.scenes = list()

    @staticmethod
    def create_window(width, height, name) -> pygame.Surface:
        """ Creates a new game window. """
        window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)
        return window

    def add_image(self, image_object, x, y):
        """ Draws an image to the game window at the given x and y coordinates. """
        self.window.blit(image_object.image, (x, y))

    def add_text(self, text_object, x, y):
        """ Draws text to the game window. """
        self.window.blit(text_object.text, (x, y))

    def add_color(self, color):
        """ Fills the game window with a solid color. """
        self.window.fill(color.values)

    def set_current_scene(self, scene_name):
        """ Sets the current scene based off its name. """
        for scene in self.scenes:
            if scene.name == scene_name:
                self.current_scene = scene
            else:
                print("Scene not found!")


    def add_scene(self, scene):
        """ Adds a scene to the game window. """
        self.scenes.append(scene)

    def remove_scene(self, scene_name):
        """ Removes a scene from the game window."""
        try:
            self.scenes.remove(scene_name)
        except Exception as e:
            print(f"Error removing scene: {e}")

class Scene:
    def __init__(self, name, window):
        self.name = name
        self.functions = []
        self.window = window
        self.window.add_scene(self)

    def add_function(self, func_name, arg_1, arg_2=None, arg_3=None):
        """ Add a function call to the list of scene functions.  """
        match func_name:
            case "add_image":
                self.functions.append(lambda: self.window.add_image(arg_1, arg_2, arg_3))
            case "add_text":
                self.functions.append(lambda: self.window.add_text(arg_1, arg_2, arg_3))
            case "add_color":
                self.functions.append(lambda: self.window.add_color(arg_1))
            case _:
                print("Method calls and/or their arguments are invalid")

    def remove_function(self, func_name):
        """ Removes a function from the scene's list of functions. """
        for func in self.functions:
            if func.name == func_name:
                self.functions.remove(func)



class TextEffects:
    def __init__(self):
        self.effects = {"is_italic": False, "is_bold": False, "is_antialiasing": False}

    def set(self, name, disable=False):
        match disable:
            case False:  # Enable an effect
                match name:
                    case key if key in self.effects and not self.effects[key]:
                        self.effects[key] = True
                        print(f"Enabled text effect: {key}.")
                    case key if key in self.effects and self.effects[key]:
                        print("Text effect already enabled.")
                    case _:
                        print(f"Invalid text effect: {name}.")
            case True:  # Disable an effect
                match name:
                    case key if key in self.effects and self.effects[key]:
                        self.effects[key] = False
                        print(f"Disabled text effect: {key}.")
                    case key if key in self.effects and not self.effects[key]:
                        print("Text effect already disabled.")
                    case _:
                        print(f"Invalid text effect: {name}.")

    def check_effect_state(self, effect_name) -> bool:
        """ Checks the state of a given text effect. """
        if self.effects.get(effect_name) is not None:
            if not self.effects[effect_name]:  # if the effect is set to false
                return False
            else:
                return True   # if the effect is set to true


class Text(TextEffects):
    def __init__(self, font_name, font_size, text, color, background_color):
        """ Creates a new text object. """
        TextEffects.__init__(self)
        self.font = self.load_font(font_name, font_size)
        self.text = self.create_label(self.font, color, text, background_color)

    def load_font(self, font_name, font_size) -> pygame.font:
        """ Creates a new font."""
        is_bold = self.check_effect_state("is_bold")
        is_italic = self.check_effect_state("is_italic")
        font = pygame.font.SysFont(font_name, font_size, is_bold, is_italic)
        return font

    def create_label(self, font, color, text, background_color):
        """ Creates a new label given a font. """
        is_aa = self.check_effect_state("is_antialiasing")
        label = font.render(text, is_aa, color.values, background_color.values)
        return label

