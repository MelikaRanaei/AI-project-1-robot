from Classes.Table import Table
from copy import deepcopy

def Action(move: 'tuple'):
    action = 0
    if move == (1, 0):  # Right
        action = (0, 1)

    elif move == (-1, 0):  # Left
        action = (0, -1)

    elif move == (0, -1):  # Down
        action = (1, 0)

    else:  # Up
        action = (-1, 0)
    return action

def calc_matrix(matrix, move):
    founded_goal = None
    action = Action(move)
    table = Table(matrix)
    robot = table.robot
    matrix[robot[0]][robot[1]] = matrix[robot[0]][robot[1]].replace('r', '')
    next_cell = (robot[0] + action[0], robot[1] + action[1])
    if matrix[next_cell[0]][next_cell[1]][-1] == 'b' and \
            matrix[next_cell[0] + action[0]][next_cell[1] + action[1]][-1] not in ['b', 'x', 'p']:
        print("fadjf;a")
        matrix[next_cell[0]][next_cell[1]] = matrix[next_cell[0]][next_cell[1]][:-1]
        matrix[next_cell[0]][next_cell[1]] += 'r'
        matrix[next_cell[0] + action[0]][next_cell[1] + action[1]] += 'b'
    elif matrix[next_cell[0]][next_cell[1]][-1] == 'b' and \
            matrix[next_cell[0] + action[0]][next_cell[1] + action[1]][-1] == 'p':
        matrix[next_cell[0]][next_cell[1]] = matrix[next_cell[0]][next_cell[1]][:-1]
        matrix[next_cell[0]][next_cell[1]] += 'r'
        matrix[next_cell[0] + action[0]][next_cell[1] + action[1]] = matrix[next_cell[0] + action[0]][next_cell[1] + action[1]][:-1]
        matrix[next_cell[0] + action[0]][next_cell[1] + action[1]] += 'b'
        founded_goal = [(next_cell[0] + action[0], next_cell[1] + action[1])]
    else:
        matrix[next_cell[0]][next_cell[1]] += 'r'

    if founded_goal is None:
        return matrix, None
    else:
        return matrix, founded_goal


class Node:
    matrix: [list]
    children: list
    last_move: list
    parent: 'Node'
    last_move: list
    children: ['Node']
    founded_goal = []

    def __init__(self, matrix, children, last_move, depth=0, g_n=0, is_visited=False, parent=None):
        self.matrix = matrix
        self.depth = depth
        self.parent = parent
        self.children = children
        self.g_n = g_n
        self.last_move = last_move
        self.is_visited = is_visited

    def is_valid_move(self, move: 'tuple'):
        action = Action(move)
        board = Table(self.matrix)

        r_x = board.robot[0]
        r_y = board.robot[1]
        next_move = (r_x + action[0], r_y + action[1])
        if board.is_on_table(next_move[0], next_move[1]):
            if next_move not in board.block:
                if next_move in board.butters:
                    if not (
                                ((r_x + 2*action[0], r_y + 2*action[1]) in board.butters) or
                                ((r_x + 2*action[0], r_y + 2*action[1]) in board.block) or
                                (not board.is_on_table(r_x + 2*action[0], r_y + 2*action[1]))
                            ):
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False
        return False

    def move(self, move, last_move):
        action = Action(move)
        table = Table(self.matrix.copy())
        robot = table.robot
        cost = table.costs_matrix[robot[0] + action[0]][robot[1] + action[1]]
        new_g_n = self.g_n + cost
        depth = self.depth + 1
        board, found_goal = calc_matrix(deepcopy(self.matrix), move)
        if found_goal is not None:
            self.founded_goal.extend(found_goal)
        last_move.append(move)
        node = Node(board, [], last_move, depth, new_g_n, False, self)
        self.children.append(node)

    def successor(self, ind):
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.is_visited = True
        if self.last_move is None:
            last_move = []
        else:
            last_move = self.last_move.copy()
        # print("initial_matrix: ", self.matrix)
        # if ind == 2:
        #     print("in upward move: ", self.is_valid_move(moves[ind], mat))
        if self.is_valid_move(moves[ind]):
            self.move(moves[ind], last_move)
            print(moves[ind], ": ", self.children[-1].matrix)

    def is_goal_node(self):
        table = Table(deepcopy(self.matrix))
        butters = table.butters

        if len(butters) > len(self.founded_goal):
            count = 0
            if len(self.founded_goal) and len(butters):
                for i in self.founded_goal:
                    if i in butters:
                        count += 1
                if count == len(self.founded_goal):
                    return True
            else:
                return False

        elif len(butters) <= len(self.founded_goal):
            count = 0
            if len(butters) and len(self.founded_goal):
                for i in butters:
                    if i in self.founded_goal:
                        count += 1
                if count == len(butters):
                    return True
            else:
                return False
        else:
            return False

    

