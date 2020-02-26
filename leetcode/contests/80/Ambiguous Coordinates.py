class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        val=S[1:len(S)-1]
        
        l=[]
        ans=[]
        for i in range(1,len(val)):
            num=(val[:i],val[i:])
            
            vals= self.get_variations(num)
            l+=vals

        for i in l:
            num=val="("+i[0]+", "+i[1]+")"
            ans.append(num)
        return ans
    
    
    def  get_variations(self,num):
        left=self.generate(num[0])
        right=self.generate(num[1])
                    
        v3=[]
        for i in left:
            for j in right:
                v3.append((i,j))
                
        return list(set(v3))
    
        
    def generate(self,num):
        possible=[]
        if self.validate(num):
            possible.append(num)
        if len(num)>1:
            for i in range(1,len(num)):
                val=num[:i]+"."+num[i:]
                if self.validate(val):
                    possible.append(val)
        return possible
        
        
    def validate(self,num):
        if len(num)>1 and num[0]=="0" and num[1]!=".":
            return False
        dot=num.find('.')
        if len(num)>1 and num[-1]=="0" and dot!=-1:
            return False
                
        return True
        