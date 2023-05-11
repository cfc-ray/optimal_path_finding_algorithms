import numpy as np

# define colors
BACKGROUND_COLOR= [255,255,255]
GRAPH_COLOR = [0,0,0]
OBSTACLE_COLOR = [255,0,0]
GOAL_COLOR = [0,100,0]
PATH_COLOR = [50,50,255]
BAND_COLOR = [255,255,0]

MAX_WHILE_LOOP_TIME = 5

# define other 
BIG_NUMBER = 10000000
SMALL_NUMBER = 1e-5


def distance(x1, x2, y1, y2, z1=0, z2=0):
    return ((x1-x2)**2 + (y1-y2)**2 + (z2-z1)**2)**(1/2)

def check_circle_overlap(x1, y1, r1, x2, y2, r2, offset):
    return ((x1-x2)**2 + (y1-y2)**2) <= (r1 + r2 - offset)**2

def is_point_same(pt1, pt2):
    if (pt1 is None) or (pt2 is None):
        return False
    return ((abs(pt1.x - pt2.x) < SMALL_NUMBER) and (abs(pt1.y - pt2.y) < SMALL_NUMBER))

def print_results(results):
    name = results['name']
    time = np.round(results['time'], 6)
    cost = int(results['cost'])
    print(f'{name} took {time} seconds to find a path with cost {cost}')

    path = []
    for node in results['path']:
        path.append((node.x, node.y))
    print(f'     path: {path}')

class Point():
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def distanceTo(self, x, y):
        return distance(self.x, self.y, x, y)

    def distanceToPoint(self, v):
        return self.distanceTo(v.x, v.y)
    