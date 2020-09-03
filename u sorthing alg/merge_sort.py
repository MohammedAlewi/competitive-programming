def merge_sort(arr,start,end):
    if start+1==end:
        return start,end

    left= merge_sort(arr,start,(start+end)//2)
    right= merge_sort(arr,(start+end)//2,end)

    i,j=left[0],right[0]
    result=[]
    while i<left[1] and j<right[1]:
        if arr[j] < arr[i]:
            result.append(arr[j])
            j+=1
        else:
            result.append(arr[i])
            i+=1

    while i<left[1] :
        result.append(arr[i])
        i+=1

    while j<right[1]:
        result.append(arr[j])
        j+=1
    
    index=0
    for i in range(left[0],right[1]):
        arr[i]=result[index]
        index+=1
    
    return left[0],right[1]

l=[0,-9,-2,6,-3,7,1,-3,23,1,5,3,-22]
merge_sort(l,0,len(l))
print(l)