class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited={}
        queue=[]
        count=0
        moves=[(1,0),(-1,0),(0,-1),(0,1)]
        for x in range(1,len(grid)-1):
            for y in range(1,len(grid[0])-1):
                if grid[x][y]==0 and visited.get((x,y))==None:  
                    queue.append((x,y))
                    visited[(x,y)]=True
                    if self.do_bfs(queue,visited,moves,grid):
                        count+=1
        return count
    
    def do_bfs(self,queue,visited,moves,grid):
        closed=True
        while len(queue):
            x,y=queue.pop(0)
            for i in moves:
                move=x+i[0],y+i[1]
                if move[0]<0 or move[1]<0 or move[0]>= len(grid) or move[1]>=len(grid[0]):
                    closed=False
                elif (move[0]==0 or move[1]==0) and grid[move[0]][move[1]]==0:
                    closed=False
                elif (move[0]+1==len(grid) or move[1]+1==len(grid[0])) and grid[move[0]][move[1]]==0:
                    closed=False
                elif grid[move[0]][move[1]]==0 and visited.get(move)==None:
                    queue.append(move)
                    visited[move]=True
        return closed

                    