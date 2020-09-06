class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = self.getValues(rowIndex+1)
        return result
        
    def getValues(self,rowIndex):
        if rowIndex<=1:
            return [1]
        
        prev = self.getValues(rowIndex-1)
        
        result= [1]
        for i in range(1,len(prev)):
            result.append( prev[i-1]  + prev[i]  )
        result.append(1)
        
        return result
