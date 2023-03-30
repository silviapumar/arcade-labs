""" Sprite Sample Program """

import arcade

# --- Constants ---
SPRITE_SCALING_METEOR = 0.5
SPRITE_SCALING_ALIEN = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites With Walls Example")

        self.player_list = None
        self.meteor_list = None

        self.player_sprite = None

        self.physics_engine = None

    def setup(self):
        arcade.set_background_color(arcade.color.SPACE_CADET)

        self.player_list = arcade.SpriteList()
        self.meteor_list = arcade.SpriteList()

    def on_draw(self):
        arcade.start_render()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

