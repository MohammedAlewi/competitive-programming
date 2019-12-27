# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.original=None
        
    def searchBST(self, root: TreeNode, val: int,x=None) -> TreeNode:
        x=TreeNode(3)
        self.get(root,val,x)
        
        return self.original
        
    def get(self,root,val,x):
        if root!=None and root.val==val:
            self.copy(root)
           
        elif root!=None :
            self.get(root.left,val,x)
            self.get(root.right,val,x)
        
    def copy(self,original):
        self.original=original
        