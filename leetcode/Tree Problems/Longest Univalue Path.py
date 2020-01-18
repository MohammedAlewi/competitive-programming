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

    def locate(self,tree,value,counter):
        if tree==None: return
        if tree.val==value:
            counter+=1
        elif self.ans.get(tree.val)==None:
                self.ans[tree.val]=counter
                counter=0
        elif self.ans.get(tree.val)<counter:
                self.ans[tree.val=counter
                counter=0
        self.locate(tree.left,tree.val,counter)
        self.locate(tree.right,tree.val,counter)
            


