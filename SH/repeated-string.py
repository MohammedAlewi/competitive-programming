def repeatedString(s, n):
    length=len(s)
    a_pos=[]
    for pos,i in enumerate(s):
        if i=='a':
            a_pos.append(pos+1)

    total=0

    for i in a_pos:
        total+=1
        total+=((n-i)//length)
    
    return total


s="abacac"
n=14
print(repeatedString(s,n))