import pygame
from terrain_generation.draw.constants import Color
from typing import Tuple


class MapDrawer:
    def __init__(self, noise_array, screen_size: Tuple[int, int]):
        self.__surface = pygame.Surface(screen_size)
        get_color = self.__init_color_array()
        for i in range(len(noise_array)):
            for j in range(len(noise_array[i])):
                get_color_value = round(255 * noise_array[i][j])
                self.__surface.set_at((i, j), get_color[get_color_value])

    def __init_color_array(self):
        colors_and_intervals = [(Color.DEEP_OCEAN, 70), (Color.OCEAN, 140), (Color.SAND, 160), (Color.GRASS, 200),
                                (Color.DARK_GRASS, 230), (Color.MOUNTAIN, 243), (Color.MOUNTAIN_PEAK, 256)]
        previous_interval_end = 0
        get_color_arr = []
        for item in colors_and_intervals:
            color = item[0]
            count = item[1] - previous_interval_end
            get_color_arr += [color] * count
            previous_interval_end = item[1]
        assert len(get_color_arr) == 256
        return get_color_arr

    def draw(self, screen: pygame.display, position: Tuple[int, int]):
        screen.blit(self.__surface, position)
