# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.preorder=None
        self.bsd=[]
    def bstFromPreorder(self, preorder) -> TreeNode:
        self.preorder=preorder
        self.bsd=[0]*(len(preorder)+5)
        self.bsd.insert(0,self.preorder[0])
        self.construct()
        
        return self.bsd
        
    def construct(self):
        print(self.bsd)
        for i in range(1,len(self.preorder)):
            for j in range(1,len(self.bsd)):
                if self.bsd[j]!=None and self.bsd[j]>self.preorder[i]:
                    self.bsd[2*j-1]=self.preorder[i]
                elif self.bsd[j]!=None and self.bsd[j]<=self.preorder[i]:
                    self.bsd[2*j+1]=self.preorder[i]
            
x=Solution()
f=x.bstFromPreorder([8,5,1,7,10,12])
print(f)