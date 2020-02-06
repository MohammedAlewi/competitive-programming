class Solution:
    def __init__(self):
        self.costs={}
        
    def maxJumps(self, arr: List[int], d: int) -> int:
        vals=[]
        for i in range(len(arr)):
            x=self.do_jumps(i,d,arr)
            vals.append(x)
        return max(vals)
    
    def do_jumps(self,index,d,arr):
        if index in self.costs.keys():
            return self.costs[index]
        
        childs=self.childrens(index,d,arr)
        vals=[1]
        for i in childs:
            x=self.do_jumps(i,d,arr)
            vals.append(x+1)
        
        self.costs[index]=max(vals)
        return self.costs[index]
    
    def childrens(self,index,d,arr):
        childrens=[]
        left_limit=max(index-d,0)        
        right_limit=min(index+d,len(arr)-1)
        l=index-1
        r=index+1
        while l >=left_limit and arr[l]<arr[index]:
            childrens.append(l)
            l-=1
            
        while r <=right_limit and arr[r]<arr[index]:
            childrens.append(r)
            r+=1
        return childrens
