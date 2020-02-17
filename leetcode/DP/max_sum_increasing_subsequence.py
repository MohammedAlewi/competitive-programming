
def explore(node,childs,visited,arr):
    current_ans=0,[]
    if node in visited:
        return visited[node]
    for i in childs[node]:
            curr=explore(i,childs,visited,arr)
            if current_ans[0]<curr[0]:
                current_ans=curr
    visited[node]=current_ans[0]+arr[node],[arr[node]]+current_ans[1]
    return visited[node]

def get_inc_childrens(arr):
    childs={}
    for i in range(len(arr)):
        childs[i]=[]
        for j in range(i,len(arr)):
            if arr[i] < arr[j]:
                childs[i].append(j)
    return childs
    

def run_dfs(arr):
    inc_childs=get_inc_childrens(arr)
    ans=0,[]

    visited_inc={}
    for i in range(len(arr)):
        current=explore(i,inc_childs,visited_inc,arr)

        if current[0]>ans[0]:
            ans=current

    return ans


arr=[0,8,4,12,2,10,6,14,1,9,5,13,3,11]


a=run_dfs(arr)
print(a)