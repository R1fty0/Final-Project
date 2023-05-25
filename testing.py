import curses
import random

# Initialize the screen
stdscr = curses.initscr()
curses.curs_set(0)  # Hide the cursor
stdscr.nodelay(1)  # Non-blocking input
stdscr.timeout(100)  # Refresh rate (milliseconds)

# Set up the screen
height, width = stdscr.getmaxyx()
window = curses.newwin(height, width, 0, 0)
window.keypad(1)
window.border(0)

# Create the environment
environment = [
    ["#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#"],
]

# Create boxes in the environment
boxes = [(2, 2), (3, 4), (1, 6)]

# Player position
player_x = 1
player_y = 1

# Items
items = ["Sword", "Shield", "Potion", "Scroll", "Gem"]

# Game loop
while True:
    # Clear the screen
    window.clear()
    window.border(0)

    # Draw the environment
    for y in range(len(environment)):
        for x in range(len(environment[y])):
            if environment[y][x] == "#":
                window.addch(y, x, "#")
            else:
                window.addch(y, x, " ")

    # Draw the boxes
    for box in boxes:
        box_y, box_x = box
        window.addch(box_y, box_x, "B")

    # Draw the player
    window.addch(player_y, player_x, "P")

    # Refresh the screen
    window.refresh()

    # Get user input
    key = window.getch()

    # Player movement
    if key == curses.KEY_UP:
        if player_y > 0 and environment[player_y - 1][player_x] != "#":
            player_y -= 1
    elif key == curses.KEY_DOWN:
        if player_y < len(environment) - 1 and environment[player_y + 1][player_x] != "#":
            player_y += 1
    elif key == curses.KEY_LEFT:
        if player_x > 0 and environment[player_y][player_x - 1] != "#":
            player_x -= 1
    elif key == curses.KEY_RIGHT:
        if player_x < len(environment[player_y]) - 1 and environment[player_y][player_x + 1] != "#":
            player_x += 1
    elif key == ord("q"):  # Quit the game
        break
    elif key == ord("o"):  # Open a box
        for i, box in enumerate(boxes):
            box_y, box_x = box
            if player_y == box_y and player_x == box_x:
                if environment[box_y][box_x] != "O":
                    # Replace the box with an opened box
                    environment[box_y][box_x] = "O"
                    # Generate a random item
                    item = random.choice(items)
                    # Provide feedback to the player on the screen
                    message = f"You opened a box and received a {item}!"
                    window.addstr(height - 1, 0, message)
                    # Print the message to the terminal
                    print(message)
                break

# End the game
curses.endwin()
