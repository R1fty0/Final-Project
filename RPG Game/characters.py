from enum import Enum


class CharacterState(Enum):
    """ A state machine that handles all character gameplay states actions. """
    OUT_OF_COMBAT = False
    ATTACKING = False
    DEFENDING = False
    USING_ITEM = False


class Character(CharacterState):
    def __init__(self, name, health, state=CharacterState.OUT_OF_COMBAT):
        self.name = name
        self.health = health
        self.state = state

    def take_damage(self, damage):
        """ Makes the character receive damage. """
        self.health -= damage

    def set_state(self, state):
        """ Sets the Character's current state. """
        self.state = state

    def get_state(self):
        """ Gets the Character's current state. """
        return self.state


class Enemy(Character):
    def __init__(self, name, health):
        Character.__init__(self, name, health)


class Player(Character):
    def __init__(self, name, health):
        Character.__init__(self, name, health)


class PlayerInventory:
    def __init__(self):
        """ Creates and manages the player's inventory. """
        pass

    def initialize(self):
        """ Creates a new inventory for the player. """
        pass

    def view(self):
        """ Displays the player's current inventory to the player. """
        pass

    def add_item(self, item):
        """ Adds a given item to the player's inventory """
        pass

    def remove_item(self, item):
        """ Removes a given item from the player's inventory. """
        pass