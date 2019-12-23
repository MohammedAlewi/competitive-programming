class Solution:
    def isValid(self, s: str) -> bool:
        stack=list(s)
        if(len(stack)==0):return True
        d={ '{':'}','[':']','(':')' }
        ans=self.check(d,stack)
        return ans
            
    def check(self,d,stack):
        p=[]
        for i in stack:
            if  i in d.keys():p.append(i)
            elif(len(p)):
                if(i!=d[p.pop()]):return False
            else: return False
        if(len(p)):return False
        return True