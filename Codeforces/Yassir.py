def main(n,a):
    d=[]
    neg=[]
    sums=0
    f=0
    for i in range(int(n)):
        x=int(a[i])
        sums+=x
        if x<0:
            neg.append(x)
            d.append(f)
            f=0
        else:f+=x


    if len(d)!=0:
        d.append(f)
    else: d=[0]

    if max(d)>=sums:
        print("NO")
        return
    for i in range(len(d)-1):
        if d[i]+d[i+1]+neg[i]>sums:
            print("NO")
            return
    print("YES")

# x=["7", "4" ,"-1"]
# main()

def runner():
    val=input()
    for i in range(int(val)):
        n=input()
        a=input()
        a=a.split(" ")
        main(n,a)
runner()
