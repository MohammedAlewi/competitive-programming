from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
      children = self.get_children(edges)
      visited = set([0])
      
      result = self.do_dfs(children,0,visited,hasApple)
      
      return result[1]
      
      
    def do_dfs(self,children,node,visited,has_apple):
      status =False
      time = 0
      
      for i in children[node]:
        if i not in visited:
          visited.add(i)
          found = self.do_dfs(children,i,visited,has_apple)
          if found[0]:
            time += 2 + found[1]  
            status = True
            
      if has_apple[node]:
        status = True
        
      return status,time
    
    
    def get_children(self,edges):
      children = defaultdict(lambda:[])
      
      for edge in edges:
        
        children[edge[0]].append(edge[1])        
        children[edge[1]].append(edge[0])
        
      return children
