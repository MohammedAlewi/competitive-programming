

class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        prev=S
        if K==1:
            val=self.forone(S,K)
            return val
        else:
            f=list(S)
            f.sort()
            return "".join(f)
        
    def forone(self,S,K):
        prev=S
        results=[S]
        x=0
        while x<len(S):
            prev=prev[1:]+prev[0]
            results.append(prev)
            x+=1
        return min(results)

            
        