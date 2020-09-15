class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        left = 0
        right = 0
        
        nums = [ (nums[i],i) for i in range(len(nums)) ]
        nums.sort(key=lambda val:val[0])
        
        while right < len(nums):
            diff = abs( nums[left][0] - nums[right][0] )
            if diff > t:
                left +=1
                continue
                
            for i in range(right-left):
                if abs(nums[right][1] - nums[left+i][1]) <= k:
                    return True
                    
            right +=1
                

        return False
