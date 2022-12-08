from math import inf
from numpy import array, flip


def is_number(a):
    flag = True
    try:
        float(a)
    except ValueError:
        flag = False
    return flag


def cost_of_cells(matrix):
    row, column = len(matrix), len(matrix[0])
    temp = [[0 for i in range(column)] for i in range(row)]

    for i in range(row):
        for j in range(column):
            if not is_number(matrix[i][j]):
                if matrix[i][j] == 'x':
                    temp[i][j] = inf
                else:
                    temp[i][j] = float(matrix[i][j][:-1])
            else:
                temp[i][j] = float(matrix[i][j])
    return temp


def find(matrix, sign):
    row, column = len(matrix), len(matrix[0])
    tmp1 = []
    for j in range(column):
        tmp2 = []
        for i in range(row):
            tmp2.append(matrix[i][j])
        tmp1.append(tmp2)

    for i in range(column):
        tmp1[i] = flip(array(tmp1[i]))

    arr = []
    for i in range(column):
        for j in range(row):
            if not (is_number(tmp1[i][j]) and tmp1[i][j] == 'x'):
                if tmp1[i][j][-1] == sign:
                    arr.append((i, j))
    return arr


def heuristic(matrix):
    butter_location = find(matrix , 'b')
    goal_location = find(matrix , 'p')
    return (abs(butter_location[0]-goal_location[0])+abs(butter_location[1]-goal_location[1]))