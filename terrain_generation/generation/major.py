from terrain_generation.generation.relief import ReliefGenerator
from terrain_generation.generation.temperature import TemperatureGenerator
from terrain_generation.generation.moisture import MoistureGenerator
from terrain_generation.draw.map import MapDrawer
from terrain_generation.draw.constants import Color, ColorsAndIntervals, Biomes


class MajorGenerator:
    def generate(self):
        relief, relief_drawer = self.__generate_and_save(ReliefGenerator, ColorsAndIntervals.get_relief(), 'relief')
        temperature, temperature_drawer = self.__generate_and_save(TemperatureGenerator,
                                                        ColorsAndIntervals.get_temperature(), 'temperature', relief)
        moisture, moisture_drawer = self.__generate_and_save(MoistureGenerator, ColorsAndIntervals.get_moisture(),
                                                             'moisture', relief, relief_drawer)
        return self.__get_biomes_map(relief, relief_drawer, temperature, temperature_drawer, moisture, moisture_drawer)

    def __generate_and_save(self, generator_cls, colors_and_intervals, image_name, *args):
        generated_arr = generator_cls().generate(*args)
        drawer = MapDrawer(generated_arr, colors_and_intervals)
        drawer.save_image(image_name)
        return generated_arr, drawer

    def __get_biomes_map(self, relief, relief_drawer, temperature, temperature_drawer, moisture, moisture_drawer):
        assert len(temperature) == len(moisture) and len(temperature) == len(relief)
        assert len(temperature[0]) == len(moisture[0]) and len(temperature[0]) == len(relief[0])
        biomes = Biomes()
        result = []
        for i in range(len(temperature)):
            result.append([])
            for j in range(len(temperature[i])):
                relief_color = relief_drawer.get_color(relief[i][j])
                if relief_color == Color.DEEP_OCEAN or relief_color == Color.OCEAN:
                    result[i].append(relief_color)
                else:
                    moisture_color = moisture_drawer.get_color(moisture[i][j])
                    temperature_color = temperature_drawer.get_color(temperature[i][j])
                    result[i].append(biomes.BIOMES[moisture_color][temperature_color])
        return result
