
class Color:
    def __init__(self, red, green, blue):
        """ Creates a new color. """
        self.values = (red, green, blue)

    def get_values(self):
        return self.values