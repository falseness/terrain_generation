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
        self.__normalize_noise(noise)
        return noise

    def __get_noise(self):
        return generate_fractal_noise_2d(NoiseSettings.SIZE, NoiseSettings.PERIOD_OF_NOISE, NoiseSettings.OCTAVES)

    def __normalize_noise(self, noise) -> None:
        min_value = noise.min()
        max_value = noise.max()
        for i in range(len(noise)):
            for j in range(len(noise)):
                noise[i][j] = (noise[i][j] - min_value) / (max_value - min_value)
