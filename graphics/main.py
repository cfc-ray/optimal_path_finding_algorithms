'''
import BFS

graph = Graph(params)
graph.display()

BFS(Graph, start=x0, end=xg)

'''
import copy

from animator import Animator
from graph import Graph
from utils import *

# window
height = 1000
width = 1000
n = 5  # nxn grid of squares will be created
animate = False


params = {
    'height': height,
    'width': width,
    'n': n,
    'grid': 'grid',

    'animate': animate
}

graph_base = Graph(params)
anim = Animator(width, height, n)

