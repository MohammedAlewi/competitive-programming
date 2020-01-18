def subPrimes(a,b):
    if abs(a-b)==1: 
        print("No")
        return
    print("YES")

def runner():
    val=input()
    for i in range(int(val)):
        ans=input()
        ans=ans.split(" ")
        subPrimes(int(ans[0]),int(ans[1]))
runner()
