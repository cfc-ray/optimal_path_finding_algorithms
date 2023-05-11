import json
import numpy as np
from node import Node

# distance calculations
def distance(x1, x2, y1, y2, z1=0, z2=0):
    return ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**(1/2)

def distance_to_pt_2d(p1, p2):
    return distance(p1[0], p2[0], p1[1], p2[1])

def distance_to_pt_3d(p1, p2):
    return distance(p1[0], p2[0], p1[1], p2[1], p1[2], p2[2])


# GridWorld calculations
def compute_cost(p1:Node, p2:Node):
    coords1 = [p1.x, p1.y, p1.z]
    coords2 = [p2.x, p2.y, p2.z]
    return distance_to_pt_3d(coords1, coords2)**2


# path manipulation
def traceback_path(current:Node):
    cost = 0
    path = [current]
    while ((current.x != 0) or (current.y != 0)):
        cost += compute_cost(current, current.parent)
        current = current.parent
        path.append(current)

    path.reverse()
    return path, np.round(cost, 6)

def display_path(path):
    for node in path:
        node.display_self()
        if node != path[-1]: print('->', end='')
    print()

def convert_path_to_coords(nodes_path):
    coords_path = []
    for node in nodes_path:
        coords_path.append((node.x, node.y, node.z))
    return coords_path

# data display and storage
def display_results(results, print_path=False):
    name = results['name']
    time = results['time']
    cost = results['cost']
    print(f'{name} took {time} seconds to find path of cost {cost}')

    if print_path:
        print('   path:', end='')
        display_path(results['path'])


def dump_results(graph, results_list, filename):
    data = {'graph': graph.zvals}
    for results in results_list:
        name = results['name']
        for key in results.keys():
            if key == 'name': continue
            if key == 'path': results[key] = convert_path_to_coords(results[key])
            new_key = name + ' -- ' + key
            data[new_key] = results[key]

    with open(filename, 'w') as f:
        json.dump(data, f)