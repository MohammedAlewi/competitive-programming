from collections import deque
def pic_max(arr,num,index,values={}):
    if index in values:
        return values[index]

    max_value=0
    for i in range(index+2,len(arr)):
        value=pic_max(arr,num,i,values)
        if value+ arr[index]>num:
            continue
        max_value=max(max_value,value)
    values[index]=max_value + arr[index] 
    return values[index]


def strawberries(arr,num):
    max_value=0
    values={}
    for index in range(len(arr)):
        max_value=max(pic_max(arr,num,index,values),max_value)

    return max_value


print(strawberries([50,10,20,30,40],100))

