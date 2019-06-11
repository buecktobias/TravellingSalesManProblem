import random
import sys
import time
import tkinter
from typing import Dict
from Node import Node
from Point2D import Point2D
from Edge import Edge
from tkinter import Tk
from itertools import permutations


class Graph:
    def __init__(self):
        master = Tk()
        self.__canvas = tkinter.Canvas(master, width=400, height=400)
        self.__canvas_objects = []
        self.__nodes: Dict[str, Node] = {}
        self.__edges = set([])

    def add_node(self, name, point: Point2D):
        new_node = Node(name, point)
        self.__nodes[name] = new_node

    def connect(self, node1: Node, node2: Node):
        edge = Edge(node1, node2)
        self.__edges.add(edge)
        node1.add_edge(edge)
        node2.add_edge(edge)

    def make_route(self, nodes: list):
        self.reset_edges()
        for i in range(len(nodes) - 1):
            self.connect(nodes[i], nodes[i + 1])
        return self.get_cost()

    def get_nodes_position(self, name: str) -> Point2D:
        return self.__nodes[name].get_position()

    def reset_edges(self):
        for nodes in self.__nodes.values():
            nodes.delete_edges()
        self.__edges = set([])

    def get_cost(self):
        return sum(edge.cost for edge in self.__edges)

    def distance_between(self, name1, name2):
        point1 = self.get_nodes_position(name1)
        point2 = self.get_nodes_position(name2)
        distance = point1.euclidean_distance(point2)
        return distance

    def tsp_easy(self):  # traveling salesperson
        self.make_route(list(self.__nodes.values()))

    def tsp_bruteforce(self):
        all_routes = self.all_possible_routes()
        best_route = []
        lowest_cost = sys.maxsize
        print(all_routes)
        for route in all_routes:
            print(route)
            cost = self.make_route(route)
            self.show()
            if cost < lowest_cost:
                lowest_cost = cost
                best_route = route
        self.make_route(best_route)
        self.show()

    def tsp_nearest_neighbours(self):
        nodes = list(self.__nodes.values())
        route = []
        start_node = nodes.pop()
        route.append(start_node)
        while len(nodes) > 0:
            start_node = self.get_nearest_node(start_node, nodes)
            route.append(start_node)
            nodes.remove(start_node)
        self.make_route(route)

    def add_random_nodes(self, amount_of_nodes):
        for i in range(amount_of_nodes):
            point = Point2D.random_point(400, 400)
            self.add_node(str(point), point)

    def get_nearest_node(self, from_node, nodes):
        nearest_node = None
        shortest_distance = sys.maxsize
        nodes_position = from_node.get_position()
        for node in nodes:
            distance = nodes_position.euclidean_distance(node.get_position())
            if distance < shortest_distance:
                shortest_distance = distance
                nearest_node = node
        return nearest_node

    def all_possible_routes(self):
        nodes_copy = list(self.__nodes.values())[:]
        start_node = nodes_copy.pop()
        combinations = permutations(nodes_copy, len(nodes_copy))
        new_combinations = []
        for combination in combinations:
            ls_combination = list(combination)
            ls_combination.insert(0, start_node)
            new_combinations.append(ls_combination)
        return new_combinations

    def show(self):
        for canvas_object in self.__canvas_objects:
            self.__canvas.delete(canvas_object)
        for node in self.__nodes.values():
            self.__canvas_objects.append(node.show(self.__canvas))
        for edge in self.__edges:
            self.__canvas_objects.append(edge.show(self.__canvas))
        self.__canvas.pack()
        self.__canvas.update()

