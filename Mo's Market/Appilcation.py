import GraphicsUtils

# Create the game window
window = GraphicsUtils.Window(800, 600, "Blue Screen Example")

# Create the graphics manager
graphics_manager = GraphicsUtils.GraphicsManager(window, 60)

# Create the blue screen
blue_color = GraphicsUtils.Color(0, 0, 255)
blue_screen = GraphicsUtils.Scene("Blue Screen", graphics_manager)
blue_screen.add_draw_function(blue_color)

# Create the buttons
button_width = 200
button_height = 50
button_x = (window.window.get_width() - button_width) // 2
button_y = (window.window.get_height() - button_height) // 2

button_text = GraphicsUtils.Text(button_x, button_y, "Arial", 24, "Button", (255, 255, 255))
button_normal_color = GraphicsUtils.Color(0, 0, 200)
button_pressed_color = GraphicsUtils.Color(0, 0, 100)
button = GraphicsUtils.Button(button_text, button_x, button_y, button_width, button_height,
                button_normal_color, button_pressed_color)
button.update()

blue_screen.add_draw_function(button)

# Set the active scene
graphics_manager.set_active_scene(blue_screen)

# Run the game
graphics_manager.run()