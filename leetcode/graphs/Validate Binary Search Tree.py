# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        values=[]
        self.do_dfs(root,values)
        for i in range(len(values)-1):
            if values[i]>=values[i+1]:
                return False
        return True
    
    def do_dfs(self,root,values):
        if root!=None:
            self.do_dfs(root.left,values)
            values.append(root.val)
            self.do_dfs(root.right,values)
            