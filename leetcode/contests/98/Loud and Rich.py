class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        values=set()
        order=[i for i in range(len(quiet))]
        
        get_childs=self.get_childs(richer,len(quiet))
        if not len(richer): return order
        
        for i in range(len(quiet)):
            visited={}
            self.change_val(quiet,i,order,i,visited,get_childs)
            
        return order
    
    def change_val(self,quiet,node,order,ord_node,visited,childerns):
        if quiet[node]<=quiet[order[ord_node]]:
            order[ord_node]=node
            
        visited[node]=True    
        for i in childerns[node]:
            if i not in visited:
                self.change_val(quiet,i,order,ord_node,visited,childerns)
        
        
    def get_childs(self,richer,n):
        childs={}
        for j in range(n):
            childs[j]=[]
            for i in richer:
                if i[1]==j:
                    childs[j].append(i[0])
                
        return childs