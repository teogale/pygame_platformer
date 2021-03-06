import img_loader
import pygame as pg


class Player:

    def __init__(self, x, y):
        self.sprite, self.height, self.width = img_loader.load_img("png/character/walk/walk0001.png")
        self._x = x
        self._y = y
        self._step = 5
        self.life = 100
        # jump animation
        self.jump = False
        self.jump_frame = 0
        self.fall_frame = 0
        # count number of coin
        self.coin_count = 0

        self.bottom_screen_limit = 600 - self.height

    def step_jump(self):
        self._y += (self.jump_frame - 12) * 2.2

    def step_fall(self):
        self._y += self.fall_frame * 0.8

    def set_step(self, x):
        self._step = x

    def reset_step(self):
        self._step = 5

    def step_down(self, layer):
        self._y += self._step
        return layer

    def step_up(self, layer):

        self._y -= self._step
        return layer

    def step_left(self, layer):
        if self._x > -10:
            self._x -= self._step
        return layer

    def step_right(self, layer):
        if self._x < 550:
            self._x += self._step
        return layer

    def gravity(self, layer):
        var, layer = self.bot_collision_player_layer(layer=layer)

        if not self.jump and self._y <= self.bottom_screen_limit and var:
            self.step_fall()
            if self.fall_frame <= 12:
                self.fall_frame += 1
        elif self.jump:
            if self.jump_frame <= 12:
                self.step_jump()
                self.jump_frame += 1
            else:
                self.jump = False
                self.jump_frame = 0
                self.fall_frame = 0
        return layer

    def bot_collision_player_layer(self, layer):

        for j, i in enumerate(layer[1]):
            if i.y <= (self._y + self.height) <= i.y + i.height and i.x <= self._x + self.width / 2 <= i.x + i.width:
                if hasattr(i, 'behavior_on_hit'):
                    layer, self = i.behavior_on_hit(layer, j, player=self)
                return False, layer
        return True, layer

    def jump_method(self, layer):
        self.jump = True

    def min_pos_player(self):
        self._x = 0 + self.width

    def max_pos_player(self):
        self._x = 600 - self.width

    def collision_top(self, object):
        pass

    def collision_left(self):
        pass


