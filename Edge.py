from Node import Node
import tkinter


class Edge:
    def __init__(self, node1, node2):
        self.__node1: Node = node1
        self.__node2: Node = node2

    def show(self, canvas: tkinter.Canvas):
        point1 = self.__node1.get_position()
        point2 = self.__node2.get_position()
        return canvas.create_line(point1.to_list(), point2.to_list())

    @property
    def cost(self):
        point1 = self.__node1.get_position()
        point2 = self.__node2.get_position()
        return point1.euclidean_distance(point2)
