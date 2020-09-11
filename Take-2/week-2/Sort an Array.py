import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums,0,len(nums)-1)
        return nums
        
    def quick_sort(self,nums,left,right):
        if left <right:
            pivot = self.quick_sort_helper(nums,left,right)
            self.quick_sort(nums,left,pivot-1)
            self.quick_sort(nums,pivot+1,right)
        
    def quick_sort_helper(self,nums,left,right):  
        pivot = nums[right]
        i = left - 1
        
        for j in range(left,right):
            if nums[j] < pivot:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
                   
        nums[i+1],nums[right]=nums[right],nums[i+1]
        return i+1
                
