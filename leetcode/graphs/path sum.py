# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root==None:return False
        return self.find_path(root,0,sum)
    
    def find_path(self,root,vals,num):
        if root!=None and root.left==None and root.right==None:
            vals+=root.val
            return vals == num
        if root==None: return False
        vals+=root.val
        return self.find_path(root.left,vals,num) or self.find_path(root.right,vals,num) 