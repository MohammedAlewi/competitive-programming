class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        moves=[[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        queue=collections.deque()
        visited={}
        queue.append(tuple(click))
        visited[tuple(click)]=True
        
        while len(queue):
            move=queue.popleft()
            if board[move[0]][move[1]]=='M':
                continue
            bomb=0
            tmp_queue=collections.deque()
            for i in moves:
                mov=move[0]+i[0],move[1]+i[1]
                if mov[0]<0 or mov[0]>=len(board) or mov[1]<0 or mov[1]>=len(board[0]):
                    continue
                elif board[mov[0]][mov[1]]=='M':
                    bomb+=1
                elif visited.get(mov)==None:
                    # visited[mov]=True
                    tmp_queue.append(mov)
            board[move[0]][move[1]]=str(bomb) if bomb else 'B'
            if bomb:
                bomb=0
                continue
            while len(tmp_queue):
                mov=tmp_queue.popleft()
                visited[mov]=True
                queue.append(mov)
        
        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]]='X'
        return board
                    
                
            
        
        