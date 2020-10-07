from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        
        for i in range( len(board) ):
            for j in range(len(board[0])):
                
                if (i,j) not in visited and board[i][j] == 'O':
                    self.do_bfs( board, (i,j), visited)
        
        return board
    
    
        
    def do_bfs(self,board,node,visited):
        moves =[ (0,1),(0,-1), (1,0), (-1,0) ]
        queue = deque([node])
        
        visited.add(node)
        collected = [node]
        
        fill = True

        while len(queue):
            node = queue.popleft()
            
            for move in moves:
                new_move = node[0]+move[0], node[1]+move[1]
                
                if new_move in visited:
                    continue
                
                elif not self.in_bound(board,new_move):
                    fill = False
                    
                elif board[ new_move[0] ][ new_move[1] ] == "O":
                    queue.append(new_move)
                    collected.append(new_move)
                    visited.add(new_move)
                 
        if fill:
            for cell in collected:
                board[ cell[0] ][ cell[1] ] = 'X'
        
        
        return board
                
  
    
    def in_bound(self,board,new_move):
        return 0 <= new_move[0] < len(board) and 0 <= new_move[1] < len(board[0])
    
    
    
