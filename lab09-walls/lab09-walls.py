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

        self.physics_engine = None

    def setup(self):
        arcade.set_background_color(arcade.color.SPACE_CADET)

        self.player_list = arcade.SpriteList()
        self.meteor_list = arcade.SpriteList()

        self.score = 0

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

        for x in range(173, 650, 64):
            meteor = arcade.Sprite(":resources:meteor.png", SPRITE_SCALING_METEOR)
            meteor.center_x = x
            meteor.center_y = 350
            self.meteor_list.append(meteor)

        coordinate_list = [[400, 500], [470, 500], [400, 570], [470, 570]]

        for coordinate in coordinate_list:
            meteor = arcade.Sprite(":resources:meteor.png", SPRITE_SCALING_METEOR)
            meteor.center_x = coordinate[0]
            meteor.center_y = coordinate[1]
            self.meteor_list.append(meteor)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.meteor_list)

    def on_draw(self):
        arcade.start_render()

        self.meteor_list.draw()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

