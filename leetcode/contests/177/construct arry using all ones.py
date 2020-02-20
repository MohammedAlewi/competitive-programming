import math
class Solution:
    def isPossible(self, target) -> bool:
        arr=target
        total=sum(target)
        done=False
        while not done:
            max_index=self.max_value(target)
            if target[max_index]<=1:
                done=True
                continue
            new=arr[max_index]-(total-arr[max_index])
            if new <=0:
                return False
            total-=arr[max_index]
            arr[max_index]=new
            total+=arr[max_index]
        if [1]*len(target)==target:
            return True
    
    def max_value(self,arr):
        index=0
        for i in range(len(arr)):
            if arr[i]>= arr[index]:
                index=i
        return index


s=Solution()
ans=s.isPossible([9,3,5])
print(ans)