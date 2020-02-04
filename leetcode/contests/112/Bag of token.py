class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        point=0
        currentBuy=len(tokens)-1
        currentTake=0
        if len(tokens)==0 or tokens[currentTake]>P:
            return point
        while currentTake<len(tokens) and tokens[currentTake]<=P:
            point+=1
            P-=tokens[currentTake]
            currentTake+=1
            if currentTake<len(tokens) and tokens[currentTake]>P and point>0 and currentBuy>currentTake:
                point-=1
                P+=tokens[currentBuy]
                currentBuy-=1
        return point
                
        
        
        