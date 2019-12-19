import pygame as pg
import img_loader


class Tile:
    pass


class Block(Tile):

    def __init__(self, x, y,):
        self.sprite, self.height, self.width = img_loader.load_img(path="png/block.png")
        self.x = x
        self.y = y

    def behavior(self):
        pass


class Ground(Tile):

    def __init__(self, x, y, ):
        self.sprite, self.height, self.width = img_loader.load_img(path="png/ground.png")
        self.x = x
        self.y = y


class Crate(Tile):

    def __init__(self, x, y,):
        self.sprite, self.height, self.width = img_loader.load_img(path="png/crate.png")
        self.x = x
        self.y = y


class Bonus(Tile):

    def __init__(self, x, y,):
        self.sprite, self.height, self.width = img_loader.load_img(path="png/bonus.png")
        self.x = x
        self.y = y


class BonusUsed(Tile):

    def __init__(self, x, y):
        self.sprite, self.height, self.width = img_loader.load_img(path="png/bonus_used.png")
        self.x = x
        self.y = y


class Bridge(Tile):

    def __init__(self, x, y):
        self.sprite, self.height, self.width = img_loader.load_img(path="png/bridge.png")
        self.x = x
        self.y = y


class GroundCave(Tile):

    def __init__(self, x, y):
        self.sprite, self.height, self.width = img_loader.load_img(path="png/ground_cave.png")
        self.x = x
        self.y = y


class Grass(Tile):

    def __init__(self, x, y):
        self.sprite, self.height, self.width = img_loader.load_img(path="png/grass.png")
        self.x = x
        self.y = y


class Cloud(Tile):

    def __init__(self, x, y):
        self.sprite, self.height, self.width = img_loader.load_img(path="png/cloud_1.png")
        self.x = x
        self.y = y


class Fence(Tile):

    def __init__(self, x, y):
        self.sprite, self.height, self.width = img_loader.load_img(path="png/fence.png")
        self.x = x
        self.y = y


class GoldCoin(Tile):

    def __init__(self, x, y):
        self.sprite, self.height, self.width = img_loader.load_img(path="png/coin_gold.png")
        self.x = x
        self.y = y
