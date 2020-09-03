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


def find_freq_values(str_a,str_b):
    arr_1=str_a.split(',')
    arr_2=str_b.split(',')

    freq_1=[0]*11

    c=[]

    for val in arr_1:
        freq_1[find_smallest_char(val)]+=1
    
    for i in range(1,len(freq_1)):
        freq_1[i]+=freq_1[i-1]

    for val in arr_2:
        val=find_smallest_char(val)-1

        c.append(freq_1[val])

    return c

    
str1="abcd,aabc,bd"
str2="aaa,aa"

print(find_freq_values(str1,str2))