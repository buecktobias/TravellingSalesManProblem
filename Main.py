import time
import tkinter
from tkinter import Tk

from Graph import Graph
import random
from Point2D import Point2D



def main():
    graph = Graph()

    graph.add_random_nodes(10)
    graph.tsp_bruteforce()
    graph.show()
    time.sleep(5)


if __name__ == '__main__':
    main()
