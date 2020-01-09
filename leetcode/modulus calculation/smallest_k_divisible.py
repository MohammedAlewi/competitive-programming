class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        return self.findPrimes(K)
    
    def findPrimes(self, n: int) -> int:
        if n%2==0 or n%5==0: return -1
        
        return self.check_exist(n)
    
    def check_exist(self,n):
        num=1
        for i in range(n+1):
            if num%n==0:
                return len(str(num))
            num=num*10+1
        return -1
            