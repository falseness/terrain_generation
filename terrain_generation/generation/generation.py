from perlin_numpy import (
    generate_fractal_noise_2d
)

from terrain_generation.generation.constants import NoiseSettings
from terrain_generation.generation.utility import normalize_noise

class Generator:
    def generate(self):
        noise = self.__get_noise()
        normalize_noise(noise)
        return noise

    def __get_noise(self):
        return generate_fractal_noise_2d(NoiseSettings.SIZE, NoiseSettings.PERIOD_OF_NOISE, NoiseSettings.OCTAVES)
