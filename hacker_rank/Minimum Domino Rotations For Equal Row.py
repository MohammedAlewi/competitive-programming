def min_domino_rotate(arr_1,arr_2):

    val1= calculate_min(arr_1,arr_2)
    val2= calculate_min(arr_2,arr_1)

    if val1==-1:
        return val2
    if val2==-1:
        return val1

    return min(val1,val2)


def calculate_min(arr_1,arr_2):
    curr=arr_1[0]
    count=0

    for i in range(len(arr_1)):
        if arr_1[i]!=curr:
            if arr_2[i]==curr:
                count+=1
            else:
                return -1

    return count

print( min_domino_rotate([3,5,1,2,3],[3,6,3,3,4]))