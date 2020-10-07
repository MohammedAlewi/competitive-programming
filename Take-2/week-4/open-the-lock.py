from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadlock = set(deadends)
        queue = deque(["0000"])
        visited = {}
        
        if "0000" in deadlock:
            return -1
        elif "0000" == target:
            return 0
        
        visited["0000"] = 0
        
        while len(queue):
            node = queue.popleft()
            
            for i in range(4):
                down = node[:i] + str( (10 + int(node[i]) + 1)%10 )  + node[i+1:] 
                up = node[:i] + str( (10 + int(node[i]) - 1)%10 ) + node[i+1:] 
                
                if down == target or up == target:
                    return visited[node] + 1
                
                if down not in deadlock and down not in visited:
                    visited[down] = visited[node] + 1
                    queue.append(down)
                    
                if up not in deadlock and up not in visited:
                    visited[up] = visited[node] + 1
                    queue.append(up)
                    
        return -1
                    
                
        
        
        
        
