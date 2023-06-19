import pygame
import os
pygame.font.init()


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


