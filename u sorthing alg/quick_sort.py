import random

def quick_sort_unstable(arr):
    index=len(arr)//2
    if index==0:
        return arr
    pivot_point=arr[index]
    left_list=[]
    right_list=[]
    for i in range(len(arr)):
        if i==index:
            continue
        elif arr[index]>arr[i]:
            right_list.append(arr[i])
        else:
            left_list.append(arr[i])
    return quick_sort_unstable(left_list)+[pivot_point]+quick_sort_unstable(right_list)


#//-------------------------------------------------------------------------//#

def quick_sort_stable(arr):
    result= quick_helper(arr,0,len(arr)-1)
    return result

def quick_helper(arr,first,last):
    pivot= partition(arr,first,last)
    while first+1 <last:
        quick_helper(arr,first,pivot-1)
        quick_helper(arr,pivot,last)
    

def partition(arr,first_pointer,last):
    first=arr[first_pointer]
    left_pointer=first+1
    right_pointer=last

    done= False

    while not done:
        while left_pointer<last and arr[left_pointer]<=first:
            left_pointer+=1
        while  right_pointer>first_pointer and arr[right_pointer]>=first:
            right_pointer-=1
        if left_pointer>right_pointer:
            done=True
        else:
            arr[left_pointer],arr[right_pointer]=arr[right_pointer],arr[left_pointer]
    
    arr[first_pointer],arr[right_pointer]= arr[right_pointer],arr[first_pointer]
    return right_pointer

print(quick_sort_stable([0,2,1,5,3]))





