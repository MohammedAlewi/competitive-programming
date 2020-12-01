class Solution:
    def numDecodings(self, s: str) -> int:
        return self.calculate(s,0,{})[0]
    
    
    def calculate(self,s,i,values):
        if i in values:
            return values[i]
        
        if int(s[i]) == 0:
            return 0,False
        
        if i + 1 == len(s) and 0 <  int(s[i]) <= 26:
            return 1,True
        
        elif i + 1 == len(s):
            return 0,False
        
        elif  i + 1 > len(s):
            return 0,True
        
        
        
        total = 0
        
        s1 = self.calculate(s,i+1,values)
        
        if s1[1]:
            total+= s1[0]
        
        s2 = self.calculate(s,i+2,values)
        
        if  0 <  int(s[i]+s[i+1]) <= 26 and s2[1]:
            total += max(s2[0],1)
            
        values[i] = total, total>0
        return total, total>0
        
        
        
        
