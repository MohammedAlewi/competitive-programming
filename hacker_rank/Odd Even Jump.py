
def do_dfs(arr,flag,index):
    if index==len(arr)-1:
        return set([index])

    jump_index=None
    for i in range(index+1,len(arr)):
        if flag and arr[i]>= arr[index]:
            if jump_index==None: jump_index=i
            elif arr[i]<arr[jump_index]:
                jump_index=i
        
        if not flag and arr[i]<= arr[index]:
            if jump_index==None: jump_index=i
            elif arr[i]>arr[jump_index]:
                jump_index=i

    if jump_index==None:
        return set()

    indexes=do_dfs(arr,not flag,jump_index)

    if flag and len(indexes):
        indexes.add(index)

    return indexes
    


def amount_of_jumps(arr):
    possible=set()

    for i in range(len(arr)):
        if i not in possible:
            indexes= do_dfs(arr,True,i)
            possible=possible.union(indexes)

    return len(possible)

arr= [5,1,3,4,2]
val=amount_of_jumps(arr)
print(val)