import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x,y):
            i,j=0,0
            max_i,max_j=0,0
            while True:
                if x[i] > y[j]:
                    return 1
                elif x[i] < y[j]:
                    return -1

                if i+1 == len(x) and j+1 == len(y):
                    return 0
                
                i= i+1 if i+1 < len(x) else max_i
                j= j+1 if j+1 < len(y) else max_j
                    
                max_i= i if max(x[i],x[max_i]) == i else max_i 
                max_j= j if max(y[j],x[max_j]) == j else max_j

        
        nums = [str(i) for i in nums ]
        nums = sorted(nums, key = functools.cmp_to_key(compare) )
        result= "".join(nums[::-1])
        
        if nums[-1] == "0":
            return "0"
        return result
    

        
        
        
        
        
