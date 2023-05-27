from enum import Enum
from characters import Character

# swords
# bow and arrows
# axes
# shields
# food
# clothing


class Item:
    def __init__(self, name, max_health):
        self.name = name
        self.health = max_health

    def use(self, cost):
        """ Uses the item once. """
        self.health -= cost

    def get_health(self):
        """ Returns the item's current health. """
        return self.health


class Weapon(Item):
    def __init__(self, name, damage, health, cost, weapon_range):
        Item.__init__(self, name, health)
        self.damage = damage
        self.range = weapon_range
        self.cost = cost

    def attack(self, target: Character, distance):
        """ Attacks a given target if it is in range. """
        if distance > self.range:
            return
        else:
            self.use(self.cost)  # uses the weapon
            target.take_damage(self.damage)  # attacks the target


class Bow(Item, Weapon):
    pass


class Shield(Item):
    def __init__(self, name, health):
        Item.__init__(self, name, health)

    def block(self, damage_blocked):
        """ Blocks a given damage value once. """
        self.use(damage_blocked)


class Food(Item):
    def __init__(self, name, benefit):
        Item.__init__(self, name, 1)
        self.benefit = benefit  # what benefit the food offers to the character

    def eat(self):
        """ Eats the food item """
        self.use(1)


class ClothingState(Enum):
    NEW = False
    WORN = False
    TORN = False
    BROKEN = False


class Clothing(ClothingState):
    def __init__(self,  name, state=ClothingState.NEW):
        self.name = name
        self.state = state

    def set_state(self, state):
        """ Sets the Character's current state. """
        self.state = state

    def get_state(self):
        """ Gets the Character's current state. """
        return self.state

