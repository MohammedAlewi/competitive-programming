class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] += mat[i][j-1] if (j-1) >= 0 else 0
                mat[i][j] += mat[i-1][j] if (i-1) >= 0 else 0
                mat[i][j] -= mat[i-1][j-1] if (j-1) >= 0 and (i-1) >= 0 else 0
                
        result = [[0]*len(mat[0]) for _ in range(len(mat))]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                r,c = min(len(mat)-1, i+K),min(len(mat[0])-1, j+K) 
                
                result[i][j] = mat[r][c] 
                
                result[i][j] -= mat[r][j-K-1] if j-K-1 >= 0 else 0 
                result[i][j] -= mat[i-K-1][c] if i-K-1 >= 0 else 0 
                
                result[i][j] += mat[i-K-1][j-K-1] if (i-K-1) >= 0 and (j-K-1 >= 0) else 0 
                
        return result
