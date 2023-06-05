import pygame
pygame.font.init()


"""
WinnerFont = pygame.font.SysFont("Century Gothic", int(WindowWidth / 20), True, False)
    PromptFont = pygame.font.SysFont("Comic Sans MS", int(WindowHeight / 27), False, False)

    ScreenIsRunning = True
    while ScreenIsRunning:

        Window.fill(Sliver.get_color())  # Background Color

        # Create Text for UI
        PromptLabel = PromptFont.render("Press any mouse button to continue!", True, 1, Sliver.get_color())
        WinnerLabel = "none"

        if PlayerThatWon == 1:
            WinnerLabel = WinnerFont.render("Player 1 Won the Match!", True, 1, Sliver.get_color())
        elif PlayerThatWon == 2:
            WinnerLabel = WinnerFont.render("Player 2 Won the Match!", True, 1, Sliver.get_color())

        # Display UI on Screen
        Window.blit(PromptLabel,
                    (WindowWidth / 2 - PromptLabel.get_width() / 2, WindowHeight / 2 - PromptLabel.get_height() / 2))

        Window.blit(WinnerLabel,
                    (WindowWidth / 2 - WinnerLabel.get_width() / 2, WindowHeight / 4 - WinnerLabel.get_height() / 2))

        pygame.display.update()  # Updates the Screen


"""


class TextEffects:
    def __init__(self):
        self.effects = {"is_italic": False, "is_bold": False, "is_antialiasing": False}

    def set(self, name, disable=False):
        match disable:
            case False:  # Enable an effect
                match name:
                    case key if key in self.effects and not self.effects[key]:
                        self.effects[key] = True
                        print(f"Enabled text effect: {key}.")
                    case key if key in self.effects and self.effects[key]:
                        print("Text effect already enabled.")
                    case _:
                        print(f"Invalid text effect: {name}.")
            case True:  # Disable an effect
                match name:
                    case key if key in self.effects and self.effects[key]:
                        self.effects[key] = False
                        print(f"Disabled text effect: {key}.")
                    case key if key in self.effects and not self.effects[key]:
                        print("Text effect already disabled.")
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
    def __init__(self, font_name, font_size, text, color, background_color):
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
        label = font.render(text, is_aa, color.values, background_color.values)
        return label


