import heapq
import ctypes

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [i for i in primes]
        
        heapq.heapify(heap)
        heapq.heappush(heap,1)
        
        current = 2
        taken = set(primes)
        
        i = 0
        while i < n-1:
            val = heapq.heappop(heap)
            i+=1
            
            for j in primes:
                current = j*val
                if current not in taken:
                    heapq.heappush(heap, current)
                    taken.add(current)
      
        return heapq.heappop(heap)
                
                
                
