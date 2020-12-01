from collections import defaultdict
import heapq

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        if not matrix:
            return 0
        
        values = defaultdict(lambda:0)
        
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                if matrix[i][j] == '1':
                    values[ (i,j) ] = values[ (i,j+1) ] + 1
        
        
        max_size = 0

        for i in range(len(matrix[0])):
            heap = []
            
            for j in range(len(matrix)):
                heapq.heappush(heap, (values[ (j,i) ],j) )                    
  
            max_size = max( max_size, self.max_rec(0, len(matrix)-1, heap,{}))
            
  
        return max_size
    
    
    
    def max_rec(self,i,j,heap,values):
        if (i,j) in values:
            return values[(i,j)]
        
        if i>j:
            return 0
        
        while heap[0][1] <i or heap[0][1] > j:
            heapq.heappop(heap)
            
        rec = (j -i+1)*heap[0][0]
        point = heapq.heappop(heap)
        
        left_heap = heap.copy() 
        right_heap = heap.copy() 
    
        values[ (i,j) ] =  max( self.max_rec(i,point[1]-1,left_heap,values), self.max_rec(point[1]+1, j,right_heap,values), rec  )
        return values[ (i,j) ]
    
