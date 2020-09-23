# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
      
      arr= []
      queue= deque()
      if root:
        queue.append((root,0))
      
      
      while len(queue):
        node,index = queue.popleft()
        
        if len(arr) <= index:
          arr.append(node.val)
        else:
          arr[index] = max(arr[index] , node.val)
          
        if node.left:
          queue.append( (node.left,index+1) )
        
        if node.right:
          queue.append( (node.right,index+1) )
          
        
      return arr
      
        
    
