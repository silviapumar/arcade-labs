import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "The Sea.")
    arcade.set_background_color(arcade.color.BLUE)
    arcade.start_render()

    draw_sand()
    draw_fish(0, 0)
    draw_fish(210, 80)
    draw_fish(20, 315)

    arcade.finish_render()
    arcade.run()


def draw_sand():
    """Draw the sand at the bottom of the ocean."""
    arcade.draw_lrtb_rectangle_filled(0, 800, 120, 0, arcade.color.CAMEL)


def draw_fish(x, y):
    """Draw multiple fish in the ocean."""
    # Body.
    arcade.draw_ellipse_filled(300 + x, 200 + y, 90, 50, arcade.color.OLD_SILVER)
    # Tail.
    arcade.draw_triangle_filled(290 + x, 200 + y, 240 + x, 220 + y, 240 + x, 180 + y, arcade.color.OLD_SILVER)
    # Eye.
    arcade.draw_circle_filled(325 + x, 205 + y, 5, arcade.color.TAUPE)


# def draw_coral():



main()