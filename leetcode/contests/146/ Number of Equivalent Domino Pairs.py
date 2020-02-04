class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count=0
        values={}
        for i in range(0,len(dominoes)):
            dominoes[i].sort()
            if values.get(str(dominoes[i]))==None:
                values[str(dominoes[i])]=1
            else:
                values[str(dominoes[i])]+=1
                # count+=1
        for i in values.values():
            count+=i*(i-1)/2
        
        # print(values)
        return int(count)
    
        # return self.generate()
            
    
    
    def is_equal(self,dom1,dom2):
        return (dom1[0]==dom2[0] and dom1[1]==dom2[1]) or (dom1[0]==dom2[1] and dom1[0]==dom2[1])
    
    
