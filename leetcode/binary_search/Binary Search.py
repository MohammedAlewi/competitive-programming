class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.find(nums,target,len(nums)-1,0)
        
    def find(self,nums,target,r,l):
        if r>=l:
            mid=int((r+l)/2)
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                return self.find(nums,target,mid-1,l)
            return self.find(nums,target,r,mid+1)
                
            
        return -1