import img_loader


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

    def step_down(self):
        self._y += self._step

    def step_up(self):
        self._y -= self._step

    def step_left(self):
        self._x -= self._step

    def step_right(self):
        self._x += self._step

    def gravity(self, layer):
        if not self.jump and self._y <= (600-self.height):
            var, layer = self.bot_collision_player_layer(layer=layer)
            if var:
                self.step_down()
        elif self.jump:
            if self.jump_frame <= 15:
                self.step_up()
                self.jump_frame += 1
            else:
                self.jump = False
                self.jump_frame = 0
        return layer

    def bot_collision_player_layer(self, layer):
        for j, i in enumerate(layer):
            if i.y <= (self._y + self.height) <= i.y + i.height and i.x <= self._x + self.width/2 <= i.x + i.width:
                if hasattr(i, 'behavior_on_hit'):
                    layer = i.behavior_on_hit(layer, j)

                return False, layer
        return True, layer

    def jump_method(self, layer):
        self.jump = True


    def collision_top_player(self,object):
        if
        return False









