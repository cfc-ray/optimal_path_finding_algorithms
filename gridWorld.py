import numpy as np

from utils import *
from node import Node

class GridWorld():
    def __init__(self, params: dict, fixed_grid=False):
        self.N = params['n']

        self.nodes = []
        self.zvals = []
        if fixed_grid: self.create_fixed_grid(fixed_grid)
        else: self.create_grid()


    def create_grid(self):
        # print('generating random grid...')
        for i in range(self.N):
            nodes_row = []
            zvals_row = []
            for j in range(self.N):
                z = np.round(np.random.uniform(0, 10), 1)
                n = Node(i, j, z)
                zvals_row.append(z)
                nodes_row.append(n)

            self.zvals.append(zvals_row)
            self.nodes.append(nodes_row)

        self.nodes[0][0].cost = 0
        self.nodes[0][0].f = 0
        self.nodes[0][0].visited = True

    def create_fixed_grid(self, grid):
        # print('building fixed grid...')
        self.zvals = grid
        for i in range(len(grid)):
            nodes_row = []
            for j in range(len(grid[i])):
                n = Node(i, j, grid[i][j])
                nodes_row.append(n)
            self.nodes.append(nodes_row)
        
        self.nodes[0][0].cost = 0
        self.nodes[0][0].f = 0
        self.nodes[0][0].visited = True

    def display_self(self):
        for row in self.nodes:
            for node in row:
                node.display_self()
            print()
        print()
