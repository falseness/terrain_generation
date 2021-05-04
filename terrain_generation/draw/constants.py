class Color:
    BLACK = [0, 0, 0]
    DEEP_OCEAN = [0, 0, 100]
    OCEAN = [0, 0, 200]
    SAND = [175, 175, 0]
    GRASS = [0, 200, 0]
    DARK_GRASS = [0, 100, 0]
    MOUNTAIN = [77, 77, 77]
    MOUNTAIN_PEAK = [153, 153, 153]

    HEAT_BELTS = [[242, 68, 35], [244, 99, 38], [252, 240, 98], [108, 232, 135], [169, 250, 251], [93, 248, 253]]


class ColorsAndIntervals:
    @staticmethod
    def get_relief():
        return [(Color.DEEP_OCEAN, 70), (Color.OCEAN, 140), (Color.SAND, 160), (Color.GRASS, 200),
                        (Color.DARK_GRASS, 230), (Color.MOUNTAIN, 243), (Color.MOUNTAIN_PEAK, 256)]
    @staticmethod
    def get_temperature():
        result = [(Color.HEAT_BELTS[0], 15), (Color.HEAT_BELTS[1], 30), (Color.HEAT_BELTS[2], 50),
                  (Color.HEAT_BELTS[3], 90), (Color.HEAT_BELTS[4], 160), (Color.HEAT_BELTS[5], 256)]
        return result