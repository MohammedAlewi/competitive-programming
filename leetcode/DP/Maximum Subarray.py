class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val=nums[0]
        for i in range(1,len(nums)):
            nums[i]=max(nums[i]+nums[i-1],nums[i])
            if nums[i]>max_val:
                max_val=nums[i]
        return max_val