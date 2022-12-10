from Classes.Table import Table, array
from Classes.uninformed import ucs, BFS
from Classes.Node import Node

if __name__ == "__main__":
    row, column = map(int, input().split(" "))
    matrix = []
    for i in range(row):
        matrix.append(input().split(" "))

    table = Table(matrix)
    # tree = Tree()
    node = Node(table.robot, table.butter)
    ucs(node, table)
    #BFS(table)
    print(table)
    print("------------------------------------------------")
    print("board: ")
    print(array(table.board))
    print("------------------------------------------------")
    print("butters: ", end="")
    print(table.butter)
    print("------------------------------------------------")
    print("goals: ", end="")
    print(table.goals)
    print("------------------------------------------------")
    print("robot: ", end="")
    print(table.robot)
"""
5 5
1 1 1 1 1
1 1 1b x 1
2p 1 1 1 1
2 2 x 1 1
1r 2 2 2 1
"""
