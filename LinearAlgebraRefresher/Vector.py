import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must not be empty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return f'Vector: {self.coordinates}'


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def magnitude(self):
        sum = 0

        for coord in self.coordinates:
            sum += (coord ** 2)

        mag = round(math.sqrt(sum), 3)

        return mag

    def normalize(self):
        mag = self.magnitude()

        coords = []

        for coord in self.coordinates:
            coords.append((round((1 / mag) * coord, 3)))

        self.coordinates = tuple(coords)


def main():

    vec_1 = Vector((1.996,3.108,-4.554))

    print(f'Original coordinates: {vec_1.coordinates}')

    mag = vec_1.magnitude()

    print(f'Magnitude: {str(mag)}')

    vec_1.normalize()

    print(f'Normalized coordinates: {vec_1.coordinates}')


if __name__ == '__main__':
    main()
