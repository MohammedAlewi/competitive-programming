class StockSpanner:

    def __init__(self):
        self.nums = []

    def next(self, price: int) -> int:
        pos = len(self.nums) - 1
        span = 1
        
        if len(self.nums) == 0:
            self.nums.append( (price,0) )
            return span

        while self.nums[pos][0] <= price:
            if pos == 0:
                span = len(self.nums) + 1
                break
            span += (pos - self.nums[pos][1] )
            pos = self.nums[pos][1]
            
        self.nums.append( (price,pos ) )
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
