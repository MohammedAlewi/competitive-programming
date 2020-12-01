class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result,total = [], [] 
        self.findPossibleMoves(n,(-1,-1),set(), [],total)
  
        for sln in total:
            result.append(self.construct(sln,n) )
        
        return result
        
    def bound(self,pos,n):
        return 0 <= pos[0]< n and 0 <= pos[1]< n 
    
    
    def findPossibleMoves(self,n,node,visited,queens,totals):
        if node[0] == n-1:
            totals.append(queens)
        
        for i in range(n):
            
            new = (node[0]+1,i)
            checks = set([(1,0,new[1]),(2,new[0],0)])
            
            counter = 0
    
            for val in queens:
                if  val[1] - new[1] and abs((val[0] - new[0]) /  (val[1] - new[1])) != 1:
                    counter += 1
                
              
            if counter != len(queens):
                continue
            
            if self.bound(new,n) and not len(visited.intersection(checks)):
                
                visited = visited.union(checks)
                x = queens.copy()
                x.append(new)
                self.findPossibleMoves(n,new,visited,x,totals)                    
                visited -= checks
    
    
    def construct(self,sln,n):
        res = []
        
        for _,j in sln:
            r = ['.'] *(n)
            r[j] = 'Q'
            res.append( "".join(r) )
            
        return res
        
