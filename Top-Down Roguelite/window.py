import pygame
import sys


class Window:
    def __init__(self, width, height, name, fps):
        self.window = self.create_window(width, height, name)
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.scenes = []
        self.current_scene = None
        self.fps = fps

    def set_current_scene(self, scene):
        """ Set the current scene to the scene with the specified name. """
        for scenes in self.scenes:
            if scenes.name == scene.name:
                self.current_scene = scene
                break
        else:
            print(f"Scene '{scene.name}' not found.")

    def run(self):
        """ Runs the window and the current scene. """
        if self.current_scene is None:
            print("Scene not found!")
            return

        self.is_running = True
        while self.is_running:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.current_scene.call_functions()
            pygame.display.update()

    def create_window(self, width, height, name) -> pygame.Surface:
        """ Creates a new game window. """
        window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)
        return window


class Scene:
    def __init__(self, name, window: Window):
        """ Creates a new scene that can be run in the game window. """
        self.window = window
        self.name = name
        self.function_calls = []
        self.window.scenes.append(self)

    def add_function_call(self, function_name, var_1, var_2=None, var_3=None):
        """ Add a function call that will be called when the scene is running.  """
        match function_name:
            case "draw_image":
                self.function_calls.append(lambda: self.draw_image(var_1, var_2, var_3))
            case "add_text":
                self.function_calls.append(lambda: self.add_text(var_1, var_2, var_3))
            case "add_color":
                self.function_calls.append(lambda: self.add_color(var_1))
            case "load_scene_on_key_press":
                self.function_calls.append(lambda: self.load_scene_on_key_press(var_1, var_2))
            case _:
                print("Method calls and/or their arguments are invalid")

    def call_functions(self):
        """ Update the scene. """
        for function in self.function_calls:
            function()

    def draw_image(self, image_object, x, y):
        """ Draws an image to the game window at the given x and y coordinates. """
        self.window.window.blit(image_object.image, (x, y))

    def add_text(self, text_object, x, y):
        """ Draws text to the game window. """
        self.window.window.blit(text_object.text, (x, y))

    def add_color(self, color):
        """ Fills the game window with a solid color. """
        self.window.window.fill(color.values)

    def load_scene_on_key_press(self, key, next_scene):
        """ Loads the another scene if a condition is met while the current scene is running. """
        key_pressed = pygame.key.get_pressed()
        if key_pressed[key]:
            self.window.set_current_scene(next_scene)
