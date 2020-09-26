# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        root_2 = TreeNode()
        self.helper(root,root_2)
        return root_2
    
    
    def helper(self,root_1,root_2):
        
        root_2.val = root_1.val
        
        if root_1.left:
            root_2.right = TreeNode()
            self.helper(root_1.left,root_2.right)
        
        if root_1.right:
            root_2.left = TreeNode()
            self.helper(root_1.right,root_2.left)
        
