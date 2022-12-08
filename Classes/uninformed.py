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
   
   

def ucs(initial_node: Node , table: Table):
    ucs_Q = Queue()
    ucs_Q.put(initial_node)
    flag = True
    while not ucs_Q.empty():
        poped_node = ucs_Q.get()
        # print(poped_node.robot)
        popedlist = poped_node.successor(poped_node, table)
        for child in popedlist:
            ucs_Q.put(child[0])

def ids():
    pass
