class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return 0
        
        first_round = 0
        snd_round = 0
        
        for i in range(len(nums)):
            if i % 2 == 1:
                if  i+1 < len(nums):
                    first_round += max( nums[i] - min(nums[i-1],nums[i+1]) +1, 0 )
                else:
                    first_round += max( nums[i] - nums[i-1] +1, 0 )
            else:
                if i == 0 :
                    snd_round +=  max( nums[i] - nums[i+1] +1, 0 )
                elif 0 < i < len(nums)-1:
                    snd_round += max( nums[i] - min(nums[i-1],nums[i+1]) +1, 0 )
                else:
                    snd_round += max( nums[i] - nums[i-1] +1, 0 )
                    
        return min(first_round,snd_round)
                
        
    
    
                
        
