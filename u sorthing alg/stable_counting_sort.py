def counting_sort(arr,n):
    sorter=[0]*(n+1)
    for i in arr:
        sorter[i]+=1
    for i in range(1,len(sorter)):
        sorter[i]+=sorter[i-1]
    sorted_arr=[0]*len(arr)
    for i in range(len(arr)):
        sorted_arr[sorter[arr[i]]-1]=arr[i]
        sorter[arr[i]]-=1

    return sorted_arr


arr=[1,4,1,2,7,5,2]

ans=counting_sort(arr,7)

print(ans)

