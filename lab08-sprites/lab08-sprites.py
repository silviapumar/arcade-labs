""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_ALIEN = 0.8
SPRITE_SCALING_PLANET = 0.5
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "The Conqueror of Planets")

        self.player_list = None
        self.planet_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.SPACE_CADET)

    def setup(self):
        """ Set up the game and initialize the variables. """

        self.player_list = arcade.SpriteList()
        self.planet_list = arcade.SpriteList()

        self.score = 0

        # All of the sprites are from kenney.nl
        self.player_sprite = arcade.Sprite("alien.png", SPRITE_SCALING_ALIEN)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        arcade.start_render()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
