import pygame

MOVE_SPEED = 7
WIDTH = 24
HEIGHT = 32
COLOR = pygame.Color('green')
JUMP_POWER = 10
GRAVITY = 0.35


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x_val = 0
        self.y_val = 0
        self.startX = x
        self.startY = y
        self.on_ground = False
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(COLOR)
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)

    def update(self, left, right, up, platforms):
        if left:
            self.x_val = -MOVE_SPEED

        if right:
            self.x_val = MOVE_SPEED

        if not (left or right):
            self.x_val = 0

        if up:
            if self.on_ground:
                self.y_val = -JUMP_POWER

        if not self.on_ground:
            self.y_val += GRAVITY

        self.on_ground = False
        self.rect.y += self.y_val
        self.collide(0, self.y_val, platforms)

        self.rect.x += self.x_val
        self.collide(self.x_val, 0, platforms)

    def collide(self, x_val, y_val, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if x_val > 0:
                    self.rect.right = p.rect.left

                if x_val < 0:
                    self.rect.left = p.rect.right

                if y_val > 0:
                    self.rect.bottom = p.rect.top
                    self.on_ground = True
                    self.y_val = 0

                if y_val < 0:
                    self.rect.top = p.rect.bottom
                    self.y_val = 0
