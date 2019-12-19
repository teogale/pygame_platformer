import img_loader


class Player:

    def __init__(self, x, y):
        self.sprite, self.height, self.width = img_loader.load_img("png/character/walk/walk0001.png")
        self._x = x
        self._y = y
        self._step = 1
        self.life = 100

    def step_down(self):
        self._y += self._step

    def step_up(self):
        self._y -= self._step

    def step_left(self):
        self._x -= self._step

    def step_right(self):
        self._x += self._step

    def gravity(self):
        if self._y <= (600-self.height):
            self.step_down()

    def top_collision_player_layer(self, layer):
        for i in layer:
            print(i.y, self._y + self.height, i.y + i.height)
            print(i.x, self._x, i.x + i.width)
            if i.y <= (self._y + self.height) <= i.y + i.height and i.x <= self._x <= i.x + i.width:
                return False
        return True









