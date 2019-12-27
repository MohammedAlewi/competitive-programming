# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.answer=True
        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        self.check(p,q)
        return self.answer
    
    def check(self,p,q):
        if p!=None and q!=None and p.val!=q.val:
            self.answer=False
        elif p!=None and q==None or  q!=None and p==None: 
            self.answer=False
        if  p!=None and q!=None:
            self.check(p.left,q.left)            
            self.check(p.right,q.right)