import math

class KthLargest:
    def __init__(self, k: int, nums):
        self.k=k
        self.nums=nums   # right i*2+2
        self.heap=[]     # left i*2+1
        
    def heapify(self,index,nums):
        largest=index
        l=2*index+1;
        r=2*index+2
        if r<len(nums)-1 and nums[r]>nums[largest]:
            largest=r
        if l<len(nums)-1 and nums[l]>nums[largest]:
            largest=l
        if largest!=index:
            nums[index],nums[largest]=nums[largest],nums[index]
            self.heapify(largest,nums)


    def heapSort(self,nums):
        i=len(nums)//2-1
        while i>=0:
            self.heapify(i,nums)
            i-=1
        # self.heapify(len(nums)//2,nums)
        # x=nums.pop()
        # nums=[x]+nums
        # while i>=0:
        #     self.heapify(i,nums)
        #     i-=1
        # self.heapify(len(nums)//2,nums)
        return nums



nums=[6,3,2,1,7,6,8,9,10,12,14]
x=KthLargest(3,nums)

print(x.heapSort(nums))