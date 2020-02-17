import math



def sec(l,g,b):
    if g>l:
        print(l)
        return
    total=g
    mid=(math.ceil(l/2)-g)

    mid2=(math.floor(l/2))

    left_off=mid%g

    g_days=math.ceil(mid/g) 

    total+=g_days*g
    bad_t=g_days*b

    total+=bad_t
    if left_off:
        total-=(g-left_off)
    total+=max(mid2-bad_t,0)

    print(max(total,l))



def runner():
    val=input()
    for i in range(int(val)):
        j=input().split()
        l=int(j[0])
        g=int(j[1])
        b=int(j[2])
        sec(l,g,b)
runner()


