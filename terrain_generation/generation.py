from typing import Tuple
from perlin_numpy import (
    generate_fractal_noise_2d, generate_fractal_noise_3d,
    generate_perlin_noise_2d, generate_perlin_noise_3d
)


class NoiseSettings:
    PERIOD_OF_NOISE = (3, 3)
    SIZE = (600, 600)
    OCTAVES = 3


class Generator:
    SIZE = NoiseSettings.SIZE

    def generate(self):
        noise = self.__get_noise()
        min_value, max_value = self.__get_min_and_max(noise)
        self.__normalize_noise(noise, min_value, max_value)
        return noise

    def __get_noise(self):
        return generate_fractal_noise_2d(NoiseSettings.SIZE, NoiseSettings.PERIOD_OF_NOISE, NoiseSettings.OCTAVES)

    def __get_min_and_max(self, noise) -> Tuple[float, float]:
        max_value = min_value = noise[0][0]
        for i in range(len(noise)):
            for j in range(len(noise[i])):
                value = noise[i][j]
                max_value = max(max_value, value)
                min_value = min(min_value, value)
        return min_value, max_value

    def __normalize_noise(self, noise, min_value: float, max_value: float) -> None:
        for i in range(len(noise)):
            for j in range(len(noise)):
                noise[i][j] = (noise[i][j] - min_value) / (max_value - min_value)
