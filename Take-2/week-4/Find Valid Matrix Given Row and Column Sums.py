class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        result = [ [ 0 for i in range(len(colSum)) ] for j in range( len(rowSum) ) ]
        
        
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                result[i][j] = min( rowSum[i], colSum[j] )
                ress = min( rowSum[i], colSum[j] )
                rowSum[i] -= ress
                colSum[j] -= ress
                
        return result
