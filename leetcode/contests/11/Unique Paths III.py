class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        possible=0
        
        
        zeros,index,end=self.get_zeros(grid)

        visited=set()
        visited.add(index)
        ans=self.do_dfs(grid,index,visited)
        
        for i in ans:
            if len(i)==zeros +2:
                possible+=1
        return possible
    
    
    
    def do_dfs(self,grid,node,visited):
        if grid[node[0]][node[1]]==2:
            return [visited]
        
        ans=[]
        moves=((0,1),(1,0),(0,-1),(-1,0))
        for move in moves:
            new_m=move[0]+node[0],move[1]+node[1]
            if new_m not in visited and 0 <= new_m[0] < len(grid) and 0 <= new_m[1] < len(grid[0]):
                if grid[new_m[0]][new_m[1]]!=-1:
                    new_set=visited.copy()
                    new_set.add(new_m)
                    curr_ans=self.do_dfs(grid,new_m,new_set)
                    ans+=curr_ans
                
        return  ans
                
        
    def get_zeros(self,grid):
        count=0
        for i in range(len(grid)):
            for j in  range(len(grid[i])):
                if grid[i][j]==0:
                    count+=1
                if  grid[i][j]==1:
                    index=i,j
                    
                if  grid[i][j]==2:
                    end=i,j
                    
        return count,index,end