class Solution:
    def myPow(self, x: float, n: int) -> float:
        flag=n>0
        n=abs(n)
        computed={2:x*x}
        num=2
        new=num+num
        while new<n:
            computed[new]=computed[num]*computed[num]
            num=new
            new=num+num
        nums=list(computed.keys())
        index=len(nums)-1
        ans:float=1
        print(computed)
        while n>0 and index>=0:
            if n>=nums[index]:
                ans*=computed[nums[index]]
                n-=nums[index]
            elif n<nums[index]:
                index-=1
        while n>0:
            ans*=x
            n-=1
        return ans if flag else 1/ans