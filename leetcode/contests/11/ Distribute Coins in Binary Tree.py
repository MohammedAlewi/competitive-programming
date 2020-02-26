# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        ans=self.do_preporder(root)
        return ans[0]
    
    
    def do_preporder(self,root):
        if root!=None:
            
            count_left,coin_left=self.do_preporder(root.left)
            
            count_right,coin_right=self.do_preporder(root.right)
            
            
            total=coin_left+coin_right
            total_c=count_left+count_right
            
            if root.val==0:
                total-=1
                # total_c+=abs(total)
                
            elif root.val>1:
                total+=(root.val-1)
                # total_c+=abs(total)
                
            total_c+=abs(total)
                
            return total_c,total
        
        return 0,0
                
                
            