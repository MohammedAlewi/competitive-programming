import math
def medians(l1,l2):

    total=len(l1)+len(l2)
    leave= math.floor(total/2) - 1 if total%2==0 else math.floor(total/2)

    num_1=None
    num_2=None
    first= find_left_median(l1,l2,leave)
    second= find_left_median(l2,l1,leave)

    if first!=None:num_1= first 
    if second!=None:num_1= second 

    first= find_right_median(l1,l2,leave)
    second= find_right_median(l2,l1,leave)

    if first!=None:num_2= first 
    if second!=None:num_2= second 

    if num_1!=None and num_2!=None:
        return (num_1+num_2)/2 
    elif num_1!=None:
        return num_1
    elif num_2!=None:
        return num_2

def find_loc(num,l2):
    start,end=0,len(l2)-1
    while start<=end:
        mid=math.floor((start+end)/2)
        if l2[mid-1]<=num<=l2[mid]:
            return mid
        elif l2[mid-1]>num:
            end=mid-1
        elif l2[mid]<num:
            start=mid+1
    if l2[mid]<num:
        mid+=1
    return mid

def find_left_median(l1,l2,leave):
    start,end=0,len(l2)-1
    while start<=end:
        mid=math.floor((start+end)/2)
        num=find_loc(l2[mid],l1)

        left_part=num+mid

        if left_part< leave:
            start=mid+1
        elif left_part>leave:
            end=mid-1
        else:
            return l2[mid]

def find_right_median(l1,l2,leave):
    start,end=0,len(l2)-1
    while start<=end:
        mid=math.floor((start+end)/2)
        num=find_loc(l2[mid],l1)
        right_part=(len(l1)-num)+(len(l2)-mid-1)

        if right_part> leave:
            start=mid+1
        elif right_part<leave:
            end=mid-1
        else:
            return l2[mid]


def medians2(l1,l2):
    l1+=l2
    l1.sort()
    if len(l1)%2==0:
        return l1[int(len(l1)/2)-1],l1[int(len(l1)/2)]
    else:
        return l1[int(len(l1)/2)],l1[int(len(l1)/2)]


print(medians([0],[0]))
print(medians2([0],[0]))