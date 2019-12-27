def main(n,s,a,b):
    total=0
    current=1
    found=0
    x=dict()
    for i in range(n):
        x[a[i]]=i

    for i in b:
        index=x[i]+1-found
        if current-found>=index:
            total+=1
        else:
            current=index
            total+=2*(index-1)+1
        found+=1
    print(total)

def runner():
    val=input()
    for i in range(int(val)):
        ans=input()
        ans=ans.split(" ")
        b=input()
        b=b.split(" ")
        c=input()
        c=c.split(" ")
        main(int(ans[0]),int(ans[1]),b,c)
runner()
