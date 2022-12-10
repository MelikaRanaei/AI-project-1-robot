from Classes.Table import Table
from Classes.uninformed import ucs, BFS
from Classes.Node import Node

if __name__ == "__main__":
    row, column = map(int, input().split(" "))
    matrix = []
    for i in range(row):
        matrix.append(input().split(" "))

    table = Table(matrix)
    # tree = Tree()
    node = Node(matrix, [], [], 0, 0)
    path = ucs(node)
    s = ""
    for i in range(len(path)):
        if path[i] == (1, 0):
            s += "R"
        elif path[i] == (-1, 0):
            s += "L"
        elif path[i] == (0, 1):
            s += "U"
        else:
            s += "D"


    #BFS(table)
    # print(table)
    # print("------------------------------------------------")
    # print("board: ")
    # print((table.board))
    # print("------------------------------------------------")
    # print("butters: ", end="")
    # print(table.butter)
    # print("------------------------------------------------")
    # print("goals: ", end="")
    # print(table.goals)
    # print("------------------------------------------------")
    # print("robot: ", end="")
    # print(table.robot)
"""
5 5
1 1 1 1 1
1 1 1b x 1
2p 1 1 1 1
2 2 x 1 1
1r 2 2 2 1
"""
