class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        values={}
        c=self.find_max(s,values,0,len(s)-1)
        return c
    
    def find_max(self,string,values,start,end):
        if values.get((start,end))!=None:
            return values.get((start,end))
        elif start>end:
            return 0
        elif start==end:
            values[(start,end)]=1
            return 1
        elif string[start]==string[end]:
            val=2+self.find_max(string,values,start+1,end-1)
            values[(start,end)]=val
            return val
        else:
            val=max(self.find_max(string,values,start+1,end),
                   self.find_max(string,values,start,end-1))
            values[(start,end)]=val
            return val