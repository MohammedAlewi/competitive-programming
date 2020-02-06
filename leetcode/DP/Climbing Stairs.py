class Solution:
    def climbStairs(self, n: int) -> int:
        return self.get_fib(n)
    
    def get_fib(self,n):
        values={}
        values[0]=1
        values[1]=1
        i=2
        while i<=n:
            values[i]=values[i-1]+values[i-2]
            i+=1
        return values[n]
            