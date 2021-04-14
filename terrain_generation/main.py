import pygame
import sys
from time import time
from perlin_noise import PerlinNoise


size = [200, 200]
black = [0, 0, 0]
green = [0, 255, 0]

class GameOptions:
    WIDTH = 400
    HEIGHT = 400
    SIZE = [WIDTH, HEIGHT]

class MapData:
    def __init__(self, height: int, width: int):
        self._matrix = [[0.0 for x in range(width)] for y in range(height)]

class Generator:
    def __init__(self):
        pass



def main():
    tmp = round(time() * 1000)
    print(tmp)
    noise = PerlinNoise(octaves=3, seed=tmp)
    xpix, ypix = GameOptions.HEIGHT, GameOptions.WIDTH
    pic = [[noise([i / xpix, j / ypix]) for j in range(xpix)] for i in range(ypix)]
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
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode(GameOptions.SIZE)
    game_over = False

    sur = pygame.Surface(GameOptions.SIZE)
    for i in range(len(pic)):
        for j in range(len(pic[i])):
            color_value = 255 * pic[i][j]
            if color_value < 70:
                color = [0, 0, 100]
            elif color_value < 140:
                color = [0, 0, 200]
            elif color_value < 180:
                color = [150, 150, 0]
            else:
                color = [0, 200, 0]
            sur.set_at((i, j), color)

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