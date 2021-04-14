from terrain_generation.generation import Generator
from terrain_generation.draw.map import MapDrawer
from terrain_generation.draw.main_loop import MainLoop


def main():
    generator = Generator()
    main_loop = MainLoop(MapDrawer(generator.generate(), generator.SIZE), generator.SIZE)
    main_loop.iterate()


if __name__ == '__main__':
    main()
