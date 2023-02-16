import arcade

# Open up a window.
arcade.open_window(800, 600, "Rest at Dawn.")

# Set background color.
arcade.set_background_color(arcade.color.AMARANTH)

# Get ready to draw.
arcade.start_render()

# Draw the "crust" of the watermelon.
# (left, right, top, bottom)
arcade.draw_lrtb_rectangle_filled(0, 800, 160, 100, arcade.color.ALMOND)
arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.BANGLADESH_GREEN)

# Draw the stripes of the "crust".


# Finish the drawing.
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()