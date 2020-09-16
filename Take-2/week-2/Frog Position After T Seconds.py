from collections import defaultdict

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        children = self.getChildren(edges)
        visited=set([1])
        return self.do_dfs(children,1,visited,t,target)[1]
        
        
    def do_dfs(self,children,node,visited,t,target):
        if t < 0:
            return False,0

        p,found = 0,0
        
        for i in children[node]:
            if i not in visited:
                visited.add(i)
                p += 1
                val = self.do_dfs(children,i,visited,t-1,target) 
                if val[0]: found = val[1]
             
        if (node == target and t == 0) or (node == target and p==0):
            return True,1
        
        prob = found /p if p>0 else 0
        return prob>0 , prob
    
        
    
    
    def getChildren(self,edges):
        childs = defaultdict(lambda:[])
        
        for edge in edges:
            childs[edge[0]].append(edge[1]) 
            childs[edge[1]].append(edge[0])            
            
        return childs
