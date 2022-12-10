from Classes.Table import Table
from Classes.uninformed import ucs, BFS , DFS, DLS, IDS
from Classes.Node import Node

if __name__ == "__main__":
    row, column = map(int, input().split(" "))
    matrix = []
    for i in range(row):
        matrix.append(input().split(" "))

    table = Table(matrix)
    # tree = Tree()
    node = Node(matrix, [], [], 0, 0)
    path = BFS(node)
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

"""
5 5
1 1 1 1 1
1 1 1b x 1
2p 1 1 1 1
2 2 x 1 1
1r 2 2 2 1
"""
