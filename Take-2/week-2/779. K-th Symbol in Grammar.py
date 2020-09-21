class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        k= self.generate_row(N,K)
        
        if k==2: return 1
        return 0
    
    
    def generate_row(self,n,k):
        if n < 3:
            return k
        
        prev =  2**(n-2)
        
        if k <= prev:
            return self.generate_row(n-1,k)
        
        else:
            if n%2!= 0:
                k = 2*prev - k + 1
            else:
                k-=prev
                prev/=2
                
                k = 2*prev - k + 1  if (k > prev)  else k
                k+= prev
            return self.generate_row(n-1,k)
            
