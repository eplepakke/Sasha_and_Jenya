import os
import pygame

WIN_WIDTH = 800
WIN_HEIGHT = 600
SIZE = (WIN_WIDTH, WIN_HEIGHT)
pygame.init()
screen = pygame.display.set_mode(SIZE)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image
