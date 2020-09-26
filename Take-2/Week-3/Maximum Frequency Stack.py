import heapq
from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.counter = 0
        self.values = defaultdict(lambda:0)
        self.heap = []

    def push(self, x: int) -> None:
        self.values[x]+=1
        heapq.heappush( self.heap, ( -1*self.values[x], self.counter, x ) )
        self.counter-=1
        

    def pop(self) -> int:
        value = heapq.heappop(self.heap)
        self.values[value[2]]-=1
        
        return value[2]
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
