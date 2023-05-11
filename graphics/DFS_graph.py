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

    'points': [Point(150, 300, 0),  
               Point(250, 250, 1),  Point(320, 250, 2),   Point(390, 250, 3),  Point(460, 250, 4), 
               Point(250, 300, 5),  Point(320, 300, 6),   Point(390, 300, 7),  Point(460, 300, 8),
               Point(250, 350, 9),  Point(320, 350, 10),  Point(390, 350, 11), Point(460, 350, 12)],

    'edges': [[0, 1], [1, 2],  [2, 3],   [3, 4], 
              [0, 5], [5, 6],  [6, 7],   [7, 8],
              [0, 9], [9, 10], [10, 11], [11, 12]],
}


graph = Graph(params)

input("\n\npress 'enter' to exit")