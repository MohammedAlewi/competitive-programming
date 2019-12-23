import math
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.values=[]
        self.ans=0
    def longestUnivaluePath(self, root):
        self.get(root.left,root.val)
        self.get(root.right,root.val)
        return self.ans

    def get(self,tree,upper):
        if tree==None: return
        if tree.val-upper< self.ans and self.ans!=0:
            self.ans= tree.val-upper
        self.locate(tree.left,tree.val)
        self.locate(tree.left,tree.val)

    
                    

