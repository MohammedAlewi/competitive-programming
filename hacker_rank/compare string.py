def find_smallest_char(str_value):
    count=0
    small_char=None
    if len(str_value):
        small_char=str_value[0]

    for char in str_value:
        if char < small_char:
            count=1
            small_char=char
        elif char==small_char:
            count+=1
    return count

def find_greater_count(freq_values,val):
    start,end = 0,len(freq_values)-1

    while start <= end:
        mid= int((start+end)/2)
        
        if freq_values[mid]>=val:
            end= mid-1
        elif freq_values[mid]<val:
            start=mid+1

    return start

def find_freq_values(str_a,str_b):
    arr_1=str_a.split(',')
    arr_2=str_b.split(',')

    freq_1=[]
    freq_2=[]

    for val in arr_1:
        freq_1.append(find_smallest_char(val))

    for val in arr_2:
        freq_2.append(find_smallest_char(val))

    freq_1.sort()

    c=[]

    for val in freq_2:
        c.append(find_greater_count(freq_1,val))

    return c

    
str1="abcd,aabc,bd"
str2="aaa,aa"

print(find_freq_values(str1,str2))