def main(nums,l):
    nums=int(nums)
    values={}
    i=0
    total=0
    while i<nums//2 and total<=nums//2:
        if values.get(l[i])==None:
            values[l[i]]=1
            total+=1
        else: 
            values[l[i]]+=1
            total+=1
        i+=1
    if len(l)>i  and values.get(l[i])!=None:
        values.pop(l[i])
    if len(values.keys())<3: 
        print("0 0 0")
        return
    ans=list(values.values())
    r=[ans[0],0,0]
    i=1
    while r[0]>=r[1] and i<len(ans):
        r[1]+=ans[i]
        i+=1
    r[2]=sum(ans[i:])
    if r[0]<r[1] and r[0]<r[2]:
        print(str(r[0]),r[1],r[2])
        return
    print("0 0 0")
def runner():
    val=input()
    for i in range(int(val)):
        a=input()
        b=input()
        b=b.split(" ")
        main(a,b)
runner()
