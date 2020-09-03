def do_shell_sort(arr):
    gap=len(arr)//2

    while gap>=1:

        for i in range(gap,len(arr),gap):
            element=arr[i]
            index=i
            j=i-gap

            while j>=0 and arr[j]> element:
                arr[j],arr[index]=arr[index],arr[j]
                index=j
                j-=gap
            arr[index]=element

        gap=gap//2

    return arr





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

# l=[0,-9,-2,6,-3,7,1,-3,23,1,5,3,-22]
# merge_sort(l,0,len(l))
# print(l)






def quick_sort(arr,start,end):
    i=start
    j=end
    pivot=arr[start]

    if end-start<3:
        return

    while i<j:

        while i<j and  arr[j] >pivot:
            j-=1
        if i<j and arr[j]< pivot:
            arr[i]=arr[j]
            i+=1

        while i<j and  arr[i] <pivot:
            i+=1

        if i<j and arr[i]> pivot:
            arr[j]=arr[i]
            j-=1
    
    arr[i]=pivot
    return i

def quick_helper(arr,start,end):
    if end-start<2:
        return
    pivot=quick_sort(arr,start,end)
    quick_sort(arr,start,pivot-1)
    quick_sort(arr,pivot+1,end)


l=[0,-9,-2,6,-3,7,1,-3,23,1,5,3,-22]
quick_helper(l,0,len(l)-1)
print(l)
