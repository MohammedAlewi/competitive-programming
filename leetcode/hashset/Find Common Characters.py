class Solution:
    def commonChars(self, A):
        counts={}
        values={}
        vals=set(A[0])
        for i in A:
            vals=vals.intersection(vals,i)
        for i in vals:    
            values[i]=A[0].count(i)

        for j in range(1,len(A)):
            for i in vals:
                values[i]=min(A[j].count(i),values[i])
            
        result=[]
        for i  in values:
            result+=[i]*values[i]
        
        return result
            
            
        
        


s=Solution()
print(s.commonChars(["bella","label","roller"]))