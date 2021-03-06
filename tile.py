import pygame as pg
import img_loader


class Tile:
    pass


class Block(Tile):
    sprite, height, width = img_loader.load_img(path="png/block.png")

    def __init__(self, x, y, ):
        self.x = x
        self.y = y

    def behavior(self):
        pass


class Ground(Tile):
    sprite, height, width = img_loader.load_img(path="png/ground.png")

    def __init__(self, x, y, ):
        self.x = x
        self.y = y


class Crate(Tile):
    sprite, height, width = img_loader.load_img(path="png/crate.png")

    def __init__(self, x, y, ):
        self.x = x
        self.y = y


class Bonus(Tile):
    sprite, height, width = img_loader.load_img(path="png/bonus.png")

    def __init__(self, x, y, ):
        self.x = x
        self.y = y

    def behavior_on_hit(self, layer, j, player):
        layer[1][j] = BonusUsed(x=self.x, y=self.y)
        return layer, player


class BonusUsed(Tile):
    sprite, height, width = img_loader.load_img(path="png/bonus_used.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Bridge(Tile):
    sprite, height, width = img_loader.load_img(path="png/bridge.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y


class GroundCave(Tile):
    sprite, height, width = img_loader.load_img(path="png/ground_cave.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Grass(Tile):
    sprite, height, width = img_loader.load_img(path="png/grass.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Cloud(Tile):
    sprite, height, width = img_loader.load_img(path="png/cloud_1.png")

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.animation_frame = 0
        # direction cloud True right, False left
        self.direction_cloud = True

    def behavior_animation(self, layer, player):

        self.animation_frame += 1
        if self.animation_frame <= 120:
            if self.direction_cloud:
                self.x += 1
            else:
                self.x -= 1
        else:
            self.direction_cloud = not self.direction_cloud
            self.animation_frame = 0
        return layer, player


class Fence(Tile):
    sprite, height, width = img_loader.load_img(path="png/fence.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y


class GoldCoin(Tile):
    sprite, height, width = img_loader.load_img(path="png/coin_gold.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def behavior_on_hit(self, layer, j, player):
        del layer[1][j]
        return layer, player


class Bush(Tile):
    sprite, height, width = img_loader.load_img(path="png/bush.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Spikes(Tile):
    sprite, height, width = img_loader.load_img(path="png/spikes.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def behavior_on_hit(self, layer, j, player):
        if player.life > 0:
            player.life -= 20
        return layer, player


class Water(Tile):
    sprite, height, width = img_loader.load_img(path="png/water.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Plank(Tile):
    sprite, height, width = img_loader.load_img(path="png/plank.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y


class KeyRed(Tile):
    sprite, height, width = img_loader.load_img(path="png/key_red.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def behavior_on_hit(self, layer, j, player):
        del layer[1][j]
        object = Mushroom(self.x + 20, self.y + +35)
        object.animation_bool = True
        layer[1].append(object)
        return layer, player


class Mushroom(Tile):
    sprite, height, width = img_loader.load_img(path="png/shroom.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.animation_bool = False

    def behavior_on_hit(self, layer, j, player):
        del layer[1][j]
        player.life += 20
        return layer, player

    def behavior_animation(self, layer, player):
        if self.animation_bool:
            self.x += 1
        return layer, player


class HillLong(Tile):
    sprite, height, width = img_loader.load_img(path="png/hill_long.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y


class BackgroundForest(Tile):
    sprite, height, width = img_loader.load_img(path="png/background/background_forest.png",
                                                rescale=(600, 600))

    def __init__(self, x, y):
        self.x = x
        self.y = y
