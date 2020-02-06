class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        values={}
        for i in range(len(nums)):
            if values.get(nums[i])!=None:
                if k>=i-values.get(nums[i]):
                    return True
            values[nums[i]]=i
        return False