def main(n,s,a,b):
    total=0
    current=1
    found=0
    for i in b:
        if current>=len(a):index=0
        try:
            index=a[current-1:].index(i)+1-found
        except:
            index=0
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
