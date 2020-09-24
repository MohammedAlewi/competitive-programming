# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        values = defaultdict(lambda:[])
        self.collect_nodes(root,values)
        
        result = []
        keys = sorted(values.keys())
        for key in keys:
            if key %2 == 0:
                result.append( values[key] )
            else:
                result.append( reversed(values[key]) )
                
        return result
        
    def collect_nodes(self,node,values,count=0):
        if not node:
            return
        
        values[count].append(node.val)
        
        self.collect_nodes(node.left,values,count+1)
        self.collect_nodes(node.right,values,count+1)        
