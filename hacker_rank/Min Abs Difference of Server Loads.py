def min_abs_diff(arr):
    min_diff=float('inf')
    total=sum(arr)
    
    for i in range(len(arr)):
        curr=arr[i]

        for j in range(len(arr)):
            curr_diff= abs(abs(total-curr)-curr)
            min_diff=min(min_diff , curr_diff)

            if j==i:
                continue
            else:
                curr+=arr[j]
    
    return min_diff

print( min_abs_diff([1,4,2,3,2]) )