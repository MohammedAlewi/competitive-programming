import collections
class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odd=0
        even=0
        
        for i in chips:
            if i%2==0:
                odd+=1
            else:
                even+=1
        return min(odd,even)