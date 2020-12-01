class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = nums[0]
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            
            if (prev + nums[i]) > nums[i]:
                max_sum = max(max_sum, (prev + nums[i]) )
                prev = (prev + nums[i])
            else:
                max_sum = max(max_sum, nums[i])
                prev = nums[i]
                
        return max_sum
        
        
