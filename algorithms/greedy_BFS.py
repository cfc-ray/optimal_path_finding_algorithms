import time

from gridWorld import GridWorld
from node import Node
from utils import *

def GBFS(graph:GridWorld, start=[0,0]):
    # print('starting greedy best-first search...')
    start_time = time.time()
    queue = [graph.nodes[start[0]][start[1]]]
    N = graph.N
    num_expansions = 0
    dummy_node = Node(0, 0, 0)

    while len(queue) > 0:
        best_node = dummy_node
        best_ind = None
        for i, node in enumerate(queue):
            if node.f < best_node.f:
                best_node = node
                best_ind = i
        current = queue.pop(best_ind)
        cur_x = current.x
        cur_y = current.y
        # print(cur_x, cur_y)

        num_expansions += 1

        if (current.x == N-1) and (current.y == N-1):
            end_time = np.round(time.time() - start_time, 6)
            path, cost = traceback_path(current)
            return {
                'name': 'Greedy Best-First Search',
                'path': path,
                'cost': cost,
                'time': end_time,
                'num_expansions': num_expansions,
            }
        
        neighbors = []
        if cur_x > 0:   neighbors.append(graph.nodes[cur_x-1][cur_y])
        if cur_y > 0:   neighbors.append(graph.nodes[cur_x][cur_y-1])
        if cur_x < N-1: neighbors.append(graph.nodes[cur_x+1][cur_y])
        if cur_y < N-1: neighbors.append(graph.nodes[cur_x][cur_y+1])

        for neighbor in neighbors:
            tentative_cost = current.cost + compute_cost(current, neighbor)
            tentative_f = ((neighbor.x - (N-1))**2 + (neighbor.y - (N-1))**2)**(1/2)
            # input(f'    tentative cost = {tentative_f}')
            if tentative_f < neighbor.f:
                neighbor.parent = current
                neighbor.cost = tentative_cost
                neighbor.f = tentative_f
                if neighbor not in queue:
                    queue.append(neighbor)


