from pygame import *
from level_loading import load_level
from start_screen import start_screen
from player import *
from platform import *
from camera import *

WIN_WIDTH = 800
WIN_HEIGHT = 640
BACKGROUND_COLOR = pygame.Color('blue')
SIZE = (WIN_WIDTH, WIN_HEIGHT)
FPS = 60

sprites = pygame.sprite.Group()
platforms = []
level = load_level('first.txt')
hero = Player(50, 50)
sprites.add(hero)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

    l = min(0, l)
    l = max(-(camera.width - WIN_WIDTH), l)
    t = max(-(camera.height - WIN_HEIGHT), t)
    t = min(0, t)

    return pygame.Rect(l, t, w, h)


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
    bg.fill(BACKGROUND_COLOR)

    for row in level:
        for col in row:
            if col == "#":
                pf = Platform(x, y)
                sprites.add(pf)
                platforms.append(pf)
            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return
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

        hero.update(left, right, up, platforms)
        camera.update(hero)

        for s in sprites:
            screen.blit(s.image, camera.apply(s))

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    start_screen()
    main()
