# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, total_sum: int) -> List[List[int]]:
        total_paths = []
    
        
        def find_path(root,total,collected):
            if root == None:
                return
            
            if root.left == root.right == None and total - root.val == 0:
                collected.append(root.val)
                return total_paths.append( collected )
                
        
            collected.append(root.val)
            
            find_path( root.left, total-root.val, collected.copy())
            find_path( root.right, total-root.val, collected.copy())
        
        
        find_path(root,total_sum,[])
        return total_paths
        
        
        
