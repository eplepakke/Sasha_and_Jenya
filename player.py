import pygame
from load_image import load_image
from final_exit import Final

MOVE_SPEED = 5
WIDTH = 24
HEIGHT = 32
COLOR = pygame.Color('green')
STAND_IMAGE = load_image('stand.png', -1)
RIGHT_IMAGES = [load_image('right1.png', -1), load_image('right2.png', -1)]
LEFT_IMAGES = [load_image('left1.png', -1), load_image('left2.png', -1)]
JUMP_IMAGE = load_image('jump.png', -1)
JUMP_POWER = 8
GRAVITY = 0.35


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x_val = 0
        self.y_val = 0
        self.anim_count = 0
        self.on_ground = False
        self.image = STAND_IMAGE
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)
        self.final = False

    def update(self, left, right, up, platforms):
        if self.final:
            return True
        else:
            if self.anim_count + 1 >= 60:
                self.anim_count = 0

            if left:
                self.x_val = -MOVE_SPEED
                self.image = LEFT_IMAGES[self.anim_count // 30]
                self.anim_count += 1

            elif right:
                self.x_val = MOVE_SPEED
                self.image = RIGHT_IMAGES[self.anim_count // 30]
                self.anim_count += 1

            elif not (left or right):
                self.x_val = 0
                self.image = STAND_IMAGE

            if up:
                if self.on_ground:
                    self.y_val = -JUMP_POWER
                self.image = JUMP_IMAGE

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
                if type(p) == Final:
                    self.final = True
                else:
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
