import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums=nums
        self.k=k
        heapq.heapify(self.nums)
        self.nums=heapq.nlargest(self.k, self.nums)
        heapq.heapify(self.nums)
        
    def add(self, val: int) -> int:
        if len(self.nums)==self.k and self.nums[0]<val:
            heapq.heapreplace(self.nums,val)
        elif len(self.nums)<self.k:
            heapq.heappush(self.nums,val)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)