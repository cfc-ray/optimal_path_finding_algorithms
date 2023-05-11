from animator import Animator
from graph import Graph
from graphics_utils import *

# window
height = 800
width = 800

# setup animation
animator = Animator(width, height)

zz = []
for i in range(9):
    zz.append(np.round(np.random.uniform(0, 10), 1))

params = {
    'height': height,
    'width': width,

    'animator': animator,

    'points': [
        Point(100,100,zz[0]), Point(150,100,zz[1]), Point(200,100,zz[2]), 
        Point(100,150,zz[3]), Point(150,150,zz[4]), Point(200,150,zz[5]),
        Point(100,200,zz[6]), Point(150,200,zz[7]), Point(200,200,zz[8])
    ],

    'edges': [
        [0, 1], [1, 2], 
        [3, 4], [4, 5], 
        [6, 7], [7, 8],
        [0, 3], [3, 6],
        [1, 4], [4, 7],
        [2, 5], [5, 8]
    ],
}


graph = Graph(params)

input("\n\npress 'enter' to exit")