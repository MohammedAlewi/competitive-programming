def find_min_path(grid):
    ans= do_dfs((0,0),grid,{})
    return ans

def do_dfs(node,grid,visited):
    if visited.get(node)!=None:
        return visited[node]

    ans=None 
    right=node[0]+1,node[1]
    bottom=node[0],node[1]+1

    if len(grid[0])>right[1] and len(grid)>right[0]:
        ans=do_dfs(right,grid,visited)

    if len(grid[0])>bottom[1] and len(grid)>bottom[0]:
        curn=do_dfs(bottom,grid,visited)
        if ans==None: ans=curn
        else: ans=min(ans,curn)

    ans= ans+ grid[node[0]][node[1]] if ans!=None else grid[node[0]][node[1]]

    visited[node]= ans
    return ans


grid=[
    [4,7,8,6,4],
    [6,7,3,9,2],
    [3,8,1,2,4],
    [7,1,7,3,7]
]

print(find_min_path(grid))