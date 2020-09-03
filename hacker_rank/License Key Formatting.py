
def license_key_formatting(str_val,k):
    buffer=[]
    counter=0

    for i in range(len(str_val)-1,-1,-1):
        if counter<k and str_val[i]!='-':
            buffer.append(str_val[i].upper())
            counter+=1
        if counter==k:
            buffer.append('-')
            counter=0
    
    if buffer[-1]=='-':
        buffer.pop()

    buffer.reverse()
    return "".join(buffer)
    

val=license_key_formatting("2-5g-3-J",2)

print(val)
