# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def findNodes(root):
            nonlocal result
            
            if not root:
                return False,0
            
            if root == target:
                fillResult(root,K+1)
                return True, 1
            
            left, i = findNodes(root.left)
            right, j = findNodes(root.right)
                
            
            if K - max(i,j) == 0:
                result.append(root.val)
                return False,0
            
            elif left:
                fillResult(root.right,K - i)
                return True,i + 1
            
            elif right:
                fillResult(root.left,K - j)
                return True,j + 1
            
            return False,0 
                
        def fillResult(root,pos):
            nonlocal result 
            
            q= deque([(root,1)])
            while q:
                node, d = q.popleft()
                
                if d == pos and node:
                    result.append(node.val)
                    
                if d < pos and node:
                    q.append( (node.left, d+1) )
                    q.append( (node.right, d+1) )
                
            
        result = []
        
        if K == 0:
            return [target.val]
        
        findNodes(root)
        return result
