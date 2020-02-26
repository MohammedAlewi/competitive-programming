from functools import *

class  FindMinPath:
    def __init__(self,grid):
        self.grid=grid

    def find_min_path(self,point):
        ans= self.do_dfs(point)
        return ans

    @lru_cache()
    def do_dfs(self,node):
        ans=None 
        right=node[0]+1,node[1]
        bottom=node[0],node[1]+1
        print(node)
        if len(self.grid[0])>right[1] and len(self.grid)>right[0]:
            ans=self.do_dfs(right)

        if len(self.grid[0])>bottom[1] and len(self.grid)>bottom[0]:
            curn=self.do_dfs(bottom)
            if ans==None: ans=curn
            else: ans=min(ans,curn)

        ans= ans+ self.grid[node[0]][node[1]] if ans!=None else self.grid[node[0]][node[1]]
        return ans


grid=[
    [4,7,8,6,4],
    [6,7,3,9,2],
    [3,8,1,2,4],
    [7,1,7,3,7]
]

s=FindMinPath(grid)
print(s.find_min_path((0,0)))