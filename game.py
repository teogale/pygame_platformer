import pygame as pg
from player import Player
from tile import *
from pygame.locals import *


class Game:

    def __init__(self):

        # pygame basic property
        self.weight = 600
        self.height = 600
        self.screen = pg.display.set_mode([self.weight, self.height])
        self.frame_rate = pg.time.Clock()
        self.clock = 60
        # layer
        self.layer = [
            [Cloud(x=150, y=100),
             Fence(x=70, y=450)
             ],

            [Block(x=250, y=250),
             Ground(x=0, y=500),
             Ground(x=70, y=500),
             Bonus(x=150, y=250),
             Bridge(x=140, y=500),
             Bridge(x=210, y=500),
             GoldCoin(x=350, y=430),
             Spikes(x=270, y=530),
             Spikes(x=340, y=530),
             GoldCoin(x=50, y=430),
             Bridge(x=420, y=500)
             ],

            [Grass(x=0, y=460)
             ]
        ]
        # player area
        self.player = Player(x=250, y=250)
        # ennemy area
        self.ennemy_list = []

    def animation_for_layer(self, layer, player):
        for l in range(len(layer)):
            for j, i in enumerate(self.layer[l]):
                if hasattr(i, "behavior_animation"):
                    i.behavior_animation(layer, player)
        return layer, player

    def run(self):
        pg.init()
        pg.key.set_repeat(1, 0)

        boucle_jeu = True
        while boucle_jeu:

            for event in pg.event.get():
                if event.type == QUIT:
                    boucle_jeu = False
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.player.step_left()
                    elif event.key == K_RIGHT:
                        self.player.step_right()
                    elif event.key == K_UP:
                        self.player.step_up()
                    elif event.key == K_SPACE:
                        if not self.player.jump:
                            self.player.jump_method(self.layer)

            self.show()
            self.layer[1] = self.player.gravity(layer=self.layer[1])
            self.layer, self.player = self.animation_for_layer(self.layer,
                                                               self.player)
            self.frame_rate.tick(self.clock)
            pg.display.update()

    def show(self):

        self.screen.fill((0, 0, 0))
        for i in self.layer[0]:
            self.screen.blit(i.sprite, (i.x, i.y))
        for i in self.layer[1]:
            self.screen.blit(i.sprite, (i.x, i.y))
        self.screen.blit(self.player.sprite, (self.player._x, self.player._y))
        for i in self.layer[2]:
            self.screen.blit(i.sprite, (i.x, i.y))
