class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        result = self.calculate(piles,0,len(piles)-1,0,{})
        
        # print(result)
        return result[0] > result[1]
    
    
    def calculate(self,piles,i,j,turn, values):
        if (i,j) in values:
            total = [0,0]
            
            total[turn] = values[(i,j)][0]
            total[(turn + 1)% 2] = values[(i,j)][1]
            return total
            
        if i==j:
            
            total = [0,0]
            total[turn] = piles[i]
            
            return total
        
        res_1 = self.calculate(piles,i+1,j, (turn + 1)% 2, values)
        res_2 = self.calculate(piles,i,j-1, (turn + 1)% 2, values)
        
        if res_1[turn] + piles[i] > res_2[turn] + piles[j]:
            
            res_1[turn] += piles[i]    
            values[(i,j)] = [res_1[turn],res_1[(turn + 1)% 2]]
            
            return res_1
        
        
        res_2[turn] += piles[j]
        values[(i,j)] = [res_2[turn],res_2[(turn + 1)% 2]]
        
        return res_2
        
        
