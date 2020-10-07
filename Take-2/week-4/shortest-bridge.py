from collections import deque,defaultdict

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        visited = set()
        
        moves = [ (0,1),(1,0),(-1,0),(0,-1) ]
        land = []
        found = False
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]==1:
                    self.find_land( visited, land, (i,j), A )
                    found = True
                    break
            if found:
                break
                
        
        distance = defaultdict(lambda:0)
        queue = deque(land)
        
        while len(queue):
            val= queue.popleft()
            if val not in visited and A[val[0]][val[1]]==1:
                return distance[val] -1
            
            for move in moves:
                new = val[0]+move[0], move[1]+val[1]
                if self.in_bound(new,A) and new not in distance and new not in visited:
                    distance[new] = distance[val] + 1
                    queue.append(new)
        
        return 1
        
    
    def find_land(self,visited,island,node,matrix):
        if matrix[node[0]][node[1]] == 0:
            return 
        
        moves = [ (0,1),(1,0),(-1,0),(0,-1) ]
        island.append(node)
        visited.add(node)
        
        for move in moves:
            new = node[0]+move[0], node[1]+move[1]
            if new not in visited and self.in_bound(new,matrix):
                self.find_land(visited,island,new,matrix)
        
    
    def in_bound(self,node,matrix):
        return 0<=node[0]<len(matrix) and 0<=node[1]<len(matrix[0])
