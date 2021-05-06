from terrain_generation.generation.utility import normalize_value, generate_common_noise
from terrain_generation.draw.constants import Color
from terrain_generation.draw.map import MapDrawer
from terrain_generation.draw.constants import ColorsAndIntervals
from terrain_generation.generation.constants import NoiseSettings


class MoistureGenerator:
    def generate(self, relief_noise, relief_drawer: MapDrawer):
        arr = [[0] * len(relief_noise[0]) for i in range(len(relief_noise))]
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                #color = relief_drawer.get_color(relief_noise[i][j])
                arr[i][j] = 1.0 - relief_noise[i][j] + 0.075
                arr[i][j] = normalize_value(arr[i][j])
        return arr

    def __get_height_ratio(self, color) -> float:
        if color == Color.DEEP_OCEAN:
            return 1
        if color == Color.OCEAN:
            return 1
        if color == Color.SAND:
            return 0.6
        if color == Color.GRASS:
            return 0.5
        if color == Color.DARK_GRASS:
            return -0.6
        if color == Color.MOUNTAIN:
            return -0.7
        if Color == Color.MOUNTAIN_PEAK:
            return -1
        return 0.0
