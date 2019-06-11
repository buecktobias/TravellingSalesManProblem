import random
from math import sqrt
import tkinter


class Point2D:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @staticmethod
    def random_point(max_x, max_y):
        x = random.randrange(1, max_x-1)
        y = random.randrange(1, max_y-1)
        point = Point2D(x, y)
        return point

    def show(self, canvas: tkinter.Canvas):
        return canvas.create_oval(self.__x - 1, self.__y - 1, self.__x + 1, self.__y + 1)

    def to_list(self):
        return [self.x, self.y]

    def __str__(self):
        return f"Point({self.__x}, {self.__y})"

    def __repr__(self):
        return f"Point({self.__x}, {self.__y})"

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def euclidean_distance(self, other) -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
