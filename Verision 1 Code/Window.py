import pygame
import sys


class DrawUtils:
    def __init__(self, window):
        """ Class that stores game functions that can run through the window. """
        self.window = window

    def draw_image(self, image_object, x, y):
        """ Draws an image to the game window at the given x and y coordinates. """
        self.window.blit(image_object.image, (x, y))

    def draw_text(self, text_object, x, y):
        """ Draws text to the game window. """
        self.window.blit(text_object.text, (x, y))

    def draw_color(self, color):
        """ Fills the game window with a solid color. """
        self.window.fill(color)

    def draw_button(self, button):
        """ Draws a button to the screen. """
        pygame.draw.rect(self.window, button.color, button.collider, button.outline_width)
        text_rect = button.text_object.text.get_rect(center=button.collider.center)
        self.window.blit(button.text_object.text, text_rect)


class BehaviourUtils:
    def add_button(self, result, button):
        """ Calls a given function if a given button is pressed. """
        on_clicked = button.on_clicked()
        if on_clicked:
            result()


class Window(DrawUtils):
    def __init__(self, width, height, name, fps, icon=None):
        """ Creates a new game window that can have images, colors, and text drawn onto it. """
        self.window = self.create_window(width, height, name, icon)
        DrawUtils.__init__(self, self.window)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.current_scene = None
        self.scenes = list()

    @staticmethod
    def create_window(width, height, name, icon) -> pygame.Surface:
        """ Creates a new game window. """
        window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)
        if icon is None:
            return window
        else:
            pygame.display.set_icon(icon.image)
            return window

    def run(self):
        """ Runs the game window. """
        while True:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            for function in self.current_scene.functions:
                function()
            pygame.display.update()

    def add_scene(self, scene):
        """ Adds a scene to the game window. """
        self.scenes.append(scene)

    def remove_scene(self, scene_name):
        """ Removes a scene from the game window."""
        try:
            self.scenes.remove(scene_name)
        except Exception as e:
            print(f"Error removing scene: {e}")

    def set_current_scene(self, scene_name):  # weird exception handing
        """ Sets the current scene based off its name. """
        for scene in self.scenes:
            if scene.name == scene_name:
                self.current_scene = scene
