# from Characters import Collider

class Item:
    def __init__(self, name, durability, cost):
        self.name = name
        self.durability = durability
        self.cost = cost

    def reduce_durability(self, amount):
        """ Reduces the item's durability by a given amount. """
        self.durability -= amount


class Weapon(Item):
    def __init__(self, name, durability, cost, damage):
        """ Creates a weapon that can damage enemies. """
        Item.__init__(self, name, durability, cost)
        self.damage = damage

class Melee(Weapon):
    def __init__(self, name, durability, cost, damage, attack_range):
        """ Creates a melee weapon which damages enemies within a certain range. """
        Weapon.__init__(self, name, durability, cost, damage)
        self.attack_range = attack_range

class Projectile:
    def __init__(self, image, speed, impact_effect, gravity):
        """ Creates a new projectile that can fly, be effected by gravity, check for enemy collision and apply damage. """
        self.in_air = False
        pass

    def apply_gravity(self):
        """ Applies gravity to the projectile while it is airborne. """
        while self.in_air:
            pass

class Helmet(Item):
    def __init__(self, name, durability, cost, buff, character):
        """ Creates a helmet item which provides a character a buff to their stats """
        Item.__init__(self, name, durability, cost)
        # self.buff = self.determine_buff(buff)
    def take_damage(self, damage):
        """ Makes the helmet take damage. """
        self.reduce_durability(damage)

    def determine_buff(self, buff):
        """ Determines which buff the helmet provides the player. """
        pass
