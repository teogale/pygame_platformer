import pygame as pg
from player import Player
from tile import *
from pygame.locals import *
from map import Map


class Game:

    def __init__(self):
        # pygame basic property
        self.weight = 600
        self.height = 600
        self.screen = pg.display.set_mode([self.weight, self.height])
        self.frame_rate = pg.time.Clock()
        self.clock = 60
        self.map = Map()
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
                #
                # if event.type == KEYDOWN:
                #     if event.key == K_LEFT:
                #         self.map.region = self.player.step_left(self.map.region)
                #     elif event.key == K_RIGHT:
                #         self.map.region = self.player.step_right(self.map.region)
                #     elif event.key == K_UP:
                #         self.map.region = self.player.step_up(self.map.region)
                #     elif event.key == K_SPACE:
                #         if not self.player.jump:
                #             self.player.jump_method(self.map.region)

            # movement test
            key_pressed = pg.key.get_pressed()
            if key_pressed[K_LEFT]:
                self.map.region = self.player.step_left(self.map.region)
            if key_pressed[K_RIGHT]:
                self.map.region = self.player.step_right(self.map.region)
            if key_pressed[K_SPACE]:
                if not self.player.jump:
                    self.player.jump_method(self.map.region)

            # collision player to object in self.map

            # every frame
            self.show()
            self.map.region = self.player.gravity(layer=self.map.region)
            self.map.region, self.player = self.animation_for_layer(self.map.region,
                                                                    self.player)
            # region change
            self.player = self.map.region_changes(player=self.player)

            # test area

            self.frame_rate.tick(self.clock)
            pg.display.update()

    def show(self):
        self.screen.fill((0, 0, 0))
        for i in self.map.region[0]:
            self.screen.blit(i.sprite, (i.x, i.y))
        for i in self.map.region[1]:
            self.screen.blit(i.sprite, (i.x, i.y))
        self.screen.blit(self.player.sprite, (self.player._x, self.player._y))
        for i in self.map.region[2]:
            self.screen.blit(i.sprite, (i.x, i.y))

    def animation_for_layer(self, layer, player):
        for l in range(len(layer)):
            for j, i in enumerate(self.map.region[l]):
                if hasattr(i, "behavior_animation"):
                    i.behavior_animation(layer, player)
        return layer, player

    def object_collision_to_player(self):
        pass
