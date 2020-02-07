class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited={}
        return self.do_dfs(arr,visited,start)
    
    def do_dfs(self,arr,visited,index):
        ans=False
        
        if arr[index]==0:
            return True
        childs=self.childrens(index,arr[index],len(arr),visited)
        
        for i in childs:
            if visited.get(i)==None:
                visited[i]=True
                ans= ans or self.do_dfs(arr,visited,i)
        return ans
    
    def childrens(self,index,val,length,visited):
        childs=[]
        
        if index-val>=0 :#and visited.get(index-val)==None:
            childs.append(index-val)
            
        if index+val<length:# and visited.get(index+val)==None:
            childs.append(index+val)
            
        return childs
        