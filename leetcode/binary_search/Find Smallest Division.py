import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
            print(self.sum_all(nums,10134))
            return self.find(nums,threshold,1,nums[len(nums)-1])
            
    def find(self,nums,threshold,l,r,min_val=0):
        if r>=l:
            mid=int((r+l)/2)
            if self.sum_all(nums,mid)<=threshold:
                return self.find(nums,threshold,l,mid-1,mid)
            return self.find(nums,threshold,mid+1,r,min_val)
        return min_val
    
    def sum_all(self,nums,divider):
        sums=0
        for i in nums:
            sums+=math.ceil(i/divider)
        return sums