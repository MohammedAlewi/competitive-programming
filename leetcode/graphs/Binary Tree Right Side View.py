# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        level={}
        self.dfs(root,level,0)
        view=list(level.values())
        return view
    
    
    def dfs(self, root,level,count):
        if root!=None:
            level[count]=root.val
            self.dfs(root.left,level,count+1)
            self.dfs(root.right,level,count+1)
        
        