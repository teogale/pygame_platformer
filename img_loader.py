import pygame as pg


def load_img(path, rescale=None):
    loaded_img = pg.image.load(path)
    if rescale is not None:
        loaded_img = pg.transform.scale(loaded_img, (rescale[0], rescale[1]))

    return loaded_img, loaded_img.get_height(), loaded_img.get_width()
