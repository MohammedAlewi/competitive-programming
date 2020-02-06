class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        length=len(A)
        if length<3: return 0
        buf=0
        m=None
        for i  in range(1,length):
            if A[i]>A[buf]:
                buf=i
        for i in range(buf,length):
            if A[buf]<A[i]:
                return 0
        return buf