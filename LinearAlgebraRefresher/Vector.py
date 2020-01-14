import math

'''
TODO:
'''

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

        mag = math.sqrt(sum)

        return mag


    def normalize(self):
        mag = self.magnitude()

        coords = []

        for coord in self.coordinates:
            try:
                coords.append((1 / mag) * coord)

            except ZeroDivisonError:
                raise Exception('Cannot normalize the zero vector')

        return Vector(tuple(coords))


    def is_zero(self):
        tolerance = 1e-10

        return self.magnitude() < tolerance


    def dot_product(self, v1, v2):
        coords_1 = v1.coordinates
        coords_2 = v2.coordinates

        sum = 0

        if len(coords_1) == len(coords_2):
            for i, j in zip(coords_1, coords_2):
                sum += (i * j)
        else:
            print('The Vectors must be the same length')
            return None

        return sum


    def angle(self, v1, v2):
        dp = v1.dot_product(v1, v2)

        mag_1 = v1.magnitude()
        mag_2 = v2.magnitude()

        if v1.is_zero or v2.is_zero:
            return (0, 0)

        theta_rads = math.acos(dp / (mag_1 * mag_2))
        theta_degrees = math.degrees(theta_rads)

        return (theta_rads, theta_degrees)


    def parallel(self, v1, v2):
        tolerance = 1e-10
        parallel = False
        scalar_multiple = 0
        scalar_multiples = []

        if v1.is_zero() or v2.is_zero():
            parallel = True
            return (parallel,scalar_multiple)

        for i, j in zip(v1.coordinates, v2.coordinates):
            i = abs(i)
            j = abs(j)

            if i > j:
                if float(i / j).is_integer():
                    parallel = True
                    scalar_multiple = i / j
                    scalar_multiples.append(scalar_multiple)
                else:
                    parallel = False
                    break

            elif j > i:
                if float(j / i).is_integer():
                    parallel = True
                    scalar_multiple = j / i
                    scalar_multiples.append(scalar_multiple)
                else:
                    parallel = False
                    break

            else:
                parallel = True
                scalar_multiples.append(1)

        if scalar_multiples.count(scalar_multiples[0]) == len(scalar_multiples):
            parallel = True
        else:
            parallel = False

        return (parallel,scalar_multiple)


    def orthogonal(self, v1, v2):
        tolerance = 1e-10

        if abs(v1.dot_product(v1, v2)) < tolerance:
            return True
        else:
            return False


    def scalar_multiply(self, scalar, v1):
        coords = []

        for i in v1.coordinates:
            coords.append(i * scalar)

        return tuple(coords)


    def subtraction(self, v1, v2):
        coords = []

        for i, j in zip(v1.coordinates, v2.coordinates):
            coords.append(i - j)

        return tuple(coords)


    def projection(self, v, b):
        b_norm = b.normalize()

        dp = v.dot_product(v, b_norm)

        new_coords = v.scalar_multiply(dp, b_norm)

        return Vector(new_coords)


    def orth_component(self, v, b):
        proj = v.projection(v, b)

        coords = v.subtraction(v, proj)

        return Vector(tuple(coords))


    def decompose(self, v, b):
        proj = v.projection(v, b)

        orth = v.orth_component(v, b)

        return [proj, orth]


    def cross_product(self, v1, v2):
        coords = []

        v1_coords = v1.coordinates
        v2_coords = v2.coordinates

        if len(v1_coords) != len(v2_coords):
            print(f'Cannot find the Cross Product of Vectors of different sizes')
            return None

        v1_list = []
        v2_list = []

        for i in range(0, 2):
            for j, k in zip(v1_coords, v2_coords):
                v1_list.append(j)
                v2_list.append(k)

        del(v1_list[0])
        del(v1_list[-1])
        del(v2_list[0])
        del(v2_list[-1])

        for i in range(len(v1_list) - 1):
            coord = (v1_list[i] * v2_list[i+1]) - (v1_list[i+1] * v2_list[i])
            coords.append(coord)

        return Vector(tuple(coords))


    def area_parallelogram(self, v1):
        return v1.magnitude()


    def area_triangle(self, v1):
        mag = v1.magnitude()

        return (mag / 2)


def main():

    v1 = Vector((1, -3))
    v2 = Vector((2, -6))

    print(str(v1.parallel(v1, v2)))


if __name__ == '__main__':
    main()
