import pygame


class Collider:
    def __init__(self, x, y, width, height):
        """ Creates a collider anchored to the provided x and y coordinates. """
        self.collider = pygame.Rect(x, y, width, height)  # collider
        self.x = x  # current x-position of collider
        self.y = y  # current y-position of collider

    def is_colliding(self, game_object) -> bool:
        """ Returns true if this collider is colliding with a given collider.  """
        if self.collider.colliderect(game_object):
            return True
        else:
            return False


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


    def initialize(self):
        """ Sets the starting values needed for the animation to run. """
        current_frame_time = 0
        current_frame_index = 0
        return current_frame_time, current_frame_index


class Player:
    def __init__(self):
        pass

class Enemy:
    def __init__(self):
        pass
