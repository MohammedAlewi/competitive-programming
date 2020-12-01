class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = 0
        max_score = 0
        
        for i in range(k):
            total += cardPoints[i]
        
        
        i,j= k - 1 ,len(cardPoints) - 1
        max_score = max(max_score, total )
        
        if k == len(cardPoints):
            return total
        
        while  len(cardPoints) - k  <= j:
            total -= cardPoints[i]
            total += cardPoints[j]
            
            i = (i - 1 + len(cardPoints)) % len(cardPoints)
            j = (j - 1 + len(cardPoints)) % len(cardPoints)
         
            max_score = max(max_score, total )
            
        return max_score
