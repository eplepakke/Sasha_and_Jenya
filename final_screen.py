import pygame
from load_image import load_image

WIN_WIDTH = 800
WIN_HEIGHT = 640
SIZE = (WIN_WIDTH, WIN_HEIGHT)
FPS = 60
pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


def final_screen():
    text = ["Так держать, Вы спасли Сашу!!!",
            "Овало-люди теперь в безопасности!"]
    fon = pygame.transform.scale(load_image('final.png'), (WIN_WIDTH, WIN_HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 60)
    text_coord = 450
    for line in text:
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
                return
        pygame.display.flip()
        clock.tick(FPS)
