from collections import defaultdict
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        res = defaultdict(lambda:0)      
        for i in nums:
            res[i] += 1
         
        keys = sorted(res.keys())
        i, c = 0, 0
        
        while i < len(keys):
            curr = res[ keys[i] ]
            res[ keys[i] ] -= curr
            c, i = c + 1, i + 1
            n = None   
            
            while c < k:
                if i >= len(keys):    
                    return False
                
                if curr < res[ keys[i] ] and not n:
                        n = i
                
                if curr <= res[ keys[i] ] and keys[i-1] + 1 == keys[i]:
                    res[ keys[i] ] -= curr
                    c, i = c + 1, i + 1
                    
                else:
                    return False
                
            if not n: n = i
            i,c = n,0
                     
        return max(res.values()) == 0 == min(res.values())
        
        
        
                
                
