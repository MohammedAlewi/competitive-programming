def selection_sort_max(arr):
    for i in range(len(arr)-1,-1,-1):
        l_index=0
        for j in range(i+1): 
            if arr[j][0]>=arr[l_index][0]:
                l_index=j
        arr[i],arr[l_index]=arr[l_index],arr[i]
    return arr

def selection_sort_min(arr):
    for i in range(len(arr)):
        s_index=i
        for j in range(i,len(arr)):
            if arr[j]<arr[s_index]:
                s_index=j
        arr[i],arr[s_index]=arr[s_index],arr[i]
    return arr

print(selection_sort_max([(0,1),(1,-1),(3,2),(1,3),(3,4)]))