class Solution:
    def myPow(self, x: float, n: int) -> float:
        flag=n>0
        computed={2:x*x}
        num=2
        while num<n:
            new=num*num
            computed[new]=computed[num]*computed[num]
            num=new
        nums=list(computed.keys())
        index=len(nums)-1
        ans=1
        while n>=0 or index>=0:
            if n>nums[index] and computed.get(nums[index])!=None:
                ans*=computed[nums[index]]
                n-=nums[index]
            elif n<nums[index]:
                index-=1
        while n>=0:
            ans*=x
            n-=1
        return ans if flag else 1/ans