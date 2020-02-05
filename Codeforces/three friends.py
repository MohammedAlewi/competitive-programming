    def main(l):
        x=[l[0],l[0]+1,l[0]-1]
        y=[l[1],l[1]-1,l[1]+1]
        z=[l[2],l[2]-1,l[2]+1]
        ans=[]
        for i in x:
            for j in y:
                for k in z:
                    ans.append(abs(i-j)+abs(i-k)+abs(j-k))
        print(min(ans))
     
     
    def runner():
        val=input()
        x=[]
        for i in range(int(val)):
            ans=input()
            ans=ans.split(" ")
            ans=[int(i) for i in ans]
            x.append(ans)
        for i in range(int(val)):
            main(x[i])
     
    runner()