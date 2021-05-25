from typing import Tuple
import numpy as np
from terrain_generation.generation.utility import normalize_value, generate_common_noise
from terrain_generation.draw.constants import Color
from terrain_generation.draw.map import MapDrawer

class TemperatureGenerator:
    def generate(self, relief_noise, relief_drawer: MapDrawer):
        arr = self.__generate_main_temperature_distribution()
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                color = relief_drawer.get_color(relief_noise[i][j])
                arr[i][j] += self.__get_height_ratio(color) * relief_noise[i][j]
                arr[i][j] = normalize_value(arr[i][j])
        return arr

    def __get_height_ratio(self, color) -> float:
        if color == Color.GRASS:
            return 0.05
        if color == Color.DARK_GRASS:
            return 0.1
        if color == Color.MOUNTAIN:
            return 0.2
        if color == Color.MOUNTAIN_PEAK:
            return 0.3
        return 0.0

    def __generate_main_temperature_distribution(self):
        noise = generate_common_noise()
        arr = self.__get_heat_belt_arr((len(noise), len(noise[0])))
        return np.multiply(arr, noise)

    def __get_heat_belt_arr(self, size):
        n = size[1]
        m = size[0]
        result = np.array([[self.__get_heat_belt_value(i, (n, m))] * m for i in range(n)]).transpose()
        return result

    def __get_heat_belt_value(self, y_coord: int, size: Tuple[int, int]) -> float:
        map_center = size[0] // 2 - 0.5
        cold_ratio = abs(y_coord - map_center) / map_center
        return cold_ratio
