from animator import Animator
from graph import Graph
from graphics_utils import *

# window
height = 800
width = 800
n = 5  # nxn grid of squares will be created

# setup animation
animator = Animator(width, height)

x0 = 400
y0 = 300
h = 70
num_neibs = 6
points = [Point(x0, y0, 0)]
for i in range(1, num_neibs + 1):
    x1 = x0 + h*np.cos(i*2*np.pi/num_neibs)
    y1 = y0 + h*np.sin(i*2*np.pi/num_neibs)
    z1 = 2*i-1
    x2 = x0 + 2*h*np.cos(i*2*np.pi/num_neibs)
    y2 = y0 + 2*h*np.sin(i*2*np.pi/num_neibs)
    z2 = 2*i
    points.append(Point(x1, y1, z1))
    points.append(Point(x2, y2, z2))

edges = []
for i in range(int(num_neibs*2)):
    edges.append([0, i+1])

edges.append([1,3])
edges.append([3,5])
edges.append([5,7])
edges.append([7,9])
edges.append([9,11])
edges.append([11,1])
edges.append([2,4])
edges.append([4,6])
edges.append([6,8])
edges.append([8,10])
edges.append([10,12])
edges.append([12,2])

params = {
    'height': height,
    'width': width,
    'n': n,

    'animator': animator,

    'points': points,
    # 'points': [Point(400, 300, 0),  
    #            Point(450, 250, 1),  Point(520, 250, 2), Point(590, 250, 3), 
    #            Point(450, 350, 4),  Point(520, 350, 5), Point(590, 350, 6), 
    #            Point(350, 350, 7),  Point(280, 350, 8),  Point(210, 350, 9),
    #            Point(350, 250, 10), Point(280, 250, 11), Point(210, 250, 12)],

    'edges': edges
    # 'edges': [[0, 1],  [1, 2],   [2, 3], 
    #           [0, 4],  [4, 5],   [5, 6],
    #           [0, 7],  [7, 8],   [8, 9],
    #           [0, 10], [10, 11], [11, 12]],
}


graph = Graph(params)

input("\n\npress 'enter' to exit")