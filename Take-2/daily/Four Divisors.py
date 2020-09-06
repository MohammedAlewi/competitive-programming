class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        sums = 0 
        
        
        for i in nums:
            
            counter = 0
            totals = 0
            for j in range(1,math.ceil(math.sqrt(i)) ):
                
                if i % j == 0:
                    totals +=  j  +  (i//j) 
                    counter += 2
                    
            if math.sqrt(i).is_integer():
                counter += 1
                totals += int(math.sqrt(i))
           
            if counter == 4:
                sums += totals
                
                
        return sums
