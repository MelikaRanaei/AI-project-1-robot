from Classes.Node import Node , is_goal_node , succesor
from Classes.Table import Table
 
        

def bfs(table:Table):
    node=Node(table.robot,table.butter)
    if is_goal_node(node,table.goals):
        return node
    
    queue=[node]
    
    while queue:
        node = queue.pop(0)
        for child in successor(node , table):
            if is_goal_node(child,table.goals):
                return child
            else:
                if child.is_visited==False:
                    queue.extend(successor(child , table))
                
    return -1  



def dfs():
    pass

def ucs():
    pass

def ids():
    pass
