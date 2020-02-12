import math



def sec(l,g,b):
    if l<g:
        print(l)
        return
    total=g
    mid=(math.ceil(l/2)-g)

    mid2=(math.floor(l/2)-g)

    total+=mid*g
    bad_t=mid*b
    total+=bad_t
    total+=max(mid2-bad_t,0)
    print(total)



def runner():
    val=input()
    for i in range(int(val)):
        j=input().split()
        l=int(j[0])
        g=int(j[1])
        b=int(j[2])
        sec(l,g,b)
runner()


