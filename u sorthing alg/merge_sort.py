def merge_sort(arr):
    if len(arr)<=1:
        return arr
    left=merge_sort(arr[:len(arr)//2])
    right=merge_sort(arr[len(arr)//2:])
    i,j=0,0
    new=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1
    while i<len(left):
        new.append(left[i])
        i+=1

    while j<len(right):
        new.append(right[j])
        j+=1
    return new


print(merge_sort([0,-9,-2,6,-3,7,1,-3,23,1,5,3]))