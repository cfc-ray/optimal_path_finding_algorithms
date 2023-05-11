import time
import copy

from gridWorld import GridWorld
from utils import *

def dynamic_programming(grid:GridWorld, start=[0,0]):
    # print('starting dynamic programming...')
    solver = Solver(grid, start)

    start_time = time.time()
    solver.solve()
    end_time = np.round(time.time() - start_time, 6)

    solver.print_table(solver.lookup_tables['0'])

    cost = solver.optimal_cost
    coords_path = solver.optimal_path

    nodes_path = []
    for coords in coords_path:
        x = coords[0]
        y = coords[1]
        nodes_path.append(grid.nodes[x][y])

    return {
        'name': 'Dynamic Programming',
        'path': nodes_path,
        'cost': cost,
        'time': end_time,
        'num_expansions': solver.num_expansions
    }


class Solver():
    def __init__(self, grid:GridWorld, start):
        self.grid = grid
        self.start = start

        self.N = grid.N
        self.lookup_tables = {}

        self.num_expansions = 0

        # generate blank table
        self.blank_table = []
        for i in range(self.N):
            blank_row = []
            for j in range(self.N):
                blank_row.append([0, None])
            self.blank_table.append(blank_row)

    def solve(self):
        self.create_lookup_tables()
        self.search_lookup_tables()

    def create_lookup_tables(self):
        for t in range(self.N**2):
            if t == 0:
                prev_table = copy.deepcopy(self.blank_table)
            else:
                keyTm1 = str(t-1)
                prev_table = copy.deepcopy(self.lookup_tables[keyTm1])

            new_table = self.compute_table(prev_table, t)

            keyT = str(t)
            self.lookup_tables[keyT] = copy.deepcopy(new_table)

            if prev_table == new_table:
                break
        self.num_tables = t-1

    def compute_table(self, table, t):
        new_table = copy.deepcopy(self.blank_table)
        for i in range(self.N):
            for j in range(self.N):

                # compute rewards
                left_reward =  self.compute_reward((i,j), (i,j-1), t)
                right_reward = self.compute_reward((i,j), (i,j+1), t)
                up_reward =    self.compute_reward((i,j), (i-1,j), t)
                down_reward =  self.compute_reward((i,j), (i+1,j), t)
                stay_reward =  self.compute_reward((i,j), (i,j), t)

                # compile actions
                actions = []
                if left_reward !=  np.inf: actions.append([np.round(left_reward + table[i][j-1][0], 6),  'left'  ])
                if right_reward != np.inf: actions.append([np.round(right_reward + table[i][j+1][0], 6), 'right' ])
                if up_reward !=    np.inf: actions.append([np.round(up_reward + table[i-1][j][0], 6),    'up'    ])
                if down_reward !=  np.inf: actions.append([np.round(down_reward + table[i+1][j][0], 6),  'down'  ])
                if stay_reward !=  np.inf: actions.append([np.round(stay_reward + table[i][j][0], 6),    'stay'  ])

                best_action = [np.inf, None]
                for action in actions:
                    if action[0] < best_action[0]:
                        best_action = action
                

                new_table[i][j] = best_action
                
        self.num_expansions += self.N**2
        return new_table

    def compute_reward(self, p1, p2, t):
        x1 = p1[0]; y1 = p1[1]
        x2 = p2[0]; y2 = p2[1]

        if (x2<0) or (y2<0) or (x2>self.N-1) or (y2>self.N-1) or (abs(x2 - (self.N-1)) + abs(y2 - (self.N-1)) > t):
            return np.inf

        n1 = self.grid.nodes[x1][y1]
        n2 = self.grid.nodes[x2][y2]

        return compute_cost(n1, n2)

    def search_lookup_tables(self):
        x = self.start[0]
        y = self.start[1]
        
        start_point = self.num_tables
        self.optimal_cost = self.lookup_tables[str(self.num_tables)][x][y][0]

        path = [[x,y]]
        for i in range(start_point+1):
            cur_table = self.lookup_tables[str(start_point-i)]
            action = cur_table[x][y][1]
            if action == 'left':
                y -= 1
            elif action == 'right':
                y += 1
            elif action == 'up':
                x -= 1
            elif action == 'down':
                x += 1
            else:
                pass

            path.append([x,y])
            
            if (x == self.N-1) and (y == self.N-1):
                break

        # if (x != self.N-1) and (y != self.N-1):
        #     path.append([self.N-1, self.N-1])
        self.optimal_path = path

    def print_table(self, table):
        for row in table:
            for action in row:
                print(action, end='')
            print()
        print()
