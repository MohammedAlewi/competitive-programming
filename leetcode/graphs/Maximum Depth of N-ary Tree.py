"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root==None:return 0
        count=self.find_max(root,0)
        return count
        
    def find_max(self,root,count):
        count+=1
        if len(root.children)==0:
            return count
        values=0
        for node in range(len(root.children)):
            val=self.find_max(root.children[node],count)
            if values<val: values=val
        return values