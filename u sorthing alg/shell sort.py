def shell_sort(arr):
    gap=len(arr)//2
    while gap>0:
        for i in range(gap):
            do_inner_insertion_sort(arr,start,gap)
        gap=gap//2
    return arr

def do_inner_insertion_sort(arr,start,gap):
    for i in range(start+gap,len(arr),gap):
        currnet_val=arr[i]
        pos=i
        while pos>gap and arr[pos-gap]>currnet_val:
            arr[pos]=arr[pos-gap]
        arr[pos]=currnet_val

print(shell_sort([0,-9,-2,6,-3,7,1,-3,23,1,5,3]))