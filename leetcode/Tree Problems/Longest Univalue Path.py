import math
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans={}
    def longestUnivaluePath(self, root):
        self.locate(root,None)
        max_distance=max(self.ans.values())
        print(self.ans)
        return max_distance

    def locate(self,tree,value):
        if tree==None: return
        if tree.val==value:
            self.ans[value]+=1
        else:
            self.ans[tree.val]=0
        self.locate(tree.left,tree.val)
        self.locate(tree.right,tree.val)
            


