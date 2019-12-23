# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        l=root
        self.insertVal(l,val)
        root=self.print_tree(root)
        return root

    def insertVal(self,root,val):
        if root==None:
           return TreeNode(val) 
        elif root.val>val: 
            root.left=self.insertVal(root.left,val)
        else:
            root.right=self.insertVal(root.right,val)
        return root
    def print_tree(self,root,x=0):
        if root==None:return
        print(x,":",root.val)
        self.print_tree(root.left,2*x+1)
        self.print_tree(root.right,2*x+2)


l=TreeNode(4)
x=l
x.left=TreeNode(2)
x.right=TreeNode(7)
x.left.left=TreeNode(1)
x.left.right=TreeNode(3)
g=Solution()
g.print_tree(l)
print()
g.insertIntoBST(l,0)
print()


