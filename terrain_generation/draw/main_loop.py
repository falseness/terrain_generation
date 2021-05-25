import pygame
from terrain_generation.draw.constants import Color
from terrain_generation.generation.major import MajorGenerator
from terrain_generation.draw.map import ImageDrawer


class MainLoop:
    def __init__(self):
        generated_map = MajorGenerator().generate()
        drawer = ImageDrawer(generated_map)
        drawer.save_image('terrain')

        self.__map_drawer = drawer

        pygame.init()
        self.__screen = pygame.display.set_mode((len(generated_map), len(generated_map[0])))
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
