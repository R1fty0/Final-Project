from characters import Character


class Enemy(Character):
    def __init__(self, name, health):
        Character.__init__(self, name, health)