class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        result = self.sum_up(nums,0,k)
        
        return result[1]
    
    
    def sum_up(self,nums,index,target):
        if index + 1 == len(nums):
            return [ nums[index] ],False
        
        values,status = self.sum_up(nums,index+1,target)
        
        if status:
            return [],True
        
        current = []
        for val in values:
            
            if target == 0 and (val + nums[index]) == 0:
                return [],True
            
            if target != 0 and (val + nums[index]) % target == 0:
                return [] , True
            
            current.append( val + nums[index] )
            
        current.append(nums[index])
        
        return current,False
        
        
