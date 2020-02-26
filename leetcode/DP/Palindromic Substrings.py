class Solution:
    def countSubstrings(self, s: str) -> int:
        string=s
        s,e=0,0
        count=0
        for i in range(len(string)):
            s,e=i,i
            while s>=0 and e<len(string):
                if string[s]!=string[e]:
                    break
                if string[s]==string[e]:
                    count+=1
                s-=1
                e+=1
            s,e=i,i+1
            while s>=0 and e<len(string):
                if string[s]!=string[e]:
                    break
                if string[s]==string[e]:
                    count+=1
                s-=1
                e+=1
        return count
        

        