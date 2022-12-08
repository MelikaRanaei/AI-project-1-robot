from Classes.Node import Node 
from Classes.Node import is_goal_node , succesor
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
   
   

def ucs():
    pass

def ids():
    pass
