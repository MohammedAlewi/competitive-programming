from queue import PriorityQueue
from collections import namedtuple

Pos=namedtuple('Pos','x y')

def swim_till_end(grid):
    queue=PriorityQueue()
    time=set()
    
    moves=((0,1),(1,0),(0,-1),(-1,0))

    start=Pos(0,0)
    start_cost=grid[start.x][start.y]
    end=Pos(len(grid)-1,len(grid)-1)

    queue.put((start_cost,start))
    time.add(start)

    while queue.qsize():
        curr=queue.get()
        for move in moves:
            new_move=Pos(curr[1].x+move[0],curr[1].y+move[1])

            if new_move.x==end.x and new_move.y==end.y:
                return max(grid[new_move.x][new_move.y],curr[0])
            if 0<=new_move.x<len(grid) and 0<=new_move.y<len(grid) and new_move not in time:
                cost=max(grid[new_move.x][new_move.y],curr[0])
                time.add(new_move)
                queue.put((cost,new_move))
            
grid= [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,17,20],[10,9,39,27,6]]

print(swim_till_end(grid))