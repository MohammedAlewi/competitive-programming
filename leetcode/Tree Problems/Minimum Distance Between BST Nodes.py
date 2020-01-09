import math
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        values=[]
        self.find_all(root,values)
        values.sort()
        
        return self.find_min(values)

    def find_all(self,tree,values):
        if tree!=None:
            values.append(tree.val)
            self.find_all(tree.left,values)
            self.find_all(tree.right,values)
        
    def find_min(self,values):
        x=None
        for i in range(len(values)-1):
            val=abs(values[i]-values[i+1])
            if x==None:
                x=val
            elif x>val:
                x=val
        return x
            