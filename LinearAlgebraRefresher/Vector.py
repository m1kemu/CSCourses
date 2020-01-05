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

        return self.magnitude < tolerance


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

        if v1.is_zero or v2.is_zero:
            parallel = True
            return (parallel,scalar_multiple)

        for i, j in zip(v1.coordinates, v2.coordinates):
            i = abs(i)
            j = abs(j)

            if i > j:
                if (i % j).is_integer():
                    parallel = True
                    scalar_multiple = i / j
                else:
                    parallel = False
                    break

            elif j > i:
                if (j % i).is_integer:
                    parallel = True
                    scalar_multiple = j / i
                else:
                    parallel = False
                    break

            else:
                parallel = True
                scalar_multiple = 1

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


def main():

    v = Vector((3.009, -6.172, 3.692, -2.51))
    b = Vector((6.404, -9.144, 2.759, 8.718))

    proj = v.projection(v, b)

    print(f'Projection of {str(v.coordinates)} onto {str(b.coordinates)} is: {str(proj.coordinates)}')

    orth = v.orth_component(v, b)

    print(f'Orthogonal component of {str(v.coordinates)} onto {str(b.coordinates)} is: {str(orth.coordinates)}')

    composition = v.decompose(v, b)

    print(f'Decomposition of {str(v.coordinates)} is: {str(composition[0])} and {str(composition[1])}')


if __name__ == '__main__':
    main()
