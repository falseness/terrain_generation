import pygame
import sys
from time import time
from perlin_numpy import (
    generate_fractal_noise_2d, generate_fractal_noise_3d,
    generate_perlin_noise_2d, generate_perlin_noise_3d
)


size = [200, 200]
black = [0, 0, 0]
green = [0, 255, 0]

class GameOptions:
    PERIOD_OF_NOISE = (3, 3)
    SIZE = (600, 600)
    OCTAVES = 2
    WIDTH = SIZE[0]
    HEIGHT = SIZE[1]

class MapData:
    def __init__(self, height: int, width: int):
        self._matrix = [[0.0 for x in range(width)] for y in range(height)]

class Generator:
    def __init__(self):
        pass



def main():

    xpix, ypix = GameOptions.HEIGHT, GameOptions.WIDTH
    pp = 8
    deg = 3
    pic = generate_fractal_noise_2d(GameOptions.SIZE, GameOptions.PERIOD_OF_NOISE, GameOptions.OCTAVES)
    '''for q in range(4):
        noise2 = PerlinNoise(octaves=4, seed=(q + 2)*tmp)
        pic2 = [[noise2([i / xpix, j / ypix]) for j in range(xpix)] for i in range(ypix)]
        for i in range(len(pic)):
            for j in range(len(pic[i])):
                pic[i][j] += pic2[i][j]
                '''
    maximum_value = pic[0][0]
    minimum_value = pic[0][0]
    for i in range(len(pic)):
        for j in range(len(pic[i])):
            maximum_value = max(maximum_value, pic[i][j])
            minimum_value = min(minimum_value, pic[i][j])
    for i in range(len(pic)):
        for j in range(len(pic[i])):
            pic[i][j] = (pic[i][j] - minimum_value) / (maximum_value - minimum_value)
    game_over = False

    sur = pygame.Surface(GameOptions.SIZE)
    for i in range(len(pic)):
        for j in range(len(pic[i])):
            color_value = 255 * pic[i][j]
            if color_value < 70:
                color = [0, 0, 100]
            elif color_value < 140:
                color = [0, 0, 200]
            elif color_value < 160:
                color = [175, 175, 0]
            elif color_value < 200:
                color = [0, 200, 0]
            elif color_value < 230:
                color = [0, 100, 0]
            elif color_value < 243:
                color = [77, 77, 77]
            else:
                color = [153, 153, 153]
            sur.set_at((i, j), color)

    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode(GameOptions.SIZE)
    pygame.display.flip()
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        screen.fill(black)

        screen.blit(sur, (0, 0))
        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit()


if __name__ == '__main__':
    main()