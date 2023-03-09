
""" Lab 7 - User Control """

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


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


def draw_bubbles(x, y):
    arcade.draw_circle_outline(190 + x, 300 + y, 10, arcade.color.AIR_SUPERIORITY_BLUE, 2, 0, -1)
    arcade.draw_circle_filled(191 + x, 301 + y, 7, arcade.color.AIR_SUPERIORITY_BLUE)


class SeaStar:
    def __init__(self, position_x, position_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_triangle_filled(150, 350, 100, 275, 200, 275, arcade.color.ORANGE)
        # arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)


class MyGame(arcade.Window):
    """ Our Custom Window Class """

    def __init__(self):
        """ Initializer """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, " Lab 7 - User Control ")

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLUE)

        self.ball = SeaStar(50, 50, 20, arcade.color.YELLOW_GREEN)

    def on_draw(self):
        arcade.start_render()
        draw_sand()
        draw_fish(0, 0)
        draw_fish(210, 90)
        draw_fish(20, 315)
        draw_fish(-250, 195)
        draw_fish(360, 265)
        draw_bubbles(-75, 20)
        draw_bubbles(-30, -60)
        draw_bubbles(400, 230)
        draw_bubbles(510, 100)
        draw_bubbles(370, 90)
        draw_bubbles(52, 65)
        draw_bubbles(-120, 219)
        draw_bubbles(560, -90)
        self.ball.draw()

        def on_mouse_motion(self, x, y, dx, dy):
            self.ball.position_x = x
            self.ball.position_y = y


def main():
    window = MyGame()
    arcade.run()


main()
