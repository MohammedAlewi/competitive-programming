class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        count=0
        queue=collections.deque()
        visited={}
        
        for i in range(len(M)):
            for j in range(len(M)):
                node=i,j
                if visited.get(node)==None and M[node[0]][node[1]]==1:
                    self.do_dfs(M,visited,node)
                    count+=1
        return count
    
    
    def do_dfs(self,M,visited,node):
        if visited.get(node)==None:
            visited[node]=True
            if M[node[0]][node[1]]==1:
                for i in range(len(M)):
                    new=node[1],i
                    if visited.get(new)==None:
                        self.do_dfs(M,visited,new)
        
                
    