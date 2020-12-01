import heapq
from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        
        vals = defaultdict(lambda:0)
        
        for t in tasks:
            vals[t] += 1
            
            
        for key in vals.keys():
            heapq.heappush(heap, -1*vals[key] )
            
            
        counter = 0
        
        while heap:
            buffer = []
            
            while  len(buffer) < n + 1 and len(heap):
                buffer.append( heapq.heappop(heap) )
                
            counter += len(buffer)
            length = len(buffer)
            
            while buffer:
                new = buffer.pop() + 1
                if new < 0:
                    heapq.heappush(heap,new)
                    
            if length < n+1 and len(heap):
                counter += n+1-length
                   
        return counter
            
            
        
