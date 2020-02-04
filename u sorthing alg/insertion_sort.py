def insertion_sort_swap(arr):
    for i in range(1,len(arr)):
        c=i
        for j in range(i):
            if arr[c]<arr[j]:
                arr[j],arr[c]=arr[c],arr[j]
                
    return arr

def insertion_sort(arr):
    for i in range(1,len(arr)):
        c=i
        currentVal=arr[i]
        while c>0 and currentVal<arr[c-1]:
            arr[c]=arr[c-1]
            c-=1
        arr[c]=currentVal
        

    return arr

print(insertion_sort([0,-9,-2,6,-3,7,1,-3,23,1,5,3]))