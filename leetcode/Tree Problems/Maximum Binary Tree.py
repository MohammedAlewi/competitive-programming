# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.left=[]
        self.right=[]
    def constructMaximumBinaryTree(self, nums) -> TreeNode:
        if len(nums)==0: return None
        m=max(nums)
        index=nums.index(m)
        left=nums[:index]
        right=nums[index+1:]
        tree=TreeNode(m)
        tree.left=self.constructMaximumBinaryTree(left)
        tree.right=self.constructMaximumBinaryTree(right)
        return tree

    def print_tree(self,root,x=0):
        if root==None:return
        print(x,":",root.val)
        self.print_tree(root.left,2*x+1)
        self.print_tree(root.right,2*x+2)



g=Solution()
x=g.constructMaximumBinaryTree([3,2,1,6,0,5])

g.print_tree(x)
print()


