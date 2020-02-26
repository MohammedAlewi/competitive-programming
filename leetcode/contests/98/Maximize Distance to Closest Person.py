import math
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        zero_distances=set()
        
        sums=0
        for i in seats:
            if i==0:
                sums+=1
            elif len(zero_distances)==0 and i==1:
                zero_distances.add(math.ceil(sums))
                sums=0
            else:
                zero_distances.add(math.ceil(sums/2))
                sums=0
        zero_distances.add(sums)
        max_distance=max(zero_distances)
        
        return max_distance
        