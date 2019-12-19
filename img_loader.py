import pygame as pg

def load_img(path):
    loaded_img = pg.image.load(path)

    return loaded_img, loaded_img.get_height(), loaded_img.get_width()
