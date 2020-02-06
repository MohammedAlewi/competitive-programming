    def substr(ps,hash):
        x=0
        # j=len(hash)-1
        ps2=""
        for i in range(len(hash)):
            if check_anagram(ps,hash[x:len(ps)+x]):
                print("YES")
                return
            else :
                x+=1
        print("NO")
    def check_anagram(str1,srt2):
        x1=list(str1)
        x2=list(srt2)
        x1.sort()
        x2.sort()
        return  x1==x2
    def runner():
        val=input()
        for i in range(int(val)):
            ans=input()
            an2=input()
            substr(ans,an2)
        # substr("abacaba","zyxaabcaabkjh")
    runner()