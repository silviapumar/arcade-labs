import arcade

# Open up a window.
arcade.open_window(800, 600, "Rest at Dawn.")

# Set background color.
arcade.set_background_color(arcade.color.AMARANTH)

# Get ready to draw.
arcade.start_render()

# The idea is to draw a watermelon.
# Draw the "crust" of the watermelon.
arcade.draw_lrtb_rectangle_filled(0, 800, 160, 100, arcade.color.ALMOND)
arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.BANGLADESH_GREEN)

# Draw the stripes of the "crust".
arcade.draw_lrtb_rectangle_filled(10, 55, 100, 0, arcade.color.DARK_JUNGLE_GREEN)
arcade.draw_lrtb_rectangle_filled(15, 55, 100, 0, arcade.color.DARK_JUNGLE_GREEN)
arcade.draw_lrtb_rectangle_filled(5, 35, 100, 30, arcade.color.DARK_JUNGLE_GREEN)


# Finish the drawing.
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()