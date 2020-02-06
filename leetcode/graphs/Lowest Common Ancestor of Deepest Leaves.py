# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        return self.dfs(root,0)[1]
    
    def dfs(self,root,curr):
        if root==None:
            return curr,root
        val1=self.dfs(root.left,curr+1)
        val2=self.dfs(root.right,curr+1)
        if val1[0]==val2[0]:
            return val1[0],root
        elif val1[0]>val2[0]: 
            return val1
        return val2