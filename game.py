import pygame as pg
from player import Player
from tile import Block, Ground

class Game:

    def __init__(self, screen):
        # self.player = Player()
        self.screen = screen
        # layer
        self.layer_background = []
        self.layer_middle = [Block(x=250, y=250),
                             Ground(x=0, y=500),
                             Ground(x=70, y=500)]
        self.layer_front = []

        # ennemy area
        self.ennemy_list = []

    def run(self):
        pass

    def show(self):
        self.screen.fill((0, 0, 0))
        for i in self.layer_middle:
            self.screen.blit(i.sprite, (i.x, i.y))


