from collections import defaultdict
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix=[]
        
        for i in range(n):
            v=[float('inf')]*(n)  
            matrix.append(v)

        for i in edges:
            
            matrix[i[0]][i[1]]=i[2]
            matrix[i[1]][i[0]]=i[2]
        
        for i in range(n):
            for j in range(n):
                for k in range(j+1,n):
                    if matrix[j][i]+matrix[i][k]==float('inf') or  j==k:
                           continue
                    matrix[j][k]=min(matrix[k][j],matrix[j][i]+matrix[i][k])
                    matrix[k][j]=matrix[j][k]
                    
                    
        values=n-1
        val=n-1
        for i in range(n):
            count=0
            for j in range(n):
                if matrix[i][j]<=distanceThreshold:
                    count+=1
            if values>=count:
                values=count
                val=i
        return val