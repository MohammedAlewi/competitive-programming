import math
def cal(a):
    return math.factorial(a)

def found(l,i):
    indexs=[]
    for x  in range(1,i+1):
        indexs.append(l.index(str(x)))
    indexs.sort()
    result=1
    for i in range(indexs[0],indexs[len(indexs)-1]+1):
        result*=int(l[i])
    return result
    

def main(val, l):
    l=l.split()
    ans=''
    for i in range(1,int(val)+1):
        if(found(l,i)==cal(i)): ans+='1'
        else: ans+='0'
    print(ans)


def runner():
    val=input()
    l=[]
    x=[]
    for i in range(int(val)):
        ans=input()
        an2=input()
        x.append(ans)
        l.append(an2)
    for i in range(len(l)):
        main(x[i],l[i])

runner()