import json

import matplotlib.pyplot as plt
import numpy as np

GRID_WIDTH = 1.5
FIGSIZE = (8, 6)

# ------ data to import -----
num_sims = 1000

n1 = 3
n2 = 10
n3 = 20
# ---------------------------

# load data set 1
try:
    filename = 'numsims' + str(num_sims) + '_n' + str(n1) + '.json'
    with open(filename, 'r') as f:
        data1 = json.load(f)
except FileNotFoundError:
    filename = 'json/numsims' + str(num_sims) + '_n' + str(n1) + '.json'
    with open(filename, 'r') as f:
        data1 = json.load(f)

# load data set 2
try:
    filename = 'numsims' + str(num_sims) + '_n' + str(n2) + '.json'
    with open(filename, 'r') as f:
        data2 = json.load(f)
except FileNotFoundError:
    filename = 'json/numsims' + str(num_sims) + '_n' + str(n2) + '.json'
    with open(filename, 'r') as f:
        data2 = json.load(f)

# load data set 3
try:
    filename = 'numsims' + str(num_sims) + '_n' + str(n3) + '.json'
    with open(filename, 'r') as f:
        data3 = json.load(f)
except FileNotFoundError:
    filename = 'json/numsims' + str(num_sims) + '_n' + str(n3) + '.json'
    with open(filename, 'r') as f:
        data3 = json.load(f)



# plot
X = ['BFS', 'DFS', 'UCS', 'GBFS', 'Dyn. Prog.', 'A*']
X_axis = np.arange(len(X))

# times
times1 = [data1['avg_bfs_time'], data1['avg_dfs_time'], data1['avg_ucs_time'], data1['avg_gbfs_time'], data1['avg_dp_time'], data1['avg_astar_time']]
times2 = [data2['avg_bfs_time'], data2['avg_dfs_time'], data2['avg_ucs_time'], data2['avg_gbfs_time'], data2['avg_dp_time'], data2['avg_astar_time']]
times3 = [data3['avg_bfs_time'], data3['avg_dfs_time'], data3['avg_ucs_time'], data3['avg_gbfs_time'], data3['avg_dp_time'], data3['avg_astar_time']]

plt.figure(figsize=FIGSIZE)
plt.bar(X_axis-0.3, times1, width=0.3, label='n=3',  color='red',   zorder=5)
plt.bar(X_axis+0.0, times2, width=0.3, label='n=10', color='blue',  zorder=5)
plt.bar(X_axis+0.3, times3, width=0.3, label='n=20', color='green', zorder=5)
plt.title(f'Average runtime over {num_sims} simulations')
plt.ylabel('time [s]')
plt.yscale('log')
plt.xticks(X_axis, X)
plt.grid(which='major', linewidth=GRID_WIDTH, zorder=0)
plt.grid(which='minor', linewidth=GRID_WIDTH/2, zorder=0, linestyle=':')
plt.legend(loc='upper left')
plt.savefig('runtime_1000sims.png', bbox_inches='tight', dpi=500)


# costs
costs1 = [data1['avg_bfs_cost'], data1['avg_dfs_cost'], data1['avg_ucs_cost'], data1['avg_gbfs_cost'], data1['avg_dp_cost'], data1['avg_astar_cost']]
costs2 = [data2['avg_bfs_cost'], data2['avg_dfs_cost'], data2['avg_ucs_cost'], data2['avg_gbfs_cost'], data2['avg_dp_cost'], data2['avg_astar_cost']]
costs3 = [data3['avg_bfs_cost'], data3['avg_dfs_cost'], data3['avg_ucs_cost'], data3['avg_gbfs_cost'], data3['avg_dp_cost'], data3['avg_astar_cost']]

plt.clf()
plt.figure(figsize=FIGSIZE)
plt.bar(X_axis-0.3, costs1, width=0.3, label='n=3',  color='red',   zorder=5)
plt.bar(X_axis+0.0, costs2, width=0.3, label='n=10', color='blue',  zorder=5)
plt.bar(X_axis+0.3, costs3, width=0.3, label='n=20', color='green', zorder=5)
plt.title(f'Average path cost over {num_sims} simulations')
plt.ylabel('cost')
plt.xticks(X_axis, X)
# plt.ylim(0, 0.005)
plt.grid(which='major', linewidth=GRID_WIDTH, zorder=0)
plt.grid(which='minor', linewidth=GRID_WIDTH/2, zorder=0, linestyle=':')
plt.legend(loc='upper left')
plt.savefig('costs_1000sims.png', bbox_inches='tight', dpi=500)


# expansions
expansions1 = [data1['avg_bfs_expansions'], data1['avg_dfs_expansions'], data1['avg_ucs_expansions'], data1['avg_gbfs_expansions'], data1['avg_dp_expansions'], data1['avg_astar_expansions']]
expansions2 = [data2['avg_bfs_expansions'], data2['avg_dfs_expansions'], data2['avg_ucs_expansions'], data2['avg_gbfs_expansions'], data2['avg_dp_expansions'], data2['avg_astar_expansions']]
expansions3 = [data3['avg_bfs_expansions'], data3['avg_dfs_expansions'], data3['avg_ucs_expansions'], data3['avg_gbfs_expansions'], data3['avg_dp_expansions'], data3['avg_astar_expansions']]

plt.clf()
plt.figure(figsize=FIGSIZE)
plt.bar(X_axis-0.3, expansions1, width=0.3, label='n=3',  color='red',   zorder=5)
plt.bar(X_axis+0.0, expansions2, width=0.3, label='n=10', color='blue',  zorder=5)
plt.bar(X_axis+0.3, expansions3, width=0.3, label='n=20', color='green', zorder=5)
plt.title(f'Average number of node expansions over {num_sims} simulations')
plt.ylabel('# of expansions')
plt.yscale('log')
plt.xticks(X_axis, X)
# plt.ylim(0, 1000)
plt.grid(which='major', linewidth=GRID_WIDTH, zorder=0)
plt.grid(which='minor', linewidth=GRID_WIDTH/2, zorder=0, linestyle=':')
plt.legend(loc='upper left')
plt.savefig('expansions_1000sims.png', bbox_inches='tight', dpi=500)


# n = [3, 10, 20]
# bfs =   [times1[0], times2[0], times3[0]]
# dfs =   [times1[1], times2[1], times3[1]]
# ucs =   [times1[2], times2[2], times3[2]]
# gbfs =  [times1[3], times2[3], times3[3]]
# dp =    [times1[4], times2[4], times3[4]]
# astar = [times1[5], times2[5], times3[5]]


# # plt.figure(figsize=FIGSIZE)
# plt.plot(n, bfs, label='bfs')
# plt.plot(n, dfs, label='dfs')
# plt.plot(n, ucs, label='ucs')
# plt.plot(n, gbfs, label='gbfs')
# # plt.plot(n, dp, label='dp')
# plt.plot(n, astar, label='astar')
# plt.legend()
# plt.show()
