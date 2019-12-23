def substr(a,b):
    x=1
    counter=0
    xes=0
    y=min([a,b])
    z=max([a,b])
    while(counter<5):
        y+=x
        xes=x
        x=xes+1
        counter+=1
        d=min([y,z])
        z=max([y,z])
        y=d
        print(z,y)
    print(counter)

def runner():
    val=input()
    for i in range(int(val)):
        ans=input()
        ans=ans.split(" ")
        substr(int(ans[0]),int(ans[1]))
# runner()

def gen(num):
    l=[]
    for i in range(1,num+1):
        l.append(i)
    return l

def cal(a,b):
    y=min([a,b])
    z=max([a,b])
    i=0
    while(True):
        l=gen(i)
        for j in range(len(l)):
            x1=z+sum(l[:j])
            x2=y+sum(l[j+1:])
            if x1==x2:
                return len(l)
        i+=1


def genCom(num):
    l=gen(num-1)
    ans=[]
    for i in range(0,num):
        for j in range(i,num):
            ans.append(l[i:j])
    for i  in l:
        ans.append([i])
    return ans

print(genCom(4))