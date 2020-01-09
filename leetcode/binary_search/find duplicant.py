class Solution:
    def findDuplicate(self, nums) -> int:
        return self.find(nums,0,len(nums)-1)
        
    def find(self,nums,l,r):
        if r>=l:
            mid=int((r+l)/2)
            if len((nums[l:mid]))>  len(set(nums[l:mid])):
                if len(nums)<=1:return None
                elif nums[0]==nums[len(nums)-1]:
                    return nums[0]
                elif nums[mid-1]==nums[mid]:
                    return nums[mid]
                left_list=nums[l:mid-1]+nums[mid:r]
                right_list=nums[l:mid]+nums[mid+1:r]
                return self.find(left_list,0,len(left_list)) or self.find(right_list,0,len(right_list)) 
            elif len((nums[l:mid]))>len((set(nums[l:mid]))):
                return self.find(nums,l,mid)
            elif len((nums[mid:r]))>len((set(nums[mid:r]))):
                return self.find(nums,mid,r)
        return None
    
s=Solution()
print(s.findDuplicate([1,2,3,9,6,7,8,2,5]))