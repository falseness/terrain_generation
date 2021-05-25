from terrain_generation.generation.utility import normalize_value
from terrain_generation.draw.map import MapDrawer


class MoistureGenerator:
    def generate(self, relief_noise):
        '''
        когда-то тут была своя генерауия карты влажности, но с ней получалось некрасиво, поэтому пришлось отказаться.
        '''
        arr = [[0] * len(relief_noise[0]) for i in range(len(relief_noise))]
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                arr[i][j] = 1.0 - relief_noise[i][j] + 0.075
                arr[i][j] = normalize_value(arr[i][j])
        return arr
