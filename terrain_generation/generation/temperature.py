from typing import Tuple
import numpy as np
from perlin_numpy import generate_fractal_noise_2d
from terrain_generation.generation.constants import NoiseSettings
from terrain_generation.generation.utility import normalize_noise
from terrain_generation.draw.map import MapDrawer
from terrain_generation.draw.constants import ColorsAndIntervals


class TemperatureGenerator:
    def generate(self, map_noise):
        arr = self.__generate_main_temperature_distribution()
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                HIGH_RELIEF_HEIGHT = 0.9
                CHANGE_TEMPERATURE = 0.2
                if map_noise[i][j] > HIGH_RELIEF_HEIGHT:
                    arr[i][j] += CHANGE_TEMPERATURE
                MAXIMUM_TEMPERATURE = 1.0
                arr[i][j] = min(arr[i][j], MAXIMUM_TEMPERATURE)
        return arr

    def __generate_main_temperature_distribution(self):
        arr = self.__get_heat_belt_arr(NoiseSettings.SIZE)
        noise = generate_fractal_noise_2d(NoiseSettings.SIZE, NoiseSettings.PERIOD_OF_NOISE, NoiseSettings.OCTAVES)
        normalize_noise(noise)
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
