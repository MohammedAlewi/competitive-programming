
def do_dfs(arr,flag,index):
    if index==len(arr)-1:
        return set([index])

    even_jump_index=None
    odd_jump_index=None

    total_indexes=set()


    for i in range(index+1,len(arr)):
        if arr[i]>= arr[index]:
            if odd_jump_index==None: odd_jump_index=i
            elif arr[i]<arr[odd_jump_index]:
                odd_jump_index=i
        
        if not flag and arr[i]<= arr[index]:
            if even_jump_index==None: even_jump_index=i
            elif arr[i]>arr[even_jump_index]:
                even_jump_index=i

    if even_jump_index!=None:
        indexes=do_dfs(arr,True,even_jump_index)
        total_indexes=total_indexes.union(indexes)

    if odd_jump_index!=None:
        indexes=do_dfs(arr,False,odd_jump_index)
        if len(indexes):
            indexes.add(index)
        total_indexes=total_indexes.union(indexes)

    return total_indexes
    

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