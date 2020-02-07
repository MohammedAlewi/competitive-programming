class Solution:
    def sumZero(self, n: int) -> List[int]:
        left=-1
        right=1
        arr=[]
        if n%2!=0:
            arr.append(0)
            n-=1
            
        while n>0:
            arr.append(left)
            arr.append(right)
            left-=1
            right+=1
            n-=2
        
        return arr
    
        