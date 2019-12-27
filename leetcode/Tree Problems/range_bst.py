# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, node: TreeNode, l: int, r: int) -> int:
        sum_= self.calculate(node,l,r)
        return sum_
        
        
    def calculate(self,node,l,r):
        x=node.val if node.val >=l and node.val <= r else 0
       
        if node.left!=None and node.val>=l:
            x+=self.calculate(node.left,l,r)
        if node.right!=None  and node.val <=r:
            x+=self.calculate(node.right,l,r)
        return x