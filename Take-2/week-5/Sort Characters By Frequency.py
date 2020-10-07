import heapq
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        
        heap = []
        found = Counter(s)
            
        for key in found.keys():
            heapq.heappush(heap, (found[key],key) )
            
            
        result = [] 
        
        while heap:
            val = heapq.heappop(heap)
            for i in range(val[0]):
                result.append(val[1] )
            
        return "".join(result[::-1])
