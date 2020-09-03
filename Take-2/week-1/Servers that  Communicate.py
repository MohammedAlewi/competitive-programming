from collections import deque,defaultdict
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row= defaultdict(lambda:[0 ,(0,0) ] )
        col= defaultdict(lambda:0)
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    row[r][0] +=1
                    col[c] +=1
                    row[r][1] = (r,c)
                

        
        servers = 0
        

        for i in row:
            
            if row[i][0]>1:
                servers+= row[i][0]
                
            else:
                server= row[i][1][1]
                if col[server] > 1:
                    servers += 1
                    
        return servers
                
                
        