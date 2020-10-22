from collections import defaultdict
import heapq

class Solution:
    def reorganizeString(self, S: str) -> str:
        
        chars = defaultdict(lambda : 0)
        heap = []
        
        for i in S:
            chars[i] += 1
            
        for item in chars.items():
            heapq.heappush( heap, (-1* item[1], item[0]) )
        
        result = []
        
        
        while len(heap) >= 2:
            first, snd = heapq.heappop(heap), heapq.heappop(heap)
            
            result.append( first[1]  )
            result.append( snd[1]  )
            
            if first[0] + 1 < 0:
                heapq.heappush(heap, (first[0] + 1, first[1]) )
                
            if snd[0] + 1 < 0:
                heapq.heappush(heap, (snd[0] + 1, snd[1]) )
            
        
        if heap and heap[0][0] + 1 < 0:
            return ""
        
        if heap:
            result.append(heap[0][1])
        
        return "".join(result)
        
