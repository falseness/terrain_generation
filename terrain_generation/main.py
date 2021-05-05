from terrain_generation.generation.generation import Generator
from terrain_generation.draw.map import MapDrawer
from terrain_generation.draw.constants import ColorsAndIntervals
from terrain_generation.draw.main_loop import MainLoop
from generation.constants import NoiseSettings
from terrain_generation.generation.temperature import TemperatureGenerator
from terrain_generation.generation.moisture import MoistureGenerator

def main():
    gener = Generator().generate()
    main_dr = MapDrawer(gener, NoiseSettings.SIZE, ColorsAndIntervals.get_relief())
    main_dr.save_image('relief')

    mois = MoistureGenerator().generate(gener, main_dr)
    dr = MapDrawer(mois, NoiseSettings.SIZE, ColorsAndIntervals.get_moisture())
    dr.save_image('moisture')
    '''gener = Generator().generate()
    main_dr = MapDrawer(gener, NoiseSettings.SIZE, ColorsAndIntervals.get_relief())
    temp = TemperatureGenerator()
    dr = MapDrawer(temp.generate(gener), NoiseSettings.SIZE, ColorsAndIntervals.get_temperature())
    main_dr.save_image("relief")
    dr.save_image("temperature")
    main_loop = MainLoop(dr, NoiseSettings.SIZE)

    main_loop.iterate()'''


if __name__ == '__main__':
    main()
