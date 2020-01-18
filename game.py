import pygame
from level_loading import load_level
from load_image import load_image
from start_screen import start_screen
from final_screen import final_screen
from player import Player
from final_exit import Final
from platform import Platform, PLATFORM_WIDTH, PLATFORM_HEIGHT
from camera import Camera

WIN_WIDTH = 800
WIN_HEIGHT = 640
BACKGROUND = load_image('back.png')
SIZE = (WIN_WIDTH, WIN_HEIGHT)
FPS = 60

sprites = pygame.sprite.Group()
platforms = []
level = load_level('first.txt')
hero = Player(50, 50)
sprites.add(hero)


def camera_configure(camera, target_rect):
    x, y, _, _ = target_rect
    _, _, w, h = camera
    x, y = -x + WIN_WIDTH / 2, -y + WIN_HEIGHT / 2

    x = min(0, x)
    x = max(-(camera.width - WIN_WIDTH), x)
    y = max(-(camera.height - WIN_HEIGHT), y)
    y = min(0, y)

    return pygame.Rect(x, y, w, h)


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Sasha and Jenya")

    total_level_width = len(level[0]) * PLATFORM_WIDTH
    total_level_height = len(level) * PLATFORM_HEIGHT

    camera = Camera(camera_configure, total_level_width, total_level_height)

    left = False
    right = False
    up = False
    x = 0
    y = 0

    bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.blit(BACKGROUND, (0, 0))

    for row in level:
        for col in row:
            if col == "#":
                pf = Platform(x, y)
                sprites.add(pf)
                platforms.append(pf)
            elif col == '@':
                fin = Final(x, y)
                sprites.add(fin)
                platforms.append(fin)
            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                left = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                right = True

            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False

            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                up = True

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False

        screen.blit(bg, (0, 0))

        final = hero.update(left, right, up, platforms)
        if final:
            return True
        camera.update(hero)
        for s in sprites:
            screen.blit(s.image, camera.apply(s))

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    if start_screen():
        if main():
            final_screen()
