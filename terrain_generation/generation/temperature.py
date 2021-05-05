from typing import Tuple
import numpy as np
from terrain_generation.generation.utility import normalize_value, generate_common_noise
from terrain_generation.draw.map import MapDrawer
from terrain_generation.draw.constants import ColorsAndIntervals


class TemperatureGenerator:
    def generate(self, relief_noise):
        arr = self.__generate_main_temperature_distribution()
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                HIGH_RELIEF_HEIGHT = 0.9
                CHANGE_TEMPERATURE = 0.2
                if relief_noise[i][j] > HIGH_RELIEF_HEIGHT:
                    arr[i][j] += CHANGE_TEMPERATURE
                arr[i][j] = normalize_value(arr[i][j])
        return arr

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
