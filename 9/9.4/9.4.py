import math


def main():
    height = int(input('Height: '))
    radius = int(input('Radius: '))
    volume = math.pi * radius ** 2 * height
    surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2
    print('Volume is: {}'.format(volume))
    print('Surface Area is: {}'.format(surface_area))


if __name__ == '__main__':
    main()
