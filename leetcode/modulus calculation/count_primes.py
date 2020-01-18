class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=1: return 0
        prime = [True for i in range(n)] 
        p = 2
        while (p * p < n): 
            if (prime[p] == True): 
                for i in range(p * 2, n, p): 
                    prime[i] = False
            p += 1
        prime[0]= False
        prime[1]= False
        numbers=0
        for p in range(n): 
            if prime[p]: 
                print(p)
                numbers+=1
        return numbers

x=Solution()
print(x.countPrimes(50))