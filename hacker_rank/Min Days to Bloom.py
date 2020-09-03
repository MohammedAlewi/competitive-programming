def min_days_to_bloom(arr,k,n):
    max_days=max(arr)
    min_days=1

    while max_days > min_days:
        mid =(max_days+min_days)//2
        bq=count_blooms(arr,mid,k)

        if bq<n:
            min_days=mid+1
        else:
            max_days=mid

    return min_days

def count_blooms(arr,mid,k):
    bq=0
    buff=0
    for i in range(len(arr)):
        if arr[i]<=mid:
            buff+=1
        else:
            if buff>=k:
                bq+=1
            buff=0
            
    if buff>=k:bq+=1
    return bq


print(min_days_to_bloom( [1, 2, 4, 9, 3, 4, 1],2,2))