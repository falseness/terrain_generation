import pygame
from typing import Tuple


class MapDrawer:
    def __init__(self, noise_array, screen_size: Tuple[int, int], colors_and_intervals):
        self.__surface = pygame.Surface(screen_size)
        get_color = self.__init_color_array(colors_and_intervals)
        for i in range(len(noise_array)):
            for j in range(len(noise_array[i])):
                get_color_value = round(255 * noise_array[i][j])
                self.__surface.set_at((i, j), get_color[get_color_value])

    def __init_color_array(self, colors_and_intervals):
        previous_interval_end = 0
        get_color_arr = []
        for item in colors_and_intervals:
            color = item[0]
            count = item[1] - previous_interval_end
            get_color_arr += [color] * count
            previous_interval_end = item[1]
        assert len(get_color_arr) == 256
        return get_color_arr

    def save_image(self, filename: str) -> None:
        pygame.image.save(self.__surface, filename + '.png')

    def draw(self, screen: pygame.display, position: Tuple[int, int]):
        screen.blit(self.__surface, position)
