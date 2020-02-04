class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        result=0
        for sing1 in [1,-1]:
            for sing2 in [1,-1]:
                min_val= float('inf')
                for i in range(len(arr1)):
                    curr= sing1*arr1[i] + sing2*arr2[i] +i
                    result= max(result,curr-min_val)
                    min_val= min(min_val,curr)
        return result
        
        
        