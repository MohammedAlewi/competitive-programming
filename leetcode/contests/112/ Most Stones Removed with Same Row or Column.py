class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        queue=[stones[0]]
        visited={}
        visited[str(stones[0])]=True
        count=0
        f=0
        index=0
        while len(queue)!=index:
            x=queue[index]
            for stone in stones:
                if visited.get(str(stone))==None and self.ischildrens(stone,x):
                    visited[str(stone)]=True
                    queue.append(stone)
                    count+=1
                    
            index+=1  
            # if len(queue)==0:
            if len(queue)==index:
                for i in range(f,len(stones)):
                    if visited.get(str(stones[i]))==None and not self.ischildrens(stones[i],x):
                        visited[str(stones[i])]=True
                        queue.append(stones[i])
                        f=i
                        break
        return count
        
        
    def ischildrens(self,stone,current_stone):
        return stone[0]==current_stone[0] or stone[1]==current_stone[1]
        