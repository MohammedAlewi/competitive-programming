def counting_sort(arr,index):
    val=[0]*10
    
    for i in arr:
        val[get_num(i,index)]+=1

    for i in range(1,len(val)):
        val[i]+=val[i-1]

    result=[0]*len(arr)

    for i in range(len(arr)-1,-1,-1):
        val[get_num( arr[i] ,index)]-=1
        result[val[get_num( arr[i] ,index)]]= arr[i]

    return result


def get_num(i,index):
    if len(str(i))<=index:
        return 0
    return int(str(i)[len(str(i))-1-index])



def radix_sort(arr):
    length=len(str(arr[0]))
    for i in range(length):
        arr=counting_sort(arr,i)

    return arr


arr=[1231,6111,9864,1243,2321,5436,1253,7825,2967]
val=radix_sort(arr)


print(val)