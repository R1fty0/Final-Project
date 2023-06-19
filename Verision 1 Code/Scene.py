
class Scene:
    def __init__(self, name, window):
        """ Creates a new scene that can be run in the game window. """
        self.name = name
        self.functions = []
        self.window = window
        self.window.add_scene(self)

    def add_draw_function(self, func_name, arg_1, arg_2=None, arg_3=None):
        """ Add a function call to the list of scene functions.  """
        match func_name:
            case "draw_image":
                self.functions.append(lambda: self.window.draw_image(arg_1, arg_2, arg_3))
            case "draw_text":
                self.functions.append(lambda: self.window.draw_text(arg_1, arg_2, arg_3))
            case "draw_color":
                self.functions.append(lambda: self.window.draw_color(arg_1))
            case "draw_button":
                self.functions.append(lambda: self.window.draw_button(arg_1))
            case _:
                print(f"Error:\n - Function name may be invalid: {func_name}\n - Function arguments may be invalid: {arg_1}, {arg_2}, {arg_3}")

    def remove_function(self, func_name):
        """ Removes a function from the scene's list of functions. """
        for func in self.functions:
            if func.name == func_name:
                self.functions.remove(func)
