import curses
import time

class CursesWindow:
    def __init__(self, refresh_rate_milliseconds, left_x, left_y):
        self.refresh_rate = refresh_rate_milliseconds
        self.window = self.create(curses.initscr(), left_x, left_y)

    def create(self, stdscr, left_x, left_y):
        """ Creates a new curses window in the terminal. """
        height, width = stdscr.getmaxyx()
        window = curses.newwin(height, width, left_y, left_x)
        window.keypad(True)
        return window

    def clear(self):
        """ Clears the curses window. """
        self.window.clear()

    def refresh(self, wait_time_seconds):
        """ Refreshes/updates the curses window. """
        time.sleep(wait_time_seconds)
        self.window.refresh()

    def close(self):
        """ Closes the curses window. """
        curses.endwin()

    def add_character(self, character, x, y):
        """ Displays a given character at given coordinates on the curses window. Note: window should be refreshed after
        drawing all characters. """
        self.window.addch(y, x, character)

    def add_text(self, x, y, text):
        """ Add text to the curses window. """
        self.window.addstr(x, y, text)

    def get_input(self):
        """ Returns the user's input in the form of the key they pressed. """
        key = self.window.getch()
        return key


