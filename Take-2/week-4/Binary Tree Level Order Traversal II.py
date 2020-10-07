# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        values = []
        queue = deque([(0,root)])
        
        while queue:
            node = queue.popleft()
            if len(values) <= node[0]:
                values.append([])
            
            values[node[0]].append(node[1].val)
            
            if node[1].left:
                queue.append((node[0]+1,node[1].left))
            if node[1].right:
                queue.append((node[0]+1,node[1].right))
            
            
        return values[::-1]
            
        
