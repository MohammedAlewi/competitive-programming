import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for i in nums:
            heapq.heappush(heap, -1*i)
            
        for i in range(1,k):
            heapq.heappop(heap)
            
        return heapq.heappop(heap) * -1
