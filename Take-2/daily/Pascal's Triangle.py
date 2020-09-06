class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        results = [ [1] ]
        self.getValues(numRows,results)
        return results
        
    def getValues(self,numRows,total):
        if numRows<=1:
            return 
        
        result= [1]
        
        for i in range(1,len(total[-1])):
            result.append( total[-1][i-1]  + total[-1][i]  )
        
        result.append(1)
        
        total.append(result)
        
        self.getValues(numRows-1,total)
