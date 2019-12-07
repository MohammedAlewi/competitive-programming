class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            if (nums.count(target-nums[i])>0 and nums.index(target-nums[i])!=i ):
                return [i,nums.index(target-nums[i])]