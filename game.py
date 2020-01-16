import pygame
import os
from level_loading import load_level
from start_screen import start_screen

WIN_WIDTH = 800
WIN_HEIGHT = 640
BACKGROUND_COLOR = pygame.Color('blue')
SIZE = (WIN_WIDTH, WIN_HEIGHT)
FPS = 60

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = pygame.Color('red')
level = load_level('first.txt')


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Sasha and Jenya")
    bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(BACKGROUND_COLOR)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return
        screen.blit(bg, (0, 0))
        x = 0
        y = 0
        for row in level:
            for col in row:
                if col == "#":
                    pf = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                    pf.fill(PLATFORM_COLOR)
                    screen.blit(pf, (x, y))
                x += PLATFORM_WIDTH
            y += PLATFORM_HEIGHT
            x = 0
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    start_screen()
    main()
