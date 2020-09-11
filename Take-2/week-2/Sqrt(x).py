class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        curr = 1
        
        left,right=1,x
        
        
        while left <=right:
            
            mid= (left+right)//2
            
            if mid*mid > x:
                right = mid-1
            elif mid*mid == x:
                return mid
            else:
                curr = max(curr,mid)
                left = mid+1
                
                
        return curr
