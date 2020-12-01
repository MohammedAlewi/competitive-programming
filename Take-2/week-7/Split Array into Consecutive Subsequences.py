from collections import Counter
import heapq

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        keys = sorted(counts.keys())
        
        found = []
        heap = []
        
        for i in keys:
            buff = []
            
            while heap:
                s = heapq.heappop(heap)
                if s[1] + 1 != i:
                    found.append(s)
                    
                elif s[2] <= counts[i]:
                    s = (s[0]+1, i, s[2])
                    
                    heapq.heappush(buff, s )
                    counts[i] -= s[2]
                    
                elif s[2] > counts[i] and counts[i] >0:
                    s2 = (s[0] + 1, i, counts[i])
                    s = (s[0], s[1], s[2] - counts[i])
                    
                    heapq.heappush(buff, s2 )
                    found.append( s )
                    
                    counts[i] = 0
                    
                else:
                    found.append(s)
                    
            if not heap and counts[i] > 0:
                heapq.heappush(buff, (1,i,counts[i]) )
            
            heap = buff
        

        while heap:
            found.append(heap.pop())
            
        total = len(found)        
        for i in found:
            if i[0] < 3: return False
            
        return total >= 1
