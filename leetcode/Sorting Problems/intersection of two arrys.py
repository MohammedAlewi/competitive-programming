class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        val=[ i for i in nums1 if (i in nums2)]
        return list(set(val))