# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        values=[]
        self.get_sums(root,values)
        l=values
        l.sort()
        max_val=0
        root_val=l[-1]
        print(l)
        for i in range(len(l)-2,-1,-1):
            x=((root_val-l[i])*l[i])
            if max_val<x:
                max_val=x
                print(root_val,l[i])
        return max_val%(pow(10,9)+7)
    
    
    def get_sums(self,root,values):
        vals=0
        if root!=None:
            left=self.get_sums(root.left,values)
            right=self.get_sums(root.right,values)
            vals=root.val
            vals=(left+right+vals)
            values.append(vals)
        return vals
        