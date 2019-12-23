class Solution:
    def __init__(self):
        self.ans=0
        self.vals={0:0,1:1,2:1}
    def tribonacci(self, n: int) -> int:
        if n<=2:
            if n<=0:return 0
            return 1
        if n not in self.vals.keys():
            a=self.tribonacci(n-3)        
            b=self.tribonacci(n-2)      
            c=self.tribonacci(n-1)
            self.vals[n]=a+b+c
        return self.vals[n]

        

x=Solution()
print(x.tribonacci(37))