# from asyncio import  Queue
from multiprocessing import Queue
from Classes.Node import Node
from Classes.Table import Table



def BFS(node: 'Node'):

    queue = [node]
    while queue:
        node = queue.pop(0)

        if node.is_goal_node():
            return node.last_move

        for i in range(4):
            node.successor(i)

        queue.extend(node.children)
        
    print("THERE=IS=NO=GOAL=NODE")
    return -1          
                
                
            
def DFS(node: 'Node'):

    stack = [node]
    while queue:
        node = stack.pop()

        if node.is_goal_node():
            return node.last_move

        for i in range(4):
            node.successor(i)

        stack.extend(node.children)
        
    print("THERE=IS=NO=GOAL=NODE")
    return -1 


def ucs(initial_node: Node, table: Table):
    ucs_Q = Queue()
    ucs_Q.put(initial_node)
    visited = []
    while not ucs_Q.empty():
        popped_node = ucs_Q.get()
        visited.append(popped_node)

        print(popped_node.robot)
        popedlist = popped_node.successor(popped_node, table)

        for child in popedlist:
            # if child[0][0].is_visited:
            #     continue
            if child[0] not in visited:
                ucs_Q.put(child[0])
                # total_cost = cost + tree.get_cost(child, child[0])
                print(child)


def ids():
    pass
