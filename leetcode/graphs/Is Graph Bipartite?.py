class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited_edge={}
        visited_node={}
        val=True
        for i in range(len(graph)):
            if visited_node.get(i)==None:
                visited_node[0]=0
                val = val and self.do_dfs(visited_edge,visited_node,graph,1,i)
        return val
    
    def do_dfs(self,visited_edge,visited_node,graph,count,node):
        val=True
        for i in graph[node]:
            if visited_edge.get((node,i))==None:
                visited_edge[(node,i)]=True
                visited_edge[(i,node)]=True
                if visited_node.get(i)==None:
                    visited_node[i]=count
                    val= val and self.do_dfs(visited_edge,visited_node,graph,count+1,i)
                elif (count-visited_node[i])%2!=0:
                    return False
        return val