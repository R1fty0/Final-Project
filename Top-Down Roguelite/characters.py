import pygame


class Collider:
    def __init__(self, x, y, width, height):
        self.collider = pygame.Rect(x, y, width, height)

    def is_colliding(self, game_object) -> bool:
        """ Returns true if this collider is colliding with a given collider.  """
        if self.collider.colliderect(game_object):
            return True
        else:
            return False


# Base Class was made by AI
class Animation:
    def __init__(self, image_list: list, frame_duration):
        """ Creates an animation that can be played upon request. """
        self.image_list = image_list
        self.frame_duration = frame_duration

    def update(self, scene, current_frame_time, current_frame_index):
        """ Updates the animation. """
        current_frame_time += scene.clock.get_time()
        if current_frame_time >= self.frame_duration:
            current_frame_time = 0
            current_frame_index += 1
            if current_frame_index >= len(self.image_list):
                current_frame_index = 0
        return current_frame_time, current_frame_index

    # may need some work
    def play(self, scene):
        """ Plays the animation and returns its current frame """
        time, frame = self.initialize()
        time, frame = self.update(scene, time, frame)
        return self.image_list[frame]

    def initialize(self):
        """ Sets the starting values needed for the animation to run. """
        current_frame_time = 0
        current_frame_index = 0
        return current_frame_time, current_frame_index
