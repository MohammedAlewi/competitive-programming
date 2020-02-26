class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        max_tur_1=1
        possible=1
        alternate=True
        i=0
        
        while i <(len(A)-1):
            if alternate and A[i]>A[i+1]:
                possible+=1
                alternate=False
                i+=1
            elif (not alternate) and A[i]<A[i+1]:
                possible+=1
                alternate=True
                i+=1
            
            else:
                if max_tur_1<possible:
                    max_tur_1=possible
                    
                alternate= not alternate
                if A[i]==A[i+1]:
                    i+=1
                possible=1
                
        if max_tur_1<possible:
                    max_tur_1=possible
        
         
        
        return max_tur_1