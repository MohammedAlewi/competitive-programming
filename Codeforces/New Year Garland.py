    def main(a,b,c):
        l=[a,b,c]
        l.sort()
        max_val=l[-1]
        if max_val*2-sum(l)>=2:
            print("NO")
            return 
        print("YES")
     
    def runner():
        val=input()
        for i in range(int(val)):
            ans=input()
            ans=ans.split(" ")
            main(int(ans[0]),int(ans[1]),int(ans[2]))
    runner()