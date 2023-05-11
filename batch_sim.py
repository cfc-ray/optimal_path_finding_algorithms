import copy
import json

from gridWorld import GridWorld
from utils import *

from algorithms.BFS import BFS
from algorithms.DFS import DFS
from algorithms.UCS import UCS
from algorithms.Astar import Astar
from algorithms.dynamic_programming import dynamic_programming
from algorithms.greedy_BFS import GBFS

# ------ SIMULATION PARAMS --------

num_sims = 100
n = 50   # creates an nxn grid

# ---------------------------------

graph_params = {
    'n': n,
}

results = {
    'bfs_times': [],
    'dfs_times': [],
    'ucs_times': [],
    'astar_times': [],
    'dp_times': [],
    'gbfs_times': [],

    'bfs_costs': [],
    'dfs_costs': [],
    'ucs_costs': [],
    'astar_costs': [],
    'dp_costs': [],
    'gbfs_costs': [],

    'bfs_expansions': [],
    'dfs_expansions': [],
    'ucs_expansions': [],
    'astar_expansions': [],
    'dp_expansions': [],
    'gbfs_expansions': [],
}

print(f'beginning {num_sims} simulations...')
for i in range(num_sims):
    # key = str(i)
    # if (i%10 == 0):
    print(f'  {i}/{num_sims}')
    graph = GridWorld(graph_params)
    # graph.display_self()

    BFS_results = BFS(copy.deepcopy(graph))
    DFS_results = DFS(copy.deepcopy(graph))
    GBFS_results = GBFS(copy.deepcopy(graph))
    UCS_results = UCS(copy.deepcopy(graph))
    Astar_results = Astar(copy.deepcopy(graph))
    dynamic_programming_results = dynamic_programming(copy.deepcopy(graph))

    results['bfs_times'].append(BFS_results['time'])
    results['dfs_times'].append(DFS_results['time'])
    results['gbfs_times'].append(GBFS_results['time'])
    results['ucs_times'].append(UCS_results['time'])
    results['astar_times'].append(Astar_results['time'])
    results['dp_times'].append(dynamic_programming_results['time'])

    results['bfs_costs'].append(BFS_results['cost'])
    results['dfs_costs'].append(DFS_results['cost'])
    results['gbfs_costs'].append(GBFS_results['cost'])
    results['ucs_costs'].append(UCS_results['cost'])
    results['astar_costs'].append(Astar_results['cost'])
    results['dp_costs'].append(dynamic_programming_results['cost'])

    results['bfs_expansions'].append(BFS_results['num_expansions'])
    results['dfs_expansions'].append(DFS_results['num_expansions'])
    results['gbfs_expansions'].append(GBFS_results['num_expansions'])
    results['ucs_expansions'].append(UCS_results['num_expansions'])
    results['astar_expansions'].append(Astar_results['num_expansions'])
    results['dp_expansions'].append(dynamic_programming_results['num_expansions'])


avg_bfs_time = np.round(np.mean(results['bfs_times']), 6)
avg_dfs_time = np.round(np.mean(results['dfs_times']), 6)
avg_gbfs_time = np.round(np.mean(results['gbfs_times']), 6)
avg_ucs_time = np.round(np.mean(results['ucs_times']), 6)
avg_astar_time = np.round(np.mean(results['astar_times']), 6)
avg_dp_time = np.round(np.mean(results['dp_times']), 6)

avg_bfs_cost = np.round(np.mean(results['bfs_costs']), 6)
avg_dfs_cost = np.round(np.mean(results['dfs_costs']), 6)
avg_gbfs_cost = np.round(np.mean(results['gbfs_costs']), 6)
avg_ucs_cost = np.round(np.mean(results['ucs_costs']), 6)
avg_astar_cost = np.round(np.mean(results['astar_costs']), 6)
avg_dp_cost = np.round(np.mean(results['dp_costs']), 6)

avg_bfs_expansions = np.round(np.mean(results['bfs_expansions']), 6)
avg_dfs_expansions = np.round(np.mean(results['dfs_expansions']), 6)
avg_gbfs_expansions = np.round(np.mean(results['gbfs_expansions']), 6)
avg_ucs_expansions = np.round(np.mean(results['ucs_expansions']), 6)
avg_astar_expansions = np.round(np.mean(results['astar_expansions']), 6)
avg_dp_expansions = np.round(np.mean(results['dp_expansions']), 6)

print()
print(f"BFS averages -- time: {avg_bfs_time}s, cost: {avg_bfs_cost}, expns: {avg_bfs_expansions}")
print(f"DFS averages -- time: {avg_dfs_time}s, cost: {avg_dfs_cost}, expns: {avg_dfs_expansions}")
print(f"GBFS averages -- time: {avg_gbfs_time}s, cost: {avg_gbfs_cost}, expns: {avg_gbfs_expansions}")
print(f"UCS averages -- time: {avg_ucs_time}s, cost: {avg_ucs_cost}, expns: {avg_ucs_expansions}")
print(f"Astar averages -- time: {avg_astar_time}s, cost: {avg_astar_cost}, expns: {avg_astar_expansions}")
print(f"Dyn. Prog. averages -- time: {avg_dp_time}s, cost: {avg_dp_cost}, expns: {avg_dp_expansions}")

data = {
    'avg_bfs_time': avg_bfs_time,
    'avg_dfs_time': avg_dfs_time,
    'avg_gbfs_time': avg_gbfs_time,
    'avg_ucs_time': avg_ucs_time,
    'avg_astar_time': avg_astar_time,
    'avg_dp_time': avg_dp_time,

    'avg_bfs_cost': avg_bfs_cost,
    'avg_dfs_cost': avg_dfs_cost,
    'avg_gbfs_cost': avg_gbfs_cost,
    'avg_ucs_cost': avg_ucs_cost,
    'avg_astar_cost': avg_astar_cost,
    'avg_dp_cost': avg_dp_cost,

    'avg_bfs_expansions': avg_bfs_expansions,
    'avg_dfs_expansions': avg_dfs_expansions,
    'avg_gbfs_expansions': avg_gbfs_expansions,
    'avg_ucs_expansions': avg_ucs_expansions,
    'avg_astar_expansions': avg_astar_expansions,
    'avg_dp_expansions': avg_dp_expansions,
}

filename = f'json/numsims{num_sims}_n{n}.json'
with open(filename, 'w') as f:
    json.dump(data, f)


