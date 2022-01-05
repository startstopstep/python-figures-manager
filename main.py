from math import pi, pow, sqrt
from abc import ABC, abstractmethod
from drawing import Drawing


def get_type(coords: tuple):
    if len(coords) == 1:
        return "Circle"
    elif len(coords) == 3:
        return "Triangle"
    elif len(coords) == 4:
        return "Rectangle"
    else:
        raise Exception('You should input correct coordinates.')


class Figure(ABC):

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_square(self):
        pass

    @abstractmethod
    def draw_figure(self):
        pass


class Circle(Figure):
    def __init__(self, coords: tuple):
        self.coords = coords
        self.r = sqrt(pow((0 - coords[0][0]), 2) + pow((0 - coords[0][1]), 2))

    def get_perimeter(self):
        return 2 * pi * self.r

    def get_square(self):
        return pi * pow(self.r, 2)

    def draw_figure(self):
        cr = Drawing()
        cr.draw_circle(self.r)


class Triangle(Figure):
    def __init__(self, coords):
        self.coords = coords
        self.AB = sqrt(pow((coords[1][0] - coords[0][0]), 2) + pow((coords[1][1] - coords[0][1]), 2))
        self.BC = sqrt(pow((coords[2][0] - coords[1][0]), 2) + pow((coords[2][1] - coords[1][1]), 2))
        self.CA = sqrt(pow((coords[2][0] - coords[0][0]), 2) + pow((coords[2][1] - coords[0][1]), 2))

    def get_perimeter(self):
        return self.AB + self.BC + self.CA

    def get_square(self):
        p = Triangle.get_perimeter(self) / 2
        return sqrt(p * (p - self.AB) * (p - self.BC) * (p - self.CA))

    def draw_figure(self):
        tr = Drawing()
        tr.draw_triangle(self.coords)


class Rectangle(Figure):
    def __init__(self, coords: tuple):
        self.coords = coords
        self.AB = sqrt(pow((coords[0][0] - coords[1][0]), 2) + pow((coords[0][1] - coords[1][1]), 2))
        self.BC = sqrt(pow((coords[1][0] - coords[2][0]), 2) + pow((coords[1][1] - coords[2][1]), 2))

    def get_perimeter(self):
        return (self.AB + self.BC) * 2

    def get_square(self):
        return self.AB * self.BC

    def draw_figure(self):
        rc = Drawing()
        rc.draw_rectangle(self.coords)


figures = {'Circle': Circle,
           'Triangle': Triangle,
           'Rectangle': Rectangle,
           }

if __name__ == '__main__':
    points = int(input("Hello, user. Please, input how many points have this figure: "))
    while points not in (1, 3, 4):
        points = int(input("Hello, user. Please, input how many points have this figure: "))
    coords = list()
    for i in range(1, points + 1):
        coords.append(tuple(int(x) for x in input(f"Input coordinates of {i} point: ").split(",")))
    coords = tuple(coords)
    fg = figures[get_type(coords)](coords)
    choices = {'perimeter': fg.get_perimeter,
               'square': fg.get_square,
               'draw': fg.draw_figure,
               }

    print('Available 3 commands: "perimeter", "square" and "draw".')
    s = input('Input commands: ').lower()
    if "perimeter" in s:
        print(f'Perimeter: {choices["perimeter"]()}')
    if "square" in s:
        print(f'Square: {choices["square"]()}')
    if "draw" in s:
        choices["draw"]()
