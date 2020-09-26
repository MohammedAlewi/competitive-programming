from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a= 0 
        b= 0
        
        a_left = defaultdict(lambda:0)
        b_left = defaultdict(lambda:0)
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a+=1
            else:
                a_left[secret[i]]+=1
                b_left[guess[i]]+=1
                
        for key in b_left.keys():
            b+= min(a_left[key],b_left[key])
            
            
        
        return str(a)+"A"+str(b)+"B"
                
        
        
        
        
        
        
        
