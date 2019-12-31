class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations)==0:return 0
        return self.find(citations,0,len(citations)-1)
    
    def find(self,nums,l,r):
        mid=(r+l)//2
        index=len(nums)-1-mid
        if r>=l:
            val=nums[mid]
            if val==index:
                return  index
            elif val<index:
                return self.find(nums,mid+1,r)
            elif val>index:
                return self.find(nums,l,mid-1)
        return None