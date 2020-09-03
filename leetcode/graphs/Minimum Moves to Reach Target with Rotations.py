from collections import namedtuple,deque;

Move=namedtuple('Move','r1 c1 r2 c2')
class Solution:
    def get_move_count(self,grid):
        start=Move(0,0,0,1)
        end=Move(len(grid)-1,len(grid)-2,len(grid)-1,len(grid)-1)

        queue=deque()
        distance={}
        
        distance[start]=0
        queue.append(start)

        while len(queue):
            move=queue.popleft()
            children=self.get_childrens(move,grid)
            for mov in children:
                if self.equals(mov,end):
                    return distance[move]+1
                queue.append(mov)
                distance[mov]=distance[move]+1
        return -1


    def get_childrens(self,move:Move,grid):
        possible_moves=[]

        moves= (Move(0,1,0,1),Move(1,0,1,0),Move(0,0,1,-1),Move(0,0,-1,1))
        
        right=self.new_move(move,moves[0])
        if self.inbound(right,len(grid)) and grid[right.r1][right.c1]==0 and grid[right.r2][right.c2]==0:
            possible_moves.append(right) 

        down=self.new_move(move,moves[1])
        if self.inbound(down,len(grid)) and grid[down.r1][down.c1]==0 and grid[down.r2][down.c2]==0:
            possible_moves.append(down) 

        cw=self.new_move(move,moves[2])
        if self.inbound(cw,len(grid)) and grid[cw.r1][cw.c1]==0 and grid[cw.r2][cw.c2]==0 and move.r1==move.r2 and grid[cw.r2][cw.c2+1]==0:
            possible_moves.append(cw) 

        ccw=self.new_move(move,moves[3])
        if self.inbound(ccw,len(grid)) and grid[ccw.r1][ccw.c1]==0 and grid[ccw.r2][ccw.c2]==0 and move.c1==move.c2 and grid[ccw.r2+1][ccw.c2]==0:
            possible_moves.append(ccw) 

        return possible_moves
            
    def new_move(self,m1,m2):
        return Move(m1.r1+m2.r1, m1.c1+m2.c1, m1.r2+m2.r2, m1.c2+m2.c2)

    def equals(self,m1,m2):
        return m1.r1==m2.r1 and m1.c1==m2.c1 and  m1.r2==m2.r2 and m1.c2==m2.c2

    def inbound(self,move,n):
        return 0<=move.r1<n and 0<=move.c1<n and 0<=move.r2<n and 0<=move.c2<n



grid = [[0,0,1,1,1,1],
        [0,0,0,0,1,1],
        [1,1,0,0,0,1],
        [1,1,1,0,0,1],
        [1,1,1,0,0,1],
        [1,1,1,0,0,0]]

print(Solution().get_move_count(grid))