class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orders= {}
        for i in range(len(order)):
            orders[ order[i] ]= i
                       
                       
        for i in range(1,len(words)):
            l1= len(words[i-1])
            l2= len(words[i])
            identical = True
            
            for k in range(min(l1,l2)):
                if orders[ words[i-1][k] ] > orders[ words[i][k] ] :
                    identical = False
                    return False
                elif orders[ words[i-1][k] ] < orders[ words[i][k] ] :
                    identical = False
                    break
            if l1 > l2 and identical:
                return False
        return True               
        
            
