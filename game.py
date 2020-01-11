import pygame
from level_loading import load_level
from start_screen import start_screen

WIN_WIDTH = 800
WIN_HEIGHT = 600
BACKGROUND_COLOR = pygame.Color('blue')
SIZE = (WIN_WIDTH, WIN_HEIGHT)
FPS = 50


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Sasha and Jenya")
    bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(BACKGROUND_COLOR)
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        screen.blit(bg, (0, 0))
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    start_screen()
    main()
