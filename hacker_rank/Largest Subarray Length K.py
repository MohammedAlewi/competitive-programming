def largest_Subarray(arr,k):
    start=0
    end=k
    max_index=0
    
    for i in range(len(arr)-k+1):
        if arr[i]>arr[max_index]:
            max_index=i

    result=[]
    for i in range(max_index,max_index+k):
        result.append(arr[i])

    return result


print(largest_Subarray([1,4,3,2,5],4))