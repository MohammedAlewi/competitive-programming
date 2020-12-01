class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums,0)
    
    
    def helper(self,nums,index):
        if index +1 == len(nums):
            return [[ nums[index] ]]
        
        result = []
        
        next_result = self.helper(nums,index+1)
        
        for values in  next_result:
            for i in range(len(values)+1):
                result.append( values[:i] + [nums[index]] + values[i:] )
                
        return result
