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

