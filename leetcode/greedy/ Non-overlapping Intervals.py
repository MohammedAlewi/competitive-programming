class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        vals=sorted(intervals,key=lambda value:value[1])
        c,i=0,0
        total=1
        while i<len(vals):
            if vals[c][1]<=vals[i][0]:
                c=i
                total+=1
            i+=1
        return max(len(vals)-total,0)