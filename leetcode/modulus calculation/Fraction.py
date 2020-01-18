import math
def gcd(a,b):
    if a%b==0:return b
    return gcd(b,a%b)

def max_irr(n):
    mid=math.ceil(n/2)
    a=mid-1
    b=n-a
    while a>0:
        if gcd(a,b)==1:
            print(a,b)
            return
        a-=1
        b=n-a

def runner():
    n=input()
    n=int(n)
    max_irr(n)

runner()