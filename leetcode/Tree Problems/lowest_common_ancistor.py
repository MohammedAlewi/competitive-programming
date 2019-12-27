# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.common=None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.common=None
        self.advance(root,p,q)
        return self.common
    
    def advance(self,root,p,q):
        if self.check(root,p)==True and self.check(root,q)==True:
                self.common=root
        if root!=None:
            self.advance(root.left,p,q)
            self.advance(root.right,p,q)
            
    def check(self,root,p):
        if root!=None and root.val ==p.val:
            return True
        elif root!=None:
            return self.check(root.left,p) or self.check(root.right,p)
        else:return False
        