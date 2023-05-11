import numpy as np

class Node():
    def __init__(self, x, y, z, parent=None, cost=np.inf, f=np.inf):
        self.x = x
        self.y = y
        self.z = z

        self.parent = parent
        self.cost = cost
        self.f = f

        self.optim = np.inf
        self.pessim = -np.inf

        self.visited = False

    def display_self(self):
        print(f' {self.z} ', end='')