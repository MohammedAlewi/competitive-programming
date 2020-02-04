class Solution:
    def minimumMoves(self, grid) -> int:
        print(self.possibleMov(grid,0,0,0,1))


    def possibleMov(self,grid,tx,ty,hx,hy):
        moves=[]
        if max(tx,ty,hx,hy)<len(grid):
            #down
            if grid[tx+1][ty]==0 and grid[hx+1][hy]==0:
                x=[[tx+1,ty],[hx+1,hy]]
                moves.append(x)

            if grid[tx][ty+1]==0 and grid[hx][hy+1]==0:
                x=[[tx,ty+1],[hx,hy+1]]
                moves.append(x)
            
            if grid[tx][ty]==0 and tx-1>=0 and grid[hx+1][hy-1]==0:
                x=[[tx,ty],[hx+1,ty]]
                moves.append(x)

            # if grid[tx][ty]==0 and grid[tx][ty+2]==0:
            #     x=[[tx,ty],[tx,ty+2]]
            #     moves.append(x)
        return moves


    def applayBfs(self,graph):
        queueMov=[]
        queueMov.append((0,1))
        nodeVisited[str(queueMov[0])]=True
        while(len(queueMov)):
            current=queueMov.pop(0)
            for childNode in self.possibleMov(graph,current):
                if not nodeVisited[str(childNode)]:
                    queueMov.append(childNode)
                    nodeVisited[str(childNode)]=True





x=Solution()
r=x.minimumMoves([[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]])
print(r)