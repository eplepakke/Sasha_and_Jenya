import pygame
from load_image import load_image

WIN_WIDTH = 800
WIN_HEIGHT = 640
ICON = load_image('icon.png')
SIZE = (WIN_WIDTH, WIN_HEIGHT)
FPS = 60
pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("Sasha and Jenya")
pygame.display.set_icon(ICON)


def start_screen():
    intro_text = ["САША и ЖЕНЯ:", "фантастические приключения",
                  "",
                  "Управление: стрелочки для движения",
                  "",
                  "Предистория: вы рыцарь и обычный",
                  "овало-человек по имени Женя",
                  "Ваша цель - спасти важного члена",
                  "правительства и вашего друга Сашу",
                  "из лап мошенников и заговорщиков.",
                  "Найдите клетку с Сашей и разбейте её!",
                  "Скорее, герой, овало-люди в опасности!!!"]

    fon = pygame.transform.scale(load_image('start.png'), (WIN_WIDTH, WIN_HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
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
                return False
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return True
        pygame.display.flip()
        clock.tick(FPS)
