class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        result= 0 
            
        last= len(piles)//3 -1
        
        for i in range(len(piles)-2,last,-2):
            result += piles[i]
            
            
        return result
        
        
