""" Sprite Sample Program """

import arcade

# --- Constants ---
SPRITE_SCALING_METEOR = 0.6
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

        self.score = 0

        # Create the player
        self.player_sprite = arcade.Sprite(":resources:alien.png", SPRITE_SCALING_ALIEN)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        meteor = arcade.Sprite(":resources:meteor.png", SPRITE_SCALING_METEOR)
        meteor.center_x = 300
        meteor.center_y = 200
        self.meteor_list.append(meteor)

        meteor = arcade.Sprite(":resources:meteor.png", SPRITE_SCALING_METEOR)
        meteor.center_x = 364
        meteor.center_y = 200
        self.meteor_list.append(meteor)

    def on_draw(self):
        arcade.start_render()

        self.meteor_list.draw()
        self.player_list.draw()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

