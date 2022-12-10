

def is_number(a):
    flag = True
    try:
        float(a)
    except ValueError:
        flag = False
    return flag


def update_matrix(matrix, move, robot):
    # Removing robot from old matrix
    Rx = robot[0]
    Ry = robot[1]
    matrix[Rx][Ry] = matrix[Rx][Ry].replace('r', '')
    next_move = (Rx + move[0], Ry + move[1])

    # Updating butter place if there was a butter in front of robot
    if not is_number(matrix[next_move[0]][next_move[1]]) and matrix[next_move[0]+move[0]][next_move[1]+move[1]] != 'x':
        Char = matrix[next_move[0]][next_move[1]][-1]
        matrix[next_move[0] + move[0]][next_move[1] + move[1]] += Char
        matrix[next_move[0]][next_move[1]] = matrix[next_move[0]][next_move[1]].replace(Char, 'r')
    # Updating robot place if there wasn't any butters in front of it
    else:
        matrix[next_move[0]][next_move[1]] += 'r'

    return matrix


def find(matrix, sign):
    row, column = len(matrix), len(matrix[0])
    tmp1 = matrix

    arr = []
    for i in range(row):
        for j in range(column):
            if not (is_number(tmp1[i][j]) and tmp1[i][j] == 'x'):
                if tmp1[i][j][-1] == sign:
                    arr.append((i, j))
    return arr


def cost_of_cells(matrix):
    row, column = len(matrix), len(matrix[0])
    temp = [[0 for i in range(column)] for i in range(row)]

    for i in range(row):
        for j in range(column):
            if not is_number(matrix[i][j]):
                if matrix[i][j] == 'x':
                    temp[i][j] = float('inf')
                else:
                    temp[i][j] = float(matrix[i][j][:-1])
            else:
                temp[i][j] = float(matrix[i][j])
    return temp


class Table:
    def __init__(self, matrix):
        self.matrix = matrix
        self.height = len(matrix)
        self.width = len(matrix[0])
        self.robot = find(matrix, 'r')[0]
        self.butters = find(matrix, 'b')
        self.goals = find(matrix, 'p')
        self.block = find(matrix, 'x')
        self.costs_matrix = cost_of_cells(matrix)

    def is_on_table(self, x, y):
        return 0 <= x < self.height and 0 <= y < self.width
