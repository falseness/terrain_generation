from typing import List


class Color:
    BLACK = (0, 0, 0)
    DEEP_OCEAN = (0, 0, 100)
    OCEAN = (0, 0, 200)
    SAND = (175, 175, 0)
    GRASS = (0, 200, 0)
    DARK_GRASS = (0, 100, 0)
    MOUNTAIN = (77, 77, 77)
    MOUNTAIN_PEAK = (153, 153, 153)

    HEAT_BELTS = [(242, 68, 35), (244, 99, 38), (252, 240, 98), (108, 232, 135), (169, 250, 251), (93, 248, 253)]

    MOISTURE = [(247, 140, 44), (243, 238, 59), (115, 232, 49), (93, 248, 253), (45, 104, 250)]


class Biomes:
    DESERT = (236, 219, 116)
    GRASSLAND = (164, 225, 70)
    TUNDRA = (101, 126, 111)
    ICE = (255, 255, 255)
    SAVANNA = (176, 208, 89)
    WOODLAND = (140, 175, 74)
    BOREAL_FOREST = (94, 115, 53)
    TROPICAL_RAINFOREST = (68, 124, 21)
    SEASONAL_FOREST = (76, 99, 24)
    TEMPERATURE_RAINFOREST = (30, 74, 34)

    def __init__(self):
        self.BIOMES = {}
        biomes_table = [
            [self.DESERT, self.DESERT, self.DESERT, self.GRASSLAND, self.TUNDRA, self.ICE],
            [self.DESERT, self.DESERT, self.DESERT, self.GRASSLAND, self.TUNDRA, self.ICE],
            [self.SAVANNA, self.SAVANNA, self.WOODLAND, self.WOODLAND, self.TUNDRA, self.ICE],
            [self.SAVANNA, self.SAVANNA, self.WOODLAND, self.BOREAL_FOREST, self.TUNDRA, self.ICE],
            [self.TROPICAL_RAINFOREST, self.TROPICAL_RAINFOREST, self.SEASONAL_FOREST, self.BOREAL_FOREST, self.TUNDRA,
             self.ICE],
        ]
        for i in range(len(Color.MOISTURE)):
            biomes_dict = {}
            for j in range(len(Color.HEAT_BELTS)):
                biomes_dict[Color.HEAT_BELTS[j]] = biomes_table[i][j]
            self.BIOMES[Color.MOISTURE[i]] = biomes_dict



class ColorsAndIntervals:
    @staticmethod
    def get_relief():
        return [(Color.DEEP_OCEAN, 70), (Color.OCEAN, 140), (Color.SAND, 160), (Color.GRASS, 200),
                (Color.DARK_GRASS, 230), (Color.MOUNTAIN, 243), (Color.MOUNTAIN_PEAK, 256)]

    @staticmethod
    def get_temperature():
        result = [(Color.HEAT_BELTS[0], 15), (Color.HEAT_BELTS[1], 35), (Color.HEAT_BELTS[2], 55),
                  (Color.HEAT_BELTS[3], 95), (Color.HEAT_BELTS[4], 140), (Color.HEAT_BELTS[5], 256)]
        return result

    @staticmethod
    def get_moisture():
        return [(Color.MOISTURE[0], 60), (Color.MOISTURE[1], 80), (Color.MOISTURE[2], 120), (Color.MOISTURE[3], 160),
                (Color.MOISTURE[4], 256)]
