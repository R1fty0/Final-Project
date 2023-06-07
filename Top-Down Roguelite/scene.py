import pygame
import sys


class Scene:
    def __init__(self, game_window, fps):
        self.window = game_window
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.function_calls = list()
        self.fps = fps

    def add_function_call(self, function_name, visual_object, x=None, y=None):
        """ Add a function call that is run in the scene's main loop while the scene is running. """
        match function_name:
            case "draw_image":
                self.function_calls.append(lambda: self.draw_image(visual_object, x, y))
            case "draw_text":
                self.function_calls.append(lambda: self.draw_text(visual_object, x, y))
            case "add_color":
                self.function_calls.append(lambda: self.add_color(visual_object))
            case _:
                print("Method calls and/or their arguments are invalid")

    def run(self):
        """ Runs the scene and executes a list of given functions while the game loop is running. """
        self.is_running = True
        while self.is_running:
            self.clock.tick(self.fps)
            for event in pygame.event.get():  # closes the window
                if event.type == pygame.QUIT:
                    sys.exit()
            for function in self.function_calls:  # calls functions
                function()
            if len(self.function_calls) >= 0:  # updates the screen after everything has been drawn
                pygame.display.update()

    def draw_image(self, image_object, x, y):
        """ Draws an image to the game window at the given x and y coordinates. """
        self.window.blit(image_object.image, (x, y))

    def draw_text(self, text_object, x, y):
        """ Draws text to the screen. """
        self.window.blit(text_object.text, (x, y))

    def add_color(self, color):
        """ Fills the window with a solid color. """
        self.window.fill(color.values)

    def update_object(self, obj):
        pass
