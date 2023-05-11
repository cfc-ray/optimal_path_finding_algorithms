import copy

from gridWorld import GridWorld
from utils import *

from algorithms.BFS import BFS
from algorithms.DFS import DFS
from algorithms.UCS import UCS
from algorithms.Astar import Astar
from algorithms.dynamic_programming import dynamic_programming
from algorithms.greedy_BFS import GBFS

# ------ SIMULATION PARAMS --------

n = 3   # creates an nxn grid
fixed_grid = [[8.7, 6.1, 2.8, 7.2, 9.9], [8.7, 5.7, 7.8, 5.6, 6.8], [8.5, 8.0, 3.6, 3.8, 6.1], [8.0, 1.8, 4.8, 3.5, 5.0], [6.4, 3.7, 6.3, 4.2, 2.8]]

# ---------------------------------

# package params
graph_params = {
    'n': n,
}

goal = [n, n]

graph = GridWorld(graph_params)
graph.display_self()

# BFS_results = BFS(copy.deepcopy(graph))
# DFS_results = DFS(copy.deepcopy(graph))
# UCS_results = UCS(copy.deepcopy(graph))
Astar_results = Astar(copy.deepcopy(graph))
dynamic_programming_results = dynamic_programming(copy.deepcopy(graph))
GBFS_results = GBFS(copy.deepcopy(graph))

print(f'\nRESULTS for n={n}: ............')
# display_results(BFS_results)
# display_results(DFS_results)
# display_results(UCS_results)
display_results(Astar_results)
display_results(dynamic_programming_results)
display_results(GBFS_results)
print()