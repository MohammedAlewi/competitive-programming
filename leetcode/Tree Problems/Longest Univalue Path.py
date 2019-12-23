import math
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.locations={}
        self.ans={}
    def longestUnivaluePath(self, root):
        self.locate(root,0)
        return self.calculate()

    def locate(self,tree,loc):
        if tree==None: return
        if self.locations.get(tree.val)==None:
            self.locations[tree.val]=[]
        self.locations[tree.val].append(loc)
        self.locate(tree.left,2*loc+1)
        self.locate(tree.right,2*loc+2)

    def calculate(self):
        print(self.locations)
        for i in self.locations.keys():
            s=list(self.locations[i])
            s.sort()
            x=s[len(s)-1]
            y=s[len(s)-2] if len(s)>=2 else s[len(s)-1]
            length=0
            while(x!=y):
                if y<x:
                    x=abs(x-1)/2 if x%2!=0 else abs(x-2)/2 
                    x=0 if x==0 else int(x)
                    length+=1
                elif y>x:
                    y=abs(y-1)/2 if y%2!=0 else abs(y-2)/2 
                    y=0 if y==0 else int(y)
                    length+=1                         
            self.ans[i]=length
        x=sorted(list(self.ans.values()),reverse=True)
        return x[0]
            
s=Solution()
l=TreeNode(1)
x=l
x.left=TreeNode(4)
x.right=TreeNode(5)
x.left.left=TreeNode(4)
x.left.right=TreeNode(4)
x.right.right=TreeNode(5)
print(s.longestUnivaluePath(l))
                    

