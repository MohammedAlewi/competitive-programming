def longest_seq(matrix):
    visited={}
    ans=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            curr=do_dfs((i,j),matrix,visited)
            if len(ans)<len(curr):
                ans=curr
    return ans

def in_bound(new_move,matrix):
    return new_move[0]<len(matrix) and new_move[0]>=0 and new_move[1]<len(matrix[1]) and new_move[1]>=0

def do_dfs(node,matrix,visited):
    if visited.get(node)!=None:
        return visited[node]

    ans=[]
    moves=(1,0),(-1,0),(0,1),(0,-1)

    for move in moves:
        new_move=node[0]+move[0],node[1]+move[1]
        if in_bound(new_move,matrix) and matrix[node[0]][node[1]]==matrix[new_move[0]][new_move[1]]+1:
            curr_ans=do_dfs(new_move,matrix,visited)
            ans = curr_ans if len(curr_ans)>len(ans) else ans

    ans = ans+[matrix[node[0]][node[1]]]
    visited[node]=ans
    return ans
        

matrix=[
    [10,13,14,21,23],
    [10,9,22,2,3],
    [12,8,1,5,4],
    [15,24,7,6,20],
    [16,17,18,19,25]
]

print(longest_seq(matrix))