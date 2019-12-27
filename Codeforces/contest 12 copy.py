def main(n,s,l):
    sums,i=0,0
    vals={}
    while i <len(l):
        vals[i]=int(l[i])
        sums+=int(l[i])
        if sums>s:break
        i+=1
    if sums<=s:
        print("0")
        return
    x=list(vals.values())
    m=x.index(max(x))+1
    print(m)

def runner():
    val=input()
    for i in range(int(val)):
        ans=input()
        ans=ans.split(" ")
        b=input()
        b=b.split(" ")
        main(int(ans[0]),int(ans[1]),b)
runner()
