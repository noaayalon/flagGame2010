import random

import pygame
import consts

screen = pygame.display.set_mode(
    (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def draw_background():
    screen.fill(consts.BACKGROUND_COLOR)
    pygame.display.flip()
    pygame.display.set_caption("The Flag")


def draw_bushes():
    for i in range(20):
        x = random.randint(0, consts.WINDOW_WIDTH)
        y = random.randint(0, consts.WINDOW_HEIGHT)
        screen.blit(consts.BUSH_IMAGE, (x, y))
        pygame.display.flip()


def draw_matrix_hidden():  # when you see the lines of the matrix and the mines
    pass


def draw_lose_message():
    pass


def draw_win_message():
    pass


def draw_message(message, font_size, color, location):
    pass


# run the draw_background() method
pork = True
while pork:
    draw_background()
    draw_bushes()
