# This is the "easy to code" drawing.
import arcade


def crust():
    arcade.draw_lrtb_rectangle_filled(0, 800, 160, 100, arcade.color.ALMOND)
    arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.BANGLADESH_GREEN)

    # Draw the stripes of the "crust".
    arcade.draw_lrtb_rectangle_filled(10, 55, 100, 0, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_lrtb_rectangle_filled(5, 35, 100, 30, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_rectangle_filled(160, 0, 45, 80, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_rectangle_filled(178, 50, 49, 100, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_rectangle_filled(730, 32, 15, 100, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_rectangle_filled(705, 50, 35, 100, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_rectangle_filled(303, 37, 65, 80, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_rectangle_filled(306, 45, 34, 100, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_rectangle_filled(310, 50, 28, 100, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_rectangle_filled(620, 50, 55, 100, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_rectangle_filled(640, 35, 35, 40, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_rectangle_filled(494, 18, 70, 90, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_rectangle_filled(500, 50, 40, 100, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_rectangle_filled(390, 65, 58, 70, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_rectangle_filled(390, 50, 46, 100, arcade.color.DARK_JUNGLE_GREEN)


def seeds():
    arcade.draw_ellipse_filled(300, 429, 20, 33, arcade.color.LICORICE)
    arcade.draw_ellipse_filled(720, 310, 20, 33, arcade.color.LICORICE)
    arcade.draw_ellipse_filled(117, 549, 20, 33, arcade.color.LICORICE)
    arcade.draw_ellipse_filled(429, 300, 20, 33, arcade.color.LICORICE)
    arcade.draw_ellipse_filled(629, 204, 20, 33, arcade.color.LICORICE)
    arcade.draw_ellipse_filled(535, 349, 20, 33, arcade.color.LICORICE)
    arcade.draw_ellipse_filled(280, 229, 20, 33, arcade.color.LICORICE)
    arcade.draw_ellipse_filled(491, 570, 20, 33, arcade.color.LICORICE)
    arcade.draw_ellipse_filled(65, 284, 20, 33, arcade.color.LICORICE)
    arcade.draw_ellipse_filled(660, 529, 20, 33, arcade.color.LICORICE)


def main():
    arcade.open_window(800, 600, "The Watermelon.")
    arcade.set_background_color(arcade.color.AMARANTH)
    arcade.start_render()

    crust()
    seeds()

    arcade.finish_render()
    arcade.run()


main()
