import pygame as pg
from player import Player
from tile import *
from pygame.locals import *

class Game:

    def __init__(self):

        #pygame basic property
        self.weight = 600
        self.height = 600
        self.screen = pg.display.set_mode([self.weight, self.height])
        self.frame_rate = pg.time.Clock()
        self.clock = 60


        # layer
        self.layer_background = [Cloud(x=150, y=100),
                                 Fence(x=70, y=450)]

        self.layer_middle = [Block(x=250, y=250),
                             Ground(x=0, y=500),
                             Ground(x=70, y=500),
                             Bonus(x=150, y=250),
                             Bridge(x=140, y=500),
                             Bridge(x=210, y=500),
                             GoldCoin(x=350, y=430)
                             ]

        self.layer_front = [Grass(x=0, y=460)]
        # player area
        self.player = Player(x=250, y=250)
        # ennemy area
        self.ennemy_list = []

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

            self.show()
            if self.player.bot_collision_player_layer(layer=self.layer_middle):
                self.player.gravity()
            self.frame_rate.tick(self.clock)
            pg.display.update()

    def show(self):
        self.screen.fill((0, 0, 0))
        for i in self.layer_background:
            self.screen.blit(i.sprite, (i.x, i.y))
        for i in self.layer_middle:
            self.screen.blit(i.sprite, (i.x, i.y))
        self.screen.blit(self.player.sprite, (self.player._x, self.player._y))
        for i in self.layer_front:
            self.screen.blit(i.sprite, (i.x, i.y))



