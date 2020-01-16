import pygame
from load_image import load_image

WIN_WIDTH = 800
WIN_HEIGHT = 600
SIZE = (WIN_WIDTH, WIN_HEIGHT)
FPS = 50
pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


def start_screen():
    intro_text = ["", "",
                  "",
                  "",
                  ""]

    fon = pygame.transform.scale(load_image('back.jpg'), (800, 600))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)