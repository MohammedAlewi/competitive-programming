import collections
class Solution:
    def racecar(self, target: int) -> int:
        queue=collections.deque()
        queue.append((0,1))
        
        visited={(0,1):0}
        
        while len(queue):
            node=queue.popleft()
            
            left_move=node[0]+node[1],node[1]*2
            right_move=node[0], -1*(abs(node[1])//node[1])
            
            if left_move not in visited:
                queue.append(left_move) 
            if right_move not in visited:
                queue.append(right_move) 
                
            if left_move not in visited:
                visited[left_move]=visited[node]+1
            if right_move not in visited:
                visited[right_move]=visited[node]+1
            
            if left_move[0]==target:
                return visited[left_move]
            
            if right_move[0]==target:
                return visited[right_move]
            
              