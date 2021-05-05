from terrain_generation.generation.utility import normalize_value, generate_common_noise
from terrain_generation.draw.constants import Color
from terrain_generation.draw.map import MapDrawer
from terrain_generation.draw.constants import ColorsAndIntervals
from terrain_generation.generation.constants import NoiseSettings


class MoistureGenerator:
    def generate(self, relief_noise, relief_drawer: MapDrawer):
        arr = generate_common_noise()
        MapDrawer(arr, NoiseSettings.SIZE, ColorsAndIntervals.get_moisture()).save_image('moisture_tmp')
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                color = relief_drawer.get_color(relief_noise[i][j])
                arr[i][j] += self.__get_height_ratio(color) * (1.0 - relief_noise[i][j])
                arr[i][j] = normalize_value(arr[i][j])
        return arr

    def __get_height_ratio(self, color) -> float:
        if color == Color.DEEP_OCEAN:
            return 1
        if color == Color.OCEAN:
            return 1
        if color == Color.SAND:
            return 0.3
        return 0.0
