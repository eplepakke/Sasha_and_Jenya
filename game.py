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
BACKGROUND_1 = load_image('back1.png')
BACKGROUND_2 = load_image('back2.png')
BACKGROUND_3 = load_image('back3.png')
ICON = load_image('icon.png')
SIZE = (WIN_WIDTH, WIN_HEIGHT)
FPS = 60

sprites = pygame.sprite.Group()
platforms = list()
level = list()
hero = pygame.sprite.Sprite()
camera = Camera(0, 0, 0)


def load_map_level(map_name, x_player, y_player):
    global sprites, platforms, level, hero, camera

    sprites = pygame.sprite.Group()
    platforms = list()
    level = load_level(map_name)
    hero = Player(x_player, y_player)
    sprites.add(hero)
    x = 0
    y = 0
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

    total_level_width = len(level[0]) * PLATFORM_WIDTH
    total_level_height = len(level) * PLATFORM_HEIGHT
    camera = Camera(camera_configure, total_level_width, total_level_height)


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
    pygame.display.set_icon(ICON)
    bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))

    f = 1
    load_map_level('first.txt', 50, 50)

    left = False
    right = False
    up = False
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return False
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                left = True
            elif e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                right = True
            elif e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                up = True
            elif e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False

        final = hero.update(left, right, up, platforms)
        if final and f == 1:
            load_map_level('second.txt', 32, 64)
            f += 1
        elif final and f == 2:
            load_map_level('third.txt', 32, 32)
            f += 1
        elif final and f == 3:
            return True

        if f == 1:
            bg.blit(BACKGROUND_1, (0, 0))
        elif f == 2:
            bg.blit(BACKGROUND_2, (0, 0))
        else:
            bg.blit(BACKGROUND_3, (0, 0))

        screen.blit(bg, (0, 0))
        camera.update(hero)
        for s in sprites:
            screen.blit(s.image, camera.apply(s))
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    if start_screen():
        if main():
            final_screen()
