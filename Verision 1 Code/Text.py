import pygame


class TextEffects:
    def __init__(self):
        self.effects = {"italic": False, "bold": False, "antialiasing": False}

    def enable_effect(self, name):
        """ Allows for the addition or removal of the following text effects: 1. antialiasing; 2. bold; 3. italic """
        match name:
            case key if key in self.effects and not self.effects[key]:
                self.effects[key] = True
                print(f"Enabled text effect: {key}.")
            case key if key in self.effects and self.effects[key]:
                print("Text effect already enabled.")
            case _:
                print(f"Invalid text effect: {name}.")

    def check_effect_state(self, effect_name) -> bool:
        """ Checks the state of a given text effect. """
        if self.effects.get(effect_name) is not None:
            if not self.effects[effect_name]:  # if the effect is set to false
                return False
            else:
                return True   # if the effect is set to true


class Text(TextEffects):
    def __init__(self, font_name, font_size, text, color, background_color=None):
        """ Creates a new text object. """
        TextEffects.__init__(self)
        self.font = self.load_font(font_name, font_size)
        self.text = self.create_label(self.font, color, text, background_color)

    def load_font(self, font_name, font_size) -> pygame.font:
        """ Creates a new font."""
        is_bold = self.check_effect_state("is_bold")
        is_italic = self.check_effect_state("is_italic")
        font = pygame.font.SysFont(font_name, font_size, is_bold, is_italic)
        return font

    def create_label(self, font, color, text, background_color):
        """ Creates a new label given a font. """
        is_aa = self.check_effect_state("is_antialiasing")
        if background_color is None:
            label = font.render(text, is_aa, color)  # creates text with a transparent background
        else:
            label = font.render(text, is_aa, color, background_color)  # creates text with a given colored background
        return label