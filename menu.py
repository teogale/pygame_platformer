import pygame as pg
import sys
from pygame.locals import *
from tile import

pg.init()
weight = 600
height = 600
screen = pg.display.set_mode([weight, height])
frame_rate = pg.time.Clock()
clock = 60


boucle_jeu = True
while boucle_jeu:

    for event in pg.event.get():
        if event.type == QUIT:
            boucle_jeu = False



    frame_rate.tick(clock)
    pg.display.update()