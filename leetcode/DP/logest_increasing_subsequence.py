
def explore(node,childs,visited,arr,end):
    current_ans=0,[],node
    print(node,end)
    if end!=None and node==end:
        return current_ans
    if node in visited:
        return visited[node]
    for i in childs[node]:
            curr=explore(i,childs,visited,arr,end)
            if current_ans[0]<curr[0]:
                current_ans=curr
    visited[node]=current_ans[0]+1,[arr[node]]+current_ans[1],current_ans[2]
    return visited[node]

def get_inc_childrens(arr):
    childs={}
    for i in range(len(arr)):
        childs[i]=[]
        for j in range(i,len(arr)):
            if arr[i] < arr[j]:
                childs[i].append(j)
    return childs

def get_dec_childrens(arr):
    childs={}
    for i in range(len(arr)):
        childs[i]=[]
        for j in range(i,len(arr)):
            if arr[i] > arr[j]:
                childs[i].append(j)
    return childs
    

def run_dfs(arr):
    inc_childs=get_inc_childrens(arr)
    dec_childs=get_dec_childrens(arr)
    ans=0,[]

    visited_inc={}
    visited_dec={}

    for i in range(len(arr)):
        curr_inc=explore(i,inc_childs,visited_inc,arr,None)
        curr_dec=explore(curr_inc[2],dec_childs,visited_dec,arr,None)
        current=curr_inc[0]+curr_dec[0]-1,curr_inc[1]+curr_dec[1][1:]

        curr_dec2=explore(i,dec_childs,visited_dec,arr,None)
        curr_inc2=explore(0,inc_childs,visited_inc,arr,i)
        current1=curr_inc2[0]+curr_dec2[0],curr_inc2[1]+curr_dec2[1]

        print(current,current1)
        if current[0]>ans[0]:
            ans=current

    return ans


arr=[4,2,5,9,7, 6,10,3,1]


a=run_dfs(arr)
print(a)