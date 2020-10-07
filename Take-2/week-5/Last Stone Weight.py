import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        
        for i in stones:
            heapq.heappush(heap,-1*i)
            
        
        while len(heap)!=1:
            first,snd = heapq.heappop(heap), heapq.heappop(heap)
            
            heapq.heappush(heap, (first - snd))
            
        return heapq.heappop(heap) * -1
