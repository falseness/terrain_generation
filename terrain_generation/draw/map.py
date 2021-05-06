import pygame
from typing import Tuple


class SimpleDrawer:
    def save_image(self, filename: str) -> None:
        pygame.image.save(self._surface, 'images/' + filename + '.png')

    def draw(self, screen: pygame.display, position: Tuple[int, int]):
        screen.blit(self._surface, position)


class MapDrawer(SimpleDrawer):
    def __init__(self, noise_array, colors_and_intervals):
        screen_size = (len(noise_array), len(noise_array[0]))

        self._surface = pygame.Surface(screen_size)
        self.__get_color = self.__init_color_array(colors_and_intervals)
        for i in range(len(noise_array)):
            for j in range(len(noise_array[i])):
                self._surface.set_at((i, j), self.get_color(noise_array[i][j]))

    def get_color(self, height: float):
        MAXIMUM_VALUE = 255
        return self.__get_color[round(MAXIMUM_VALUE * height)]

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


class ImageDrawer(SimpleDrawer):
    def __init__(self, image):
        screen_size = (len(image), len(image[0]))

        self._surface = pygame.Surface(screen_size)
        for i in range(len(image)):
            for j in range(len(image[i])):
                self._surface.set_at((i, j), image[i][j])
