class Solution:
    def __init__(self):
        self.count=0
    def countSubstrings(self, string: str) -> int:
        s,e=0,0
        count=0
        # if len(string)%2==0:
        #     print(string[2:]
        #     #string=string[:len(string)/2]+" "+string[len(string)/2:]
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
        

s=Solution()
print(s.countSubstrings("abba"))