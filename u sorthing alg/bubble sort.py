def buble_sort(arr):
    for j in range(len(arr)-1,-1,-1):
        for i in range(j):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr

print(buble_sort([1,5,2,9,0,-5,-7,2,0]))