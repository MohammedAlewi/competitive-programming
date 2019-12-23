# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.dict={}
        
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.search(root,1)
        self.dict[0]=root.val
        x=max(list(self.dict.keys()))
        return self.dict[x]
    
    def search(self,root,x):
        x+=1
        if root!=None and root.right!=None:
            self.dict[x]=root.right.val
        if root!=None and root.left!=None:
            self.dict[x]=root.left.val
        if root!=None:
            self.search(root.right,x)
            self.search(root.left,x)
        