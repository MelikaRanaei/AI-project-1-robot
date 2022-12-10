from asyncio import Queue, PriorityQueue
from multiprocessing import Queue
from Classes.Node import Node
from Classes.Table import Table



def BFS(table:Table):
    
    node=Node(table.robot,table.butter)
    
    queue=[node]
    
    while queue:
     
        node = queue.pop(0)

        if Node.is_goal_node(node,table.goals):
        
            return node
#             return node.find_path_from_source()
        else:
            node.is_visited=True
            
        Node.successor(node , table) 
        
        queue.extend(node.children_node)
         
    return -1           
                
                
            
def DFS(table:Table):
    
    node = Node(table.robot,table.butter)

    stack=[node]
    
    while stack:
     
        node = stack.pop()
        
        if Node.is_goal_node(node,table.goals):
         
            return node
#             return node.find_path_from_source()
        
        else:
            node.is_visited=True
            
        Node.successor(node , table)
        
        stack.extend(node.children_node[::-1])

    return -1

def ucs(initial_node: Node):
    ucs_Q = PriorityQueue()
    ucs_Q.put(initial_node)
    visited = []
    while not ucs_Q.empty():
        popped_node = ucs_Q.get()
        if popped_node.is_goal_node():
            return popped_node.last_move
        for i in range(4):
            child = popped_node.successor(i)
            ucs_Q.put(popped_node.g_n, child)

        # popedlist = popped_node.successor(popped_node)
        #
        # for child in popedlist:
        #     # if child[0][0].is_visited:
        #     #     continue
        #     if child[0] not in visited:
        #         ucs_Q.put(child[0])
        #         # total_cost = cost + tree.get_cost(child, child[0])
        #         print(child)


def ids():
    pass
