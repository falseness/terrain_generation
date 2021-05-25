from perlin_numpy import generate_fractal_noise_2d
from terrain_generation.generation.constants import NoiseSettings


def normalize_value(value: float) -> float:
    value = min(value, 1.0)
    value = max(value, 0.0)
    return value

def normalize_noise(noise) -> None:
    min_value = noise.min()
    max_value = noise.max()
    for i in range(len(noise)):
        for j in range(len(noise[i])):
            noise[i][j] = (noise[i][j] - min_value) / (max_value - min_value)


def generate_common_noise():
    noise = generate_fractal_noise_2d(NoiseSettings.SIZE, NoiseSettings.PERIOD_OF_NOISE, NoiseSettings.OCTAVES)
    normalize_noise(noise)
    return noise
