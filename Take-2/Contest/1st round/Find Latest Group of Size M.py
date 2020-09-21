class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if len(arr) == m:
            return m
        result = len(arr) - self.helper(arr,1,len(arr),len(arr)-1,m)
        
        if result < 0: 
            return -1
        return result
    
    
    
    def helper(self,arr,left,right,index,m):
        val=arr[index]
        steps= 1
        
        while val > right or val < left:
            steps+=1
            if index -1 >= 0:
                index -=1 
                val=arr[index]
            else:
                return float('inf')
        
        if val-left  == m or  right-val == m:
            return steps 

        
        left_bound =  self.helper(arr,left,val -1,index-1,m) if (val-left > m)  else float('inf')
        right_bound = self.helper(arr,val +1,right,index-1,m) if (right-val > m) else float('inf')
        
        return steps + min(left_bound,right_bound)
        
