class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        track = [0]*(n)
        i= rounds[0] -1
        track[i]+=1
        
        for k in range(1,len(rounds)):
            j = rounds[k] -1

            while j != i:
                track[j] +=1
                j= ( j + n -1 )%n
                  
            i= rounds[k] -1
                
            
        max_result = max(track)
        result= []
        for i in range(n):
            if track[i]==max_result:
                result.append(i+1)
        
        return result
                
                
            
