from math import inf


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
    arr = []
    for i in range(row):
        for j in range(column):
            if not (is_number(matrix[i][j]) and matrix[i][j] == 'x'):
                if matrix[i][j][-1] == sign:
                    arr.append((i, j))
    return arr


def find2(matrix, sign):
    row, column = len(matrix), len(matrix[0])
    arr = []
    arr2 = []
    for i in range(row):
        for j in range(column):
            if not (is_number(matrix[i][j]) and matrix[i][j] == 'x'):
                if matrix[i][j][-1] == sign:
                    arr.append((i, j))
                    arr2.append(i)
                    arr2.append(j)
    return arr2

def heuristic(matrix):

    butter_location = find2(matrix , 'b')
    goal_location = find2(matrix , 'p')
    return (abs(butter_location[0]-goal_location[0])+abs(butter_location[1]-goal_location[1]))
    #return (abs(butter_location[0]-goal_location[0])+abs(butter_location[1]-goal_location[1]))
