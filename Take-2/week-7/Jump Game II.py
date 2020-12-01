class Solution:
    def jump(self, nums: List[int]) -> int:
        inc = 0 
        i = 0
        last_w = 0
        
        while i < len(nums):
            if i == len(nums) - 1:
                return inc
            
            window = i + nums[i]
            next_jump = (0,0)
            
            j = i + 1 + last_w
            
            # print(i,j,end=", ")
            while j  <= window:
                
                if j >= len(nums) - 1:
                    return inc + 1
                
                if nums[j] + j >= next_jump[0] + next_jump[1]:
                    next_jump = (nums[j],j)
                    
                j += 1
               
            i = next_jump[1]
            inc += 1
            
            last_w = window - next_jump[1]
                
        return inc
        
