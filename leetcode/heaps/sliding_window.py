import heapq
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        heap=[]
        for i in range(k):
            heap.append((-1*nums[i],i))
        heapq.heapify(heap)

        output=[]

        l,r=0,k

        while r<=len(nums):
            ans=heap[0]
            if not l<=ans[1]<=r:
                heapq.heappop(heap)
                ans=heap[0]

            output.append(-1*ans[0])

            if r==len(nums):
                break
            heapq.heappush(heap,(-1*nums[r],r))
            r+=1
            l+=1
        print(output)


        


s=Solution()
s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)