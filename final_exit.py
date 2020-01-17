import pygame

FINAL_WIDTH = 64
FINAL_HEIGHT = 64
FINAL_COLOR = pygame.Color('yellow')


class Final(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((FINAL_WIDTH, FINAL_HEIGHT))
        self.image.fill(FINAL_COLOR)
        self.rect = pygame.Rect(x, y, FINAL_WIDTH, FINAL_HEIGHT)