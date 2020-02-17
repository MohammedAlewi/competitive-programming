def do_dfs(grid,node,visited):
    if node in visited:
        return visited[node]
    moves=[(0,1),(1,1),(1,0)]
    if node[0]>=len(grid) or node[1]>=len(grid[0]) or grid[node[0]][node[1]]==0:
        return 0
    min_val=None
    for move in moves:
        new_node = move[0]+node[0], move[1]+node[1]
        ans=do_dfs(grid,new_node,visited)
        min_val= ans if min_val==None else min(min_val,ans)
    visited[node]=min_val+1
    return min_val+1

grid=[
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]
]
visited={}
print(do_dfs(grid,(0,0),visited))


