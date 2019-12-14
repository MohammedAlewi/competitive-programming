# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        t3=TreeNode(None)
        self.const(t1,t2,t3)
        return t3 if t3.val!=0 else None
    
    def const(self,t1,t2,t3):
        if t1!=None and  t2!=None :
            t3.left=TreeNode(None)
            t3.right=TreeNode(None)
            t3.val=(t1.val +t2.val) 
            self.const(t1.left,t2.left,t3.left)
            self.const(t1.right,t2.right,t3.right)
        elif t1!=None:
            t3.val=(t1.val) 
            t3.left=t1.left
            t3.right=t1.right
        elif t2!=None:
            t3.val=(t2.val) 
            t3.left=t2.left
            t3.right=t2.right
        else: t3.val=t2.val