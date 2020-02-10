class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        visited={}
        
        for i in pairs:
                self.do_dfs(i,pairs,visited)
        
        ans=max(visited.values()) if len(visited.values()) else 0
        return ans
    
    
    def do_dfs(self,node,pairs,visited):
        if visited.get(tuple(node))!=None:
            return visited[tuple(node)]
        
        distance=0
        childs=self.get_childs(pairs,node)
        for i in childs:
                val=self.do_dfs(i,pairs,visited)
                distance=max(distance,val)
                
        visited[tuple(node)]=distance+1
        return visited[tuple(node)]
    
    def get_childs(self,pairs,node):
        childs=[]
        for i in pairs:
            if i[0]>node[1]:
                childs.append(i)
        return childs