from Classes.Node import Node
import heapq

def BestFirstSearch(node: 'Node'):

    for i in range(4):
        node.successor(i)

    Close = []
    Open = []   # Minheap

    while Open:
        i: 'Node'
        for i in node.children:
            heapq.heappush(Open, i.g_n + i.heuristic)

        heapq.heapify(Open)

        Close.append(heapq.heappop(Open))

        node_popped: 'Node'
        node_popped = Close.pop(0)
        if node_popped.is_goal_node():
            return node_popped.last_move

        for i in range(4):
            node_popped.successor(i)

        for i in node_popped.children:
            heapq.heappush(Open, i.g_n + i.heuristic)
