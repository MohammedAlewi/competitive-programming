class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        visited=set()
        if grid[0][0]>0:
            visited.add((0,0))
            positive_nums=self.do_dfs(grid,(0,0),visited)
        positive_nums=len(visited)
        total_num= len(grid[0])*len(grid) -positive_nums
        
        return total_num
    
    def do_dfs(self,grid,node,visited):
        childs= [(node[0]+1,node[1]), (node[0],node[1]+1)]
        count=0
        for new_node in childs:
            if new_node not in visited and new_node[0]<len(grid) and new_node[1]<len(grid[0]) and grid[new_node[0]][new_node[1]]>=0:
                count+=1
                visited.add(new_node)
                count+= self.do_dfs(grid,new_node,visited)
        return count
                