# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        queue=[root]
        result=0
        while(len(queue)>0):
            tree=queue.pop(0)
            if tree!=None and tree.val%2==0:
                result+=self.dfs(tree,0,2)
            if tree!=None:
                queue.append(tree.left)
                queue.append(tree.right)
        return result
    
    def dfs(self,root,curr,limit):
        if root==None:
            return 0
        if curr==limit:
            return root.val
        return self.dfs(root.left,curr+1,limit)+ self.dfs(root.right,curr+1,limit)
                    
        