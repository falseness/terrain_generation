import pygame
import sys
import math
from math import sqrt
from random import randrange

width = 800
height = 600
size = [width, height]
black = [0, 0, 0]
green = [0, 255, 0]

def main():
    pygame.init()                               # иницилизация библиотеки
    pygame.font.init()

    screen = pygame.display.set_mode(size)      # создание окна и установка размера
    game_over = False

    font = pygame.font.SysFont('Comic Sans MS', 30, True, False)

    text_x = 100
    text_y = 100


    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        screen.fill(black)

        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit()


if __name__ == '__main__':
    main()