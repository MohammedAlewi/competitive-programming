class Solution:
    def isValid(self, s: str) -> bool:
        stack=list(s)
        if(len(stack)==0): return True
        d={ '{':'}','[':']','(':')' }
        ans=self.check(d,stack)
        return ans==None
            
    def check(self,d,stack):
        val=stack.pop(0)
        if(val in d.keys()):
            a=self.check(d,stack)
            if(a==False):return False
            if(a!=None and d[val]==a): return None
            elif(a!=None): return False
        else : return val