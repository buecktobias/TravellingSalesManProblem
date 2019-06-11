from Point2D import Point2D


class Node:
    def __init__(self, name: str, point: Point2D):
        self.__name = name
        self.__point: Point2D = point
        self.__edges = set([])

    def delete_edges(self):
        self.__edges = set([])

    @property
    def amount_of_edges(self):
        return len(self.__edges)

    def add_edge(self, edge):
        self.__edges.add(edge)

    def get_position(self):
        return self.__point

    def show(self, canvas):
        return self.__point.show(canvas)

    def __repr__(self):
        return "Node at " + str(self.__point)
