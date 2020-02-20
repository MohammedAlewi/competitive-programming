def find_min_path(grid,cost):
    ans= do_dfs((0,0),grid,{},cost,cost)
    return ans[1]

def do_dfs(node,grid,visited,cost,original):
    if visited.get(node)!=None:
        return visited[node]

    ans=cost,0 
    right=node[0]+1,node[1]
    bottom=node[0],node[1]+1

    if len(grid[0])>right[1] and len(grid)>right[0]:
        curn=do_dfs(right,grid,visited,cost-grid[node[0]][node[1]],original)
        if curn[0]+grid[node[0]][node[1]]==cost:
            ans=cost,ans[1]+curn[1]+1

    if len(grid[0])>bottom[1] and len(grid)>bottom[0]:
        curn=do_dfs(bottom,grid,visited,cost-grid[node[0]][node[1]],original)

        if curn[0]+grid[node[0]][node[1]]==cost:
            ans=cost,ans[1]+curn[1]+1
    visited[node]= ans
    return ans


grid=[
    [4,7,1,6],
    [5,7,3,9],
    [5,2,1,2],
    [1,1,6,3]
]

print(find_min_path(grid,25))