class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        i=0
        j=0
        if len(A)==0:
            return True
            
        while i<(len(A)-1):
            if A[i]<=A[i+1]:
                i+=1
            else:
                break
        if i==len(A)-1:
            return True
        
        while j<(len(A)-1):
            if A[j]>=A[j+1]:
                j+=1
            else:
                break
        if j==len(A)-1:
            return True
        return False