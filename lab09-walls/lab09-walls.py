""" Sprite Sample Program """
import random

# import random
import arcade
from pyglet.math import Vec2
import os

# --- Constants ---
SPRITE_SCALING_METEOR = 0.6
SPRITE_SCALING_ALIEN = 0.5
SPRITE_SCALING_PLANET = 0.03

PLANET_COUNT = 30

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 650

MOVEMENT_SPEED = 5

CAMERA_SPEED = 1
VIEWPORT_MARGIN = 220


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "The Conqueror of Planets. Pt.2")

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.player_list = None
        self.meteor_list = None
        self.planet_list = None
        self.score = 0

        self.player_sprite = None

        self.physics_engine = None

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):
        arcade.set_background_color(arcade.color.SPACE_CADET)

        self.player_list = arcade.SpriteList()
        self.meteor_list = arcade.SpriteList()
        self.planet_list = arcade.SpriteList()

        self.score = 0

        # The sounds are from mixkit.co
        self.planet_sound = arcade.load_sound(":resources:planet2.wav")

        # All the sprites are from kenney.nl
        self.player_sprite = arcade.Sprite(":resources:alien.png", SPRITE_SCALING_ALIEN)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        # Meteors
        # All the sprites are from kenney.nl
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

        for y in range(173, 650, 64):
            meteor = arcade.Sprite(":resources:meteor.png", SPRITE_SCALING_METEOR)
            meteor.center_x = 780
            meteor.center_y = y
            self.meteor_list.append(meteor)

        coordinate_list = [[400, 500], [462, 500], [400, 555], [462, 555]]
        for coordinate in coordinate_list:
            meteor = arcade.Sprite(":resources:meteor.png", SPRITE_SCALING_METEOR)
            meteor.center_x = coordinate[0]
            meteor.center_y = coordinate[1]
            self.meteor_list.append(meteor)

        # Planets
        # All the sprites are from kenney.nl
        for i in range(PLANET_COUNT):
            planet = arcade.Sprite(":resources:planet.png", SPRITE_SCALING_PLANET)
            planet_placed_successfully = False
            while not planet_placed_successfully:
                planet.center_x = random.randrange(SCREEN_WIDTH)
                planet.center_y = random.randrange(SCREEN_HEIGHT)
                meteor_hit_list = arcade.check_for_collision_with_list(meteor, self.meteor_list)
                planet_hit_list = arcade.check_for_collision_with_list(planet, self.planet_list)
                if len(meteor_hit_list) == 0 and len(planet_hit_list) == 0:
                    planet_placed_successfully = True

            self.planet_list.append(planet)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.meteor_list)

    def on_draw(self):
        self.clear()

        arcade.start_render()

        self.camera_for_sprites.use()

        self.meteor_list.draw()
        self.player_list.draw()
        self.planet_list.draw()

        self.camera_for_gui.use()

        arcade.draw_text(f"Score: {self.score}", 10, 15, arcade.color.WHITE, 14)

    def update(self, delta_time):
        self.physics_engine.update()

        self.scroll_to_player()

        lower_left_corner = (self.player_sprite.center_x - self.width / 2,
                             self.player_sprite.center_y - self.height / 2)
        self.camera_for_sprites.move_to(lower_left_corner, CAMERA_SPEED)

        planet_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.planet_list)

        for planet in planet_hit_list:
            planet.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.planet_sound)

    def scroll_to_player(self):
        position = Vec2(self.player_sprite.center_x - self.width / 2,
                        self.player_sprite.center_y - self.height / 2)
        self.camera_for_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        self.camera_for_sprites.resize(int(width), int(height))
        self.camera_for_gui.resize(int(width), int(height))

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
