class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        visited={}
        val=self.do_dfs(triangle,(0,0),visited)
        return val
    
    def do_dfs(self,triangle,node,visited):
        if visited.get(node)!=None:
            return visited[node]
        
        childs=self.get_childs(triangle,node)
        
        min_result=0
        if len(childs)==2:
            min_result1=self.do_dfs(triangle,childs[0],visited)
            min_result2=self.do_dfs(triangle,childs[1],visited)
            min_result=min(min_result1,min_result2)
            
        elif len(childs):
            min_result=self.do_dfs(triangle,childs[0],visited)
    
        visited[node]=min_result+triangle[node[0]][node[1]]
        return visited[node]
    
    def get_childs(self,triangle,node):
        childs=[]
        
        if node[0]+1<len(triangle):
            childs.append((node[0]+1,node[1]))
            childs.append((node[0]+1,node[1]+1))
        return childs
        