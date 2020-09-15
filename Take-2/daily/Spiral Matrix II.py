class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n  for i in range(n)]
        max_num = n*n
        pos = (0,0)
        
        return self.fill_matrix(matrix,n,1,pos,0 )
        
    
    def fill_matrix(self, matrix, n, current, pos, move):
        moves = [(0,1),(1,0),(0,-1),(-1,0)]
        
        if current > n*n:
            return matrix
        
        if not self.can_move(matrix,pos,n):
            pos = pos[0] - moves[move][0], pos[1] - moves[move][1]
            move = (len(moves) + move + 1) % (len(moves))
            pos = pos[0] + moves[move][0], pos[1] + moves[move][1]
            
        matrix[ pos[0] ][ pos[1] ] = current
        pos = pos[0] + moves[move][0], pos[1] + moves[move][1]
        
        return self.fill_matrix( matrix, n, current+1, pos, move)
            
        
    def can_move(self,matrix,current,n):
        return 0<=current[0] < n and 0<=current[1]<n and matrix[current[0]][current[1]]==0
        
