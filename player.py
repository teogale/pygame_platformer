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
        # count number of coin
        self.coin_count = 0

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
        bottom_screen_limit = 600 - self.height


        if not self.jump and self._y <= (bottom_screen_limit):
            var, layer = self.bot_collision_player_layer(layer=layer)
            if var:
                layer = self.step_down(layer)
        elif self.jump:
            if self.jump_frame <= 15:
                self.step_up(layer)
                self.jump_frame += 1
            else:
                self.jump = False
                self.jump_frame = 0
        return layer

    def bot_collision_player_layer(self, layer):
        mask_player = pg.mask.from_surface(self.sprite)

        for j, i in enumerate(layer[1]):
            mask_object = pg.mask.from_surface(i.sprite)

            if pg.sprite.spritecollide(mask_player, mask_object, False, pg.sprite.collide_mask):
                if hasattr(i, 'behavior_on_hit'):
                    layer, self = i.behavior_on_hit(layer, j, player=self)
                return False, layer
        return True, layer

    def jump_method(self, layer):
        self.jump = True

    def collision_top_player(self, object):
        pass

    def min_pos_player(self):
        self._x = 0 + self.width

    def max_pos_player(self):
        self._x = 600 - self.width

    def collission_left(self):
        pass
