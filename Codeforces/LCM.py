import math
def main(num):
    x=1,num
    r=int(math.sqrt(num)) + 1
    for i in range(r,0,-1):
        val=gcd(i,num)
        if val>1 and gcd(val,int(num/val))==1:
            if max(x)>max(val,int(num/val)):
                x=val,int(num/val)
    print(x[0],x[1])
    #print(1,num)


def gcd(a,b):
    if a%b==0:return b
    return gcd(b,a%b)

def runner():
    val=input()
    main(int(val))
runner()