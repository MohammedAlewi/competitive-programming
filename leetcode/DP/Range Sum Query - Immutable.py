class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.ans={}
        if len(nums)>0:
            self.ans[(0,0)]=nums[0]
        for i in range(1,len(nums)):
            self.ans[(0,i)]=self.ans[(0,i-1)]+nums[i]

    def sumRange(self, i: int, j: int) -> int:
        if i==0:
            return self.ans[(0,j)]
        return self.ans[(0,j)]-self.ans[(0,i-1)]
            

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

