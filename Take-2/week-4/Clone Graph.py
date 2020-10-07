"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = set()
        values = {}
        if not node:
            return node
        
        cloned = Node(node.val)
        values[cloned.val] = cloned
        
        visited.add(node.val)
        
        queue = deque([node])
        queue_2 = deque([cloned])
        
        while len(queue):
            node = queue.popleft()
            c_node = queue_2.popleft()
            
            for child in node.neighbors:
                new = Node(child.val)
                
                if child.val not in visited:
                    queue.append(child)
                    queue_2.append(new)
                    
                    c_node.neighbors.append(new)
                    
                    values[new.val] = new
                    visited.add(child.val)
               
                else:
                    c_node.neighbors.append(values[new.val])
                            
        return cloned
