import numpy as np
import math
import copy

from graphics_utils import *

class Vertex(Point):
    def __init__(self, x, y, z, parent, cost):
        super().__init__(x, y, z)
        self.parent = parent
        self.cost = cost
        self.f = np.inf
        self.visited = False

    def distanceTo(self, x, y, z):
        return distance(self.x, x, self.y, y, self.z, z)

    def distanceToVert(self, v):
        return self.distanceTo(v.x, v.y, v.z)

class Edge():
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        
        self.x1 = v1.x
        self.y1 = v1.y
        self.z1 = v1.z
        self.x2 = v2.x
        self.y2 = v2.y
        self.z2 = v2.z

class Graph():
    def __init__(self, params):

        self.animator = params['animator']

        # set other parameters
        self.xmin = 0
        self.xmax = params['width']
        self.ymin = 0
        self.ymax = params['height']

        self.vertices = []
        self.edges = []

        for point in params['points']:
            v = Vertex(point.x, point.y, point.z, None, np.inf)
            self.add_vertex(v)
        for edge in params['edges']:
            e = Edge(self.vertices[edge[0]], self.vertices[edge[1]])
            self.add_edge(e)
        self.display()


    def create_fixed(self):
        print('\creating grid')

    def add_vertex(self, vert):
        self.vertices.append(vert)

    def add_edge(self, edge):
        self.edges.append(edge)

    # def find_vert(self, x, y):
    #     for vert in self.vertices:
    #         if is_point_same(vert, Point(x, y)):
    #             return vert
    #     return None
    
    # def find_edge(self, v1: Vertex, v2: Vertex):
    #     for edge in self.edges:
    #         if (is_point_same(v1, edge.v1) or is_point_same(v2, edge.v1)) and (is_point_same(v1, edge.v2) or is_point_same(v2, edge.v2)):
    #                 return edge
    #     return None

    # def compute_cost(self, v1, v2):
    #     return distance(v1.x, v2.x, v1.y, v2.y, v1.z, v2.z)**2

    # def trace_back_path(self, current: Vertex):
    #     pt_seq = [current]
    #     cost = current.cost

    #     while not is_point_same(current, self.start):
    #         current = current.parent
    #         pt_seq.append(current)
        
    #     return pt_seq, cost
    
    # def display_path(self, path, color):
    #     for i in range(len(path)):
    #         vert = path[i]
    #         if i > 0:
    #             self.animator.draw_line(vert, path[i-1], color=color, width=3, flip=False)
    #     for vert in path:
    #         self.display_vertex(vert, color=color, size=20, flip=False)
    #     self.animator.flip()

    
    def display(self):
        for edge in self.edges:
            self.display_edge(edge)
        for vertex in self.vertices:
            self.display_vertex(vertex)
        self.animator.flip()

    def display_vertex(self, vertex, color=GRAPH_COLOR, size=20, flip=False):
        self.animator.draw_point(vertex, BACKGROUND_COLOR, size, flip=flip)
        self.animator.draw_point(vertex, color, size, width=3, flip=flip)
        self.animator.draw_vertex_value(vertex, [-15, -7.5], color=color, flip=flip)
        if flip:
            self.animator.flip()

    def display_edge(self, edge, color=GRAPH_COLOR, width=3, flip=False):
        self.animator.draw_edge(edge, color, width=width, flip=flip)
