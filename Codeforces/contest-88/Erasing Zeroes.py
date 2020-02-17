import math


def main(val):
    ans=0
    start=None
    for i in  range(len(val)-1):
        if val[i]=='0' and val[i+1]=='1' and start!=None:
            ans+=i-start
        elif val[i]=='1' and val[i+1]=='0':
            start=i
    print(ans) 


def runner():
    val=input()
    for i in range(int(val)):
        ans=input()
        main(ans)
runner()