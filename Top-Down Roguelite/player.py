from characters import Collider
from enum import Enum

# what do I want the player to do?:
# 1. move
# 2. shoot
# 3. interact with items


class State(Enum):
    IDLE = False
    LEFT = False
    RIGHT = False
    JUMP = False
    FALL = False
    SHOOT = False
    RELOADING = False


class Player(Collider, State):
    def __init__(self, x, y, width, height, speed, state=State.IDLE):
        Collider.__init__(self, x, y, width, height)
        self.vel_x = 0
        self.vel_y = 0
        self.speed = speed
        self.state = state

    def get_input(self):
        """ Registers inputs from the player.  """
        pass

    def shoot(self):
        """ Enables the player to shoot. """
        pass

    def interact(self, item):
        """ Enables the player to interact with an item in the game """
        pass

    def update(self):
        """ Runs all player logic. """




""" GetKeyDown = pygame.key.get_pressed()  # An event that is triggered, akin to the "Input.GetKey()" method from Unity (it is a method right?)

        if GetKeyDown[self.upKey] and self.CanMoveUp:  # Moves Player Up
            Player_Rect.y -= self.speed"""