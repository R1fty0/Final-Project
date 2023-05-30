from world import CursesWindow


def main():
    """ Runs the curses window. """
    game_window = CursesWindow(100, 0, 0)
    running = True

    while running:
        game_window.clear()   # clears all text on the window
        char = game_window.get_input()  # gets input from user
        game_window.add_character(char, 0, 0)  # adds character to screen
        game_window.refresh(2)  # refreshes screen after delay


if __name__ == '__main__':
    main()
