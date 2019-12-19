import pygame as pg

class Tile:

    def load(self, path):
        return pg.image.load(path)


class Block(Tile):

    def __init__(self, x, y,):
        self.sprite = self.load(path="png/block.png")
        self.x = x
        self.y = y

    def behavior(self):
        pass


class Ground(Tile):

    def __init__(self, x, y, ):
        self.sprite = self.load(path="png/ground.png")
        self.x = x
        self.y = y




