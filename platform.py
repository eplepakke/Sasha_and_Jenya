import pygame
from load_image import load_image

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_IMAGE = load_image('block.png')


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = PLATFORM_IMAGE
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
