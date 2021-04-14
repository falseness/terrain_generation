import pygame
from terrain_generation.draw.constants import Color
from terrain_generation.draw.map import MapDrawer
from typing import Tuple


class MainLoop:
    def __init__(self, map_drawer: MapDrawer, screen_size: Tuple[int, int]):
        self.__map_drawer = map_drawer

        pygame.init()
        self.__screen = pygame.display.set_mode(screen_size)
        pygame.display.flip()

    def iterate(self):
        FPS = 100
        while True:
            if self.__quit_programm():
                return
            self.__draw_all()
            pygame.time.wait(1000 // FPS)

    def __quit_programm(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def __draw_all(self):
        self.__screen.fill(Color.BLACK)

        self.__map_drawer.draw(self.__screen, (0, 0))

        pygame.display.flip()
