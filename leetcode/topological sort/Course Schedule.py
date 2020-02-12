import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n=[0]*numCourses
        preq=prerequisites
        for i in preq:
            n[i[0]]+=1
        
        queue=collections.deque()
        visited={}
        
        for i in range(numCourses):
            if n[i]==0:
                queue.append(i)
                visited[i]=set([i])
                
        if len(queue)==0:
            return False
        
        while len(queue):
            node=queue.popleft()
            childs=self.get_childs(preq,node)
            for i in childs:
                if i in visited[node]:
                    return False
                queue.append(i)
                visited[i]=set(visited[node])
                visited[i].add(i)
            if len(queue)==0:
                for i in range(numCourses):
                    if i not in visited:
                        visited[i]=set([i])
                        queue.append(i)
        return True
        
    def get_childs(self,preq,node):
        childs=[]
        for i in preq:
            if i[1]==node:
                childs.append(i[0])
        return childs