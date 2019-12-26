def main(len1,coin,k,price):
    
    price.append(coin)
    price.sort()
    x=price.index(coin)
    bought=[]
    index=0
    for i in range(x-1):
        tmp=[]
        c=coin
        for j in range(i):
            print(price[x-j])
            if c>=price[x-j]:
                if j>=0:tmp.append(x-j)
                if j-1>=0:tmp.append(x-j-1)
                c-=price[x-j]
        bought.append(tmp)
    print(bought)

main(5,6,2,[2,4,3,5,7])
def runner():
    val=input()
    for i in range(int(val)):
        ans=input()
        ans=ans.split(" ")
        main(int(ans[0]),int(ans[1]))
# runner()
