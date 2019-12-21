import pygame as pg
from player import Player
from tile import *
from pygame.locals import *
from map import map


class Game:

    def __init__(self):

        # pygame basic property
        self.weight = 600
        self.height = 600
        self.screen = pg.display.set_mode([self.weight, self.height])
        self.frame_rate = pg.time.Clock()
        self.clock = 60
        self.map_global = map
        # layer
        self.layer = self.map_global[0]
        self.region_count = 0
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
                        self.layer = self.player.step_left(self.layer)
                    elif event.key == K_RIGHT:
                        self.layer = self.player.step_right(self.layer)
                    elif event.key == K_UP:
                        self.layer = self.player.step_up(self.layer)
                    elif event.key == K_SPACE:
                        if not self.player.jump:
                            self.player.jump_method(self.layer)

            self.show()
            self.layer = self.player.gravity(layer=self.layer)
            self.layer, self.player = self.animation_for_layer(self.layer,
                                                               self.player)

            # region change
            if self.player._x > 600 - self.player.width and \
                    self.region_count < len(self.map_global) - 1:
                self.player.min_pos_player()
                self.region_count += 1
                self.layer = self.map_global[self.region_count]

            if self.player._x < 0 and self.region_count > 0:
                self.player.max_pos_player()
                self.region_count -= 1
                self.layer = self.map_global[self.region_count]

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

    def animation_for_layer(self, layer, player):
        for l in range(len(layer)):
            for j, i in enumerate(self.layer[l]):
                if hasattr(i, "behavior_animation"):
                    i.behavior_animation(layer, player)
        return layer, player
