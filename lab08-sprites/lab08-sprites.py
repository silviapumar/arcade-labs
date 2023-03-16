""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_ALIEN = 0.5
SPRITE_SCALING_PLANET = 0.05
SPRITE_SCALING_METEOR = 0.6
PLANET_COUNT = 70
METEOR_COUNT = 50

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 650


class MyGame(arcade.Window):
    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "The Conqueror of Planets")

        self.player_list = None
        self.planet_list = None
        self.meteor_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.SPACE_CADET)

    def setup(self):
        """ Set up the game and initialize the variables. """

        self.player_list = arcade.SpriteList()
        self.planet_list = arcade.SpriteList()
        self.meteor_list = arcade.SpriteList()

        self.score = 0

        # All the sprites are from kenney.nl
        self.player_sprite = arcade.Sprite(":resources:alien.png", SPRITE_SCALING_ALIEN)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(PLANET_COUNT):
            # All the sprites are from kenney.nl
            planet = arcade.Sprite(":resources:planet.png", SPRITE_SCALING_PLANET)
            planet.center_x = random.randrange(SCREEN_WIDTH)
            planet.center_y = random.randrange(SCREEN_HEIGHT)
            self.planet_list.append(planet)

        for i in range(METEOR_COUNT):
            # All the sprites are from kenney.nl
            meteor = arcade.Sprite(":resources:meteor.png", SPRITE_SCALING_METEOR)
            meteor.center_x = random.randrange(SCREEN_WIDTH)
            meteor.center_y = random.randrange(SCREEN_HEIGHT)
            self.meteor_list.append(meteor)

    def on_draw(self):
        arcade.start_render()
        self.planet_list.draw()
        self.meteor_list.draw()
        self.player_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """
        self.planet_list.update()
        self.meteor_list.update()
        planet_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.planet_list)
        # meteor_hit_list = arcade.check_for_collision_with_list(self.player_list, self.meteor_list)

        for planet in planet_hit_list:
            planet.remove_from_sprite_lists()
            self.score += 1

        # for meteor in meteor_hit_list:
        #    meteor.remove_from_sprite_lists()
        #    self.score -= 1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
