# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.find_hight(root)
        
        
        
    def find_hight(self,root):
        if root==None:
            return float('inf')
        if root.left == root.right == None:
            return 1
        
        return 1 + min(self.find_hight(root.left),self.find_hight(root.right))
        
