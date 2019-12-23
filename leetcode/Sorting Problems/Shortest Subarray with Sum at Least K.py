class Solution:
    def shortestSubarray(self, A, K: int) -> int:
        a=sorted(A,reverse=True)
        sums=0
        for i in a:
            if K<=sums: break
            sums+=i
        return sums if K<=sums else -1
        
