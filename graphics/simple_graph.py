from animator import Animator
from graph import Graph
from graphics_utils import *

# window
height = 800
width = 800
n = 5  # nxn grid of squares will be created

# setup animation
animator = Animator(width, height)

params = {
    'height': height,
    'width': width,
    'n': n,

    'animator': animator,

    'points': [Point(100,100,1), Point(120,300,2), Point(400,250,3), Point(350, 70,4), Point(250,200,5)],
    'edges': [[0, 1], [0, 3], [0, 4], [1, 4], [2, 3], [3, 4]],
}


graph = Graph(params)

input("\n\npress 'enter' to exit")