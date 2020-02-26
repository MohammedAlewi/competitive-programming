class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        children=self.get_children(nums)
        visited={}
        ans=0
        for i in range(len(nums)):
            curr=self.do_dfs(i,nums,children,visited)
            if ans<curr:
                ans=curr
                
        return ans
    
    
    def do_dfs(self,node,nums,children,visited):
        if visited.get(node)!=None:
            return visited[node]
        
        ans=0
        for child in children[node]:
            current= self.do_dfs(child,nums,children,visited)
            if ans<current:
                ans=current
                
        visited[node]=1+ans
        return visited[node]
    
    
    
    def get_children(self,nums):
        children={}
        for i in range(len(nums)):
            children[i]=[]
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    children[i].append(j)
        return children