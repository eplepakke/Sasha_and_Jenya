import pygame
from load_image import load_image

FINAL_WIDTH = 64
FINAL_HEIGHT = 64
FINAL_IMAGE = load_image('fin.png', - 1)


class Final(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = FINAL_IMAGE
        self.rect = pygame.Rect(x, y, FINAL_WIDTH, FINAL_HEIGHT)
