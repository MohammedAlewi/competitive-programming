class Solution:
    def rob(self, nums: List[int]) -> int:
        nums=[0,0,0]+nums
        max_val= 0
        for i in range(2,len(nums)):
            nums[i]=max(nums[i]+nums[i-2],nums[i-1])
            if nums[i]>max_val:
                max_val=nums[i]
        return max_val